#!/usr/bin/env python3
"""
AI Library pre-commit validation hook.
Blocks on structural violations. Warns on advisory checks.

Install:
    cp pre-commit.py .git/hooks/pre-commit
    chmod +x .git/hooks/pre-commit
"""

import os
import re
import sys
import subprocess

# ── Helpers ──────────────────────────────────────────────────────────────────

def staged_files():
    result = subprocess.run(
        ["git", "diff", "--cached", "--name-only", "--diff-filter=ACM"],
        capture_output=True, text=True
    )
    return [f for f in result.stdout.strip().splitlines() if f]

def read_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except (FileNotFoundError, UnicodeDecodeError):
        return None

def repo_root():
    result = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        capture_output=True, text=True
    )
    return result.stdout.strip()

# ── Patterns ─────────────────────────────────────────────────────────────────

# Matches versioned project files: v01--artifact.md, v03--context.md, etc.
VN_PREFIX = re.compile(r"^v(\d{2})--(.+)$")



FRONTMATTER_BLOCK = re.compile(r"^---\n(.+?)\n---", re.DOTALL)

REQUIRED_FRONTMATTER_KEYS = {"title", "date", "updated", "type", "vendor", "model", "tags", "related"}
VALID_TYPES = {"document", "code", "context"}

CONTEXT_SECTIONS = ["PROJECT:", "DECISIONS:", "RULED OUT:", "OPEN:", "STATE:"]
INSTRUCTIONS_SECTIONS = [
    "PROJECT:", "GOAL:", "BACKGROUND:", "ARTIFACT STATE:",
    "KEY DECISIONS:", "OPEN QUESTIONS:", "EXPLICITLY RULED OUT:",
    "NEXT TASK:", "PERSONA:", "STYLE AND CONSTRAINTS:"
]

EXCLUDED = {
    ".git",
    "temp",
    ".DS_Store",
    ".gitignore",
    "MAP.md",
    "MASTER-PROMPT.md",
    "CLAUDE.md",
    "ARCHITECTURE.tex",
    "USER-GUIDE.tex",
    "THREAD.md",
    "persona.md",
    "SKILL.md",   # skill framework files use their own frontmatter schema
    ".deploy",    # per-project deploy marker (declares artifact deploy targets)
}

DEPLOY_MARKER = ".deploy"

def is_skill_framework_file(path):
    """True for skill framework files: SKILL.md and files inside references/ dirs.
    Skill packages may include subdirectories (e.g. references/) whose .md files
    are skill content, not library documents — they need no frontmatter or MAP entry.
    """
    base = os.path.basename(path)
    if base == "SKILL.md":
        return True
    parts = path.replace("\\", "/").split("/")
    # references/ is a known skill subdirectory — exclude all files inside it
    return "references" in parts[:-1]

# ── Check functions ───────────────────────────────────────────────────────────

errors   = []   # block commit
warnings = []   # print but allow

def err(msg):
    errors.append(f"  ERROR   {msg}")

def warn(msg):
    warnings.append(f"  WARNING {msg}")


def check_vn_naming(filename):
    """Two-digit version prefix required on versioned project files."""
    base = os.path.basename(filename)
    m = re.match(r"^v(\d+)--", base)
    if m:
        digits = m.group(1)
        if len(digits) != 2:
            err(f"{filename}: version prefix must be two digits (v01 not v{digits})")


def check_frontmatter(filename, content):
    """Standalone files must have complete, valid YAML frontmatter."""
    base = os.path.basename(filename)
    # Only check standalone files (not versioned project files, not .tex, not .py)
    ext = os.path.splitext(base)[1].lower()
    if ext not in (".md", ".txt"):
        return
    if VN_PREFIX.match(base):
        return
    if base in EXCLUDED:
        return
    if is_skill_framework_file(filename):
        return

    m = FRONTMATTER_BLOCK.match(content)
    if not m:
        err(f"{filename}: missing YAML frontmatter block")
        return

    block = m.group(1)
    found_keys = set()
    for line in block.splitlines():
        if ":" in line:
            key = line.split(":", 1)[0].strip()
            found_keys.add(key)

    missing = REQUIRED_FRONTMATTER_KEYS - found_keys
    if missing:
        err(f"{filename}: frontmatter missing keys: {', '.join(sorted(missing))}")

    # Validate type value
    type_match = re.search(r"^type:\s*(.+)$", block, re.MULTILINE)
    if type_match:
        type_val = type_match.group(1).strip()
        if type_val not in VALID_TYPES:
            err(f"{filename}: frontmatter type '{type_val}' invalid — must be one of: {', '.join(VALID_TYPES)}")


def check_triplet(staged):
    """
    Lockstep rule: if any versioned project file (artifact, context, instructions)
    is staged, all three at the same vNN must be present (staged or committed).
    A version mismatch within the same project folder also blocks.
    """
    root = repo_root()

    def exists_anywhere(path):
        if path in staged:
            return True
        return os.path.isfile(os.path.join(root, path))

    # Collect all vNN files in staged, grouped by (dirname, nn)
    from collections import defaultdict
    groups = defaultdict(set)  # (dirname, nn) -> set of stems staged

    for f in staged:
        base = os.path.basename(f)
        dirname = os.path.dirname(f)
        m = VN_PREFIX.match(base)
        if not m:
            continue
        nn = m.group(1)
        groups[(dirname, nn)].add(f)

    for (dirname, nn), members in groups.items():
        artifact_path     = None
        context_path      = os.path.join(dirname, f"v{nn}--context.md")
        instructions_path = os.path.join(dirname, f"v{nn}--instructions.md")

        # Find the artifact (any extension)
        for f in members:
            base = os.path.basename(f)
            stem = VN_PREFIX.match(base).group(2).split(".")[0]
            if stem == "artifact":
                artifact_path = f
                break
        # Also check disk for artifact if not staged
        if artifact_path is None:
            project_dir = os.path.join(root, dirname)
            if os.path.isdir(project_dir):
                for fname in os.listdir(project_dir):
                    m = VN_PREFIX.match(fname)
                    if m and m.group(1) == nn:
                        stem = m.group(2).split(".")[0]
                        if stem == "artifact":
                            artifact_path = os.path.join(dirname, fname)
                            break

        if artifact_path is None:
            # One of context/instructions staged but no artifact at this version
            for f in members:
                err(f"{f}: staged at v{nn} but no matching artifact file found at v{nn}")
        else:
            if not exists_anywhere(context_path):
                err(f"{artifact_path}: triplet incomplete — {context_path} not found")
            if not exists_anywhere(instructions_path):
                err(f"{artifact_path}: triplet incomplete — {instructions_path} not found")

        # Check for version mismatch: other vNN files in same folder staged at different version
        for f in staged:
            base = os.path.basename(f)
            fdir = os.path.dirname(f)
            if fdir != dirname:
                continue
            fm = VN_PREFIX.match(base)
            if fm and fm.group(1) != nn:
                other_nn = fm.group(1)
                err(f"{f}: version mismatch in {dirname or 'root'} — v{nn} and v{other_nn} staged together")


def check_context_sections(filename, content):
    """context.md files must contain all required section headers."""
    base = os.path.basename(filename)
    m = VN_PREFIX.match(base)
    if not m:
        return
    if "context" not in base:
        return
    for section in CONTEXT_SECTIONS:
        if section not in content:
            warn(f"{filename}: missing section '{section}' in context file")


def check_instructions_sections(filename, content):
    """instructions.md files must contain all required section headers."""
    base = os.path.basename(filename)
    m = VN_PREFIX.match(base)
    if not m:
        return
    if "instructions" not in base:
        return
    for section in INSTRUCTIONS_SECTIONS:
        if section not in content:
            warn(f"{filename}: missing section '{section}' in instructions file")


def check_map_coverage(staged):
    """Block if a docs/ or inbox/ file has no entry in MAP.md. Warn for others."""
    root = repo_root()
    map_path = os.path.join(root, "MAP.md")
    map_content = read_file(map_path) or ""

    for f in staged:
        base = os.path.basename(f)
        if base in EXCLUDED:
            continue
        if is_skill_framework_file(f):
            continue
        if base not in map_content and f not in map_content:
            # docs/ and inbox/ files must always be indexed — block the commit
            warn(f"{f}: not referenced in MAP.md")


def check_map_integrity():
    """Warn if any path listed in MAP.md does not resolve to a real file."""
    root = repo_root()
    map_path = os.path.join(root, "MAP.md")
    map_content = read_file(map_path)
    if not map_content:
        return

    # Match only paths that contain at least one directory separator
    path_pattern = re.compile(r"[\w.-]+(?:/[\w.-]+)+\.[\w]+")
    candidates = path_pattern.findall(map_content)

    for candidate in candidates:
        if candidate.startswith("http") or "#" in candidate:
            continue
        full = os.path.join(root, candidate)
        if not os.path.isfile(full):
            warn(f"MAP.md references '{candidate}' but file not found on disk")


def check_thread_order():
    """Warn if any THREAD.md has checkpoint entries out of ascending version order."""
    root = repo_root()

    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d != ".git"]
        if "THREAD.md" not in filenames:
            continue
        thread_path = os.path.join(dirpath, "THREAD.md")
        content = read_file(thread_path)
        if not content:
            continue

        # Extract vNN only from checkpoint header lines
        # Matches lines like: "### v01 —", "THREAD ENTRY v01"
        version_refs = []
        for line in content.splitlines():
            m = re.match(r"^(?:#+\s+|THREAD ENTRY\s+)[vV](\d{2})\b", line)
            if m:
                version_refs.append(int(m.group(1)))

        if not version_refs:
            continue

        nums = version_refs
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                rel = os.path.relpath(thread_path, root)
                warn(
                    f"{rel}: version order broken — "
                    f"v{nums[i]:02d} appears after v{nums[i-1]:02d}"
                )




def check_master_prompt_sync(staged):
    """
    Regenerate-and-diff guard for deployed artifacts (e.g. MASTER-PROMPT.md).
    For any project carrying a .deploy marker, if its latest artifact OR a declared
    deploy target is staged, that target must be byte-identical to the latest artifact
    (deploy is verbatim — the ARTIFACT vNN label is kept). Mirrors the standard
    'touch source -> regenerate -> fail if stale' pattern. Scoped to staged prompt
    source/output only, so unrelated commits — and the transitional state before the
    first auto-deploy heals a stale target — are never blocked.
    """
    root = repo_root()
    projects_dir = os.path.join(root, "projects")
    if not os.path.isdir(projects_dir):
        return
    staged_set = set(staged)
    for slug in sorted(os.listdir(projects_dir)):
        pdir = os.path.join(projects_dir, slug)
        marker = os.path.join(pdir, DEPLOY_MARKER)
        if not os.path.isfile(marker):
            continue
        targets = [ln.strip() for ln in (read_file(marker) or "").splitlines() if ln.strip()]
        if not targets:
            continue

        # Latest artifact in the project (any extension).
        latest_name, latest_nn = None, -1
        for fn in os.listdir(pdir):
            m = re.match(r"^v(\d{2})--artifact\.", fn)
            if m and int(m.group(1)) > latest_nn:
                latest_nn, latest_name = int(m.group(1)), fn
        if latest_name is None:
            continue

        artifact_rel = f"projects/{slug}/{latest_name}"
        touched = artifact_rel in staged_set or any(t in staged_set for t in targets)
        if not touched:
            continue  # prompt source/output not being changed — nothing to enforce

        expected = read_file(os.path.join(pdir, latest_name)) or ""
        for t in targets:
            deployed = read_file(os.path.join(root, t))
            if deployed is None:
                err(f"{t}: deploy target missing — expected a verbatim copy of {artifact_rel}")
            elif deployed != expected:
                err(f"{t}: out of sync with {artifact_rel} — re-run the checkpoint deploy "
                    f"(verbatim) before committing")


def check_artifact_wrapper(filename, content):
    """Artifact files must be non-empty and begin with 'ARTIFACT v[NN]' matching filename version."""
    base = os.path.basename(filename)
    m = VN_PREFIX.match(base)
    if not m:
        return
    stem = m.group(2).split(".")[0]
    if stem != "artifact":
        return

    if not content or not content.strip():
        err(f"{filename}: artifact file is empty")
        return

    # First non-blank line must be "ARTIFACT v[NN]"
    first_line = ""
    for line in content.splitlines():
        if line.strip():
            first_line = line.strip()
            break

    label_match = re.match(r"^ARTIFACT v(\d{2})$", first_line)
    if not label_match:
        err(f"{filename}: first line must be 'ARTIFACT v[NN]' — got '{first_line}'")
        return

    # Label version must match filename version
    label_nn = label_match.group(1)
    file_nn = m.group(1)
    if label_nn != file_nn:
        err(f"{filename}: label 'ARTIFACT v{label_nn}' does not match filename version v{file_nn}")


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    files = staged_files()

    # Per-file checks
    for f in files:
        base = os.path.basename(f)
        if base in EXCLUDED:
            continue
        content = read_file(f)
        if content is None:
            continue
        check_vn_naming(f)
        check_frontmatter(f, content)
        check_artifact_wrapper(f, content)
        check_context_sections(f, content)
        check_instructions_sections(f, content)

    # Cross-file checks
    check_triplet(files)
    check_map_coverage(files)
    check_map_integrity()
    check_thread_order()
    check_master_prompt_sync(files)

    # Report
    if warnings:
        print("\n[pre-commit] WARNINGS (commit will proceed):")
        for w in warnings:
            print(w)

    if errors:
        print("\n[pre-commit] ERRORS (commit blocked):")
        for e in errors:
            print(e)
        print("\nFix the errors above, or use --no-verify to bypass.\n")
        sys.exit(1)

    if warnings:
        print()  # blank line after warnings before git proceeds

    sys.exit(0)


if __name__ == "__main__":
    main()