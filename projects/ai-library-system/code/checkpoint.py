#!/usr/bin/env python3
"""
checkpoint.py — AI Library checkpoint automation script.

Source:  projects/ai-library-system/code/checkpoint.py
Deploys: code/checkpoint.py (library root)

Usage:
  checkpoint.py <project-slug> <version> [input-file] [--write]

  project-slug   folder name under projects/ (e.g. ai-library-system)
  version        two-digit version number (e.g. 09)
  input-file     path to checkpoint text file (optional)
                 default: temp/v[NN]-checkpoint.txt inside library root
  --write        execute all writes; omit for dry-run (default)
"""

import sys
import re
from datetime import datetime, timezone
from pathlib import Path


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

BLOCKS = ["ARTIFACT", "CONTEXT", "INSTRUCTIONS", "THREAD ENTRY"]

BLOCK_PATTERNS_TILDE = {
    name: re.compile(
        rf"^~~~[^\n]*\n{re.escape(name)} v(\d{{2}})\n(.*?)^~~~",
        re.MULTILINE | re.DOTALL,
    )
    for name in BLOCKS
}

BLOCK_PATTERNS_4 = {
    name: re.compile(
        rf"^````[^\n]*\n{re.escape(name)} v(\d{{2}})\n(.*?)^````",
        re.MULTILINE | re.DOTALL,
    )
    for name in BLOCKS
}

BLOCK_PATTERNS_3 = {
    name: re.compile(
        rf"^```[^\n]*\n{re.escape(name)} v(\d{{2}})\n(.*?)^```\s*$",
        re.MULTILINE | re.DOTALL,
    )
    for name in BLOCKS
}

THREAD_ARTIFACT_RE     = re.compile(r"^\*\*Artifact:\*\*\s*(.+)$",     re.MULTILINE)
THREAD_CONTEXT_RE      = re.compile(r"^\*\*Context:\*\*\s*(.+)$",      re.MULTILINE)
THREAD_INSTRUCTIONS_RE = re.compile(r"^\*\*Instructions:\*\*\s*(.+)$", re.MULTILINE)

# Append-only sections in context files — checked for dropped lines
APPEND_ONLY_SECTIONS = ["DECISIONS", "RULED OUT"]

# Size ratio thresholds for truncation heuristics
ARTIFACT_MIN_RATIO = 0.80   # new artifact must be >= 80% of previous size
CONTEXT_MIN_RATIO  = 0.90   # new context must be >= 90% of previous size


DEFAULT_ARTIFACT_EXT = "md"


# ---------------------------------------------------------------------------
# Artifact extension resolution
# ---------------------------------------------------------------------------

def find_artifact_path(project_dir: Path, version: str) -> Path | None:
    """Find the existing v[NN]--artifact.[ext] file for a version, any extension."""
    matches = sorted(project_dir.glob(f"v{version}--artifact.*"))
    return matches[0] if matches else None


def resolve_artifact_extension(project_dir: Path, prev_version: str) -> str:
    """
    New artifacts keep the same file extension as the previous version's
    artifact by default (the checkpoint blocks carry no extension field of
    their own). Falls back to DEFAULT_ARTIFACT_EXT when there is no previous
    artifact to inherit from (e.g. v01).
    """
    prev_path = find_artifact_path(project_dir, prev_version)
    if prev_path is not None:
        return prev_path.suffix.lstrip(".")
    return DEFAULT_ARTIFACT_EXT


# ---------------------------------------------------------------------------
# Deploy (artifact body -> declared targets, e.g. MASTER-PROMPT.md)
# ---------------------------------------------------------------------------

DEPLOY_MARKER = ".deploy"


def deploy_targets(project_dir: Path) -> list:
    """Read declared deploy targets — one library-root-relative path per line."""
    marker = project_dir / DEPLOY_MARKER
    if not marker.exists():
        return []
    return [ln.strip() for ln in marker.read_text(encoding="utf-8").splitlines() if ln.strip()]


def deploy_artifact(library_root: Path, project_dir: Path, artifact_path: Path) -> list:
    """
    Deploy the artifact file VERBATIM to each declared target (e.g. MASTER-PROMPT.md,
    loaded via CLAUDE.md). The self-describing 'ARTIFACT vNN' label is load-bearing
    and kept, so the deployed file is byte-identical to the latest artifact and always
    shows the current version. Returns a list of (target_rel, byte_count). Runs on
    every checkpoint (NO CHANGE included), so the deployed copy never drifts. No-op
    when no .deploy marker exists.
    """
    targets = deploy_targets(project_dir)
    if not targets:
        return []
    content = artifact_path.read_text(encoding="utf-8")
    written = []
    for rel in targets:
        (library_root / rel).write_text(content, encoding="utf-8")
        written.append((rel, len(content.encode("utf-8"))))
    return written


# ---------------------------------------------------------------------------
# Library root discovery
# ---------------------------------------------------------------------------

def find_library_root() -> Path:
    """Walk upward from CWD until MAP.md is found."""
    current = Path.cwd()
    for parent in [current, *current.parents]:
        if (parent / "MAP.md").exists():
            return parent
    print("Error: No library root found. Run from inside AI-Library.")
    sys.exit(1)


# ---------------------------------------------------------------------------
# Input parsing
# ---------------------------------------------------------------------------

def parse_blocks(text: str, expected_version: str) -> dict:
    """
    Extract the four labelled code blocks from checkpoint output.
    Tries tilde fence first, then four-backtick, then three-backtick.
    Returns dict mapping block name -> content string.
    Exits on missing block or version mismatch.
    """
    results = {}
    for name in BLOCKS:
        match = (
            BLOCK_PATTERNS_TILDE[name].search(text)
            or BLOCK_PATTERNS_4[name].search(text)
            or BLOCK_PATTERNS_3[name].search(text)
        )
        if not match:
            print(f"Error: Block not found in input file: {name} v{expected_version}")
            sys.exit(1)
        found_version = match.group(1)
        if found_version != expected_version:
            print(
                f"Error: Version mismatch in {name} block — "
                f"expected v{expected_version}, found v{found_version}."
            )
            sys.exit(1)
        content = match.group(2)
        # Strip leading separator lines (e.g. "-----------") between label and content
        lines = content.splitlines(keepends=True)
        while lines and re.fullmatch(r"-+\s*", lines[0]):
            lines.pop(0)
        results[name] = "".join(lines)
    return results


# ---------------------------------------------------------------------------
# Checkpoint run log
# ---------------------------------------------------------------------------

def write_checkpoint_log(library_root: Path, slug: str, version: str, warnings: list) -> None:
    """Append one line to logs/checkpoint-runs.log recording the run outcome."""
    log_path = library_root / "logs" / "checkpoint-runs.log"
    log_path.parent.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")
    if warnings:
        def short(w):
            m = re.match(r"^([A-Z][A-Z ]+[A-Z])\s", w)
            return m.group(1) if m else w[:30]
        summary = f"integrity: {len(warnings)} warning{'s' if len(warnings) != 1 else ''} — {'; '.join(short(w) for w in warnings)}"
    else:
        summary = "integrity: clean"
    with log_path.open("a", encoding="utf-8") as f:
        f.write(f"{timestamp} | {slug} | v{version} | {summary}\n")
    print(f"  Log: {log_path.relative_to(library_root)}")


def copy_and_relabel_artifact(
    library_root: Path, slug: str, version: str, prev_version: str, target: Path
) -> None:
    """
    Copy the previous artifact file and rewrite its label and separator lines
    to the new version. Used when the ARTIFACT block contains the NO CHANGE sentinel.
    """
    prev_path = find_artifact_path(library_root / "projects" / slug, prev_version)
    if prev_path is None:
        print(
            f"Error: NO CHANGE sentinel used but previous artifact not found: "
            f"v{prev_version}--artifact.* in {library_root / 'projects' / slug}"
        )
        sys.exit(1)
    lines = prev_path.read_text(encoding="utf-8").splitlines(keepends=True)
    new_label = f"ARTIFACT v{version}"
    lines[0] = new_label + "\n"
    if len(lines) > 1:
        lines[1] = "-" * len(new_label) + "\n"
    target.write_text("".join(lines), encoding="utf-8")


# ---------------------------------------------------------------------------
# Integrity validation
# ---------------------------------------------------------------------------

def extract_section_lines(content: str, section: str) -> set:
    """
    Extract bullet lines from a named section in a context file.
    Stops at the next all-caps section header.
    """
    lines = content.splitlines()
    in_section = False
    result = set()
    for line in lines:
        if line.strip() == f"{section}:":
            in_section = True
            continue
        if in_section:
            if re.match(r"^[A-Z][A-Z ]+:\s*$", line.strip()):
                break
            if line.startswith("- "):
                result.add(line.strip())
    return result


def validate_new_triplet(
    library_root: Path,
    slug: str,
    version: str,
    targets: dict,
    blocks: dict,
) -> list:
    """
    Validate the newly written triplet against the previous version.
    Returns a list of warning strings (empty = all clear).
    """
    warnings = []
    prev_version_int = int(version) - 1
    if prev_version_int < 1:
        return warnings  # No previous version to compare

    prev_version       = f"{prev_version_int:02d}"
    prev_artifact_path = find_artifact_path(library_root / "projects" / slug, prev_version)
    prev_context_path  = library_root / "projects" / slug / f"v{prev_version}--context.md"

    # Check 1: Label lines
    label_map = {
        "artifact":     f"ARTIFACT v{version}",
        "context":      f"CONTEXT v{version}",
        "instructions": f"INSTRUCTIONS v{version}",
    }
    for label, expected_label in label_map.items():
        first_line = targets[label].read_text(encoding="utf-8").splitlines()[0]
        if first_line != expected_label:
            warnings.append(
                f"LABEL MISMATCH  {targets[label].name}: "
                f"expected '{expected_label}', got '{first_line}'"
            )

    # Check 2: Separator lines
    for label, expected_label in label_map.items():
        file_lines = targets[label].read_text(encoding="utf-8").splitlines()
        if len(file_lines) < 2:
            warnings.append(f"MISSING SEPARATOR  {targets[label].name}: file too short")
            continue
        expected_sep = "-" * len(expected_label)
        if file_lines[1] != expected_sep:
            warnings.append(
                f"SEPARATOR MISMATCH  {targets[label].name}: "
                f"expected '{expected_sep}', got '{file_lines[1]}'"
            )

    # Check 3: STATE section present in context
    if "STATE:" not in blocks["CONTEXT"]:
        warnings.append(
            f"MISSING STATE  {targets['context'].name}: no STATE: section found"
        )

    # Check 4: DECISIONS and RULED OUT are superset of previous context
    if prev_context_path.exists():
        prev_text = prev_context_path.read_text(encoding="utf-8")
        new_text  = blocks["CONTEXT"]
        for section in APPEND_ONLY_SECTIONS:
            prev_lines = extract_section_lines(prev_text, section)
            new_lines  = extract_section_lines(new_text, section)
            dropped    = prev_lines - new_lines
            if dropped:
                warnings.append(
                    f"DROPPED LINES  {targets['context'].name} [{section}]: "
                    f"{len(dropped)} line(s) from v{prev_version} missing:"
                )
                for line in sorted(dropped):
                    warnings.append(f"    {line}")

    # Check 5: Artifact size not suspiciously smaller than previous
    if prev_artifact_path is not None:
        prev_size = prev_artifact_path.stat().st_size
        new_size  = targets["artifact"].stat().st_size
        if prev_size > 0 and (new_size / prev_size) < ARTIFACT_MIN_RATIO:
            warnings.append(
                f"SIZE WARNING  {targets['artifact'].name}: "
                f"{new_size} bytes vs previous {prev_size} bytes "
                f"({new_size/prev_size:.0%} of previous — possible truncation)"
            )

    # Check 6: Context size not suspiciously smaller than previous
    if prev_context_path.exists():
        prev_size = prev_context_path.stat().st_size
        new_size  = targets["context"].stat().st_size
        if prev_size > 0 and (new_size / prev_size) < CONTEXT_MIN_RATIO:
            warnings.append(
                f"SIZE WARNING  {targets['context'].name}: "
                f"{new_size} bytes vs previous {prev_size} bytes "
                f"({new_size/prev_size:.0%} of previous — possible decision loss)"
            )

    return warnings


# ---------------------------------------------------------------------------
# Summary extraction from THREAD ENTRY block
# ---------------------------------------------------------------------------

def extract_summaries(thread_entry: str):
    """Parse **Artifact:**, **Context:**, **Instructions:** fields for MAP.md."""
    def extract(pattern, fallback):
        m = pattern.search(thread_entry)
        return m.group(1).strip() if m else fallback

    return (
        extract(THREAD_ARTIFACT_RE,     "artifact"),
        extract(THREAD_CONTEXT_RE,      "context"),
        extract(THREAD_INSTRUCTIONS_RE, "instructions"),
    )


# ---------------------------------------------------------------------------
# MAP.md update
# ---------------------------------------------------------------------------

def build_map_entries(slug: str, version: str, summaries, artifact_ext: str):
    """Build the three MAP.md entry lines for the new triplet."""
    artifact_s, context_s, instructions_s = summaries
    vnn  = f"v{version}"
    base = f"projects/{slug}"
    artifact_name = f"{vnn}--artifact.{artifact_ext}"
    return [
        f"- [{artifact_name}]({base}/{artifact_name}) — {artifact_s}",
        f"- [{vnn}--context.md]({base}/{vnn}--context.md) — {context_s}",
        f"- [{vnn}--instructions.md]({base}/{vnn}--instructions.md) — {instructions_s}",
    ]


def insert_map_entries(map_path: Path, slug: str, new_entries):
    """
    Insert three new entries into the correct ## projects/<slug>/ section
    of MAP.md, after the last vNN line in that section.
    """
    section_header = f"## projects/{slug}/"
    lines = map_path.read_text(encoding="utf-8").splitlines()

    section_start = None
    for i, line in enumerate(lines):
        if line.strip() == section_header:
            section_start = i
            break

    if section_start is None:
        print(f"Error: Section '{section_header}' not found in MAP.md.")
        sys.exit(1)

    vnn_pattern    = re.compile(r"^\s*-\s*\[v\d{2}--")
    last_vnn_index = None
    for i in range(section_start + 1, len(lines)):
        if lines[i].startswith("## ") and i != section_start:
            break
        if vnn_pattern.match(lines[i]):
            last_vnn_index = i

    insert_at = (last_vnn_index + 1) if last_vnn_index is not None else (section_start + 1)
    updated   = lines[:insert_at] + new_entries + lines[insert_at:]
    return "\n".join(updated) + "\n"


# ---------------------------------------------------------------------------
# Git commit message
# ---------------------------------------------------------------------------

def git_commit_message(thread_entry: str, version: str) -> str:
    """Extract the first content line of the THREAD ENTRY for the commit message."""
    for line in thread_entry.splitlines():
        stripped = line.strip()
        if stripped and not stripped.startswith("###") and not re.fullmatch(r"-+", stripped):
            clean = re.sub(r"\*\*(.+?):\*\*\s*", "", stripped)
            return f"v{version}: {clean}"
    return f"v{version}: checkpoint"


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    # --- Argument parsing ---
    args = sys.argv[1:]
    write_mode = "--write" in args
    args = [a for a in args if a != "--write"]

    if len(args) not in (2, 3):
        print(__doc__)
        sys.exit(1)

    slug, version  = args[0], args[1]
    input_path_str = args[2] if len(args) == 3 else None

    if not re.fullmatch(r"\d{2}", version):
        print(f"Error: Version must be two digits (e.g. 09), got: {version}")
        sys.exit(1)

    vnn = f"v{version}"

    # --- Resolve paths ---
    library_root = find_library_root()
    project_dir  = library_root / "projects" / slug

    # Default input: temp/v[NN]-checkpoint.txt inside library root
    if input_path_str:
        input_file = Path(input_path_str).expanduser().resolve()
    else:
        input_file = library_root / "temp" / f"v{version}-checkpoint.txt"

    # --- Validate project and input ---
    if not project_dir.exists():
        print(f"Error: Project folder not found: {project_dir}")
        sys.exit(1)

    thread_path = project_dir / "THREAD.md"
    if not thread_path.exists():
        print(f"Error: THREAD.md not found in {project_dir}")
        sys.exit(1)

    map_path = library_root / "MAP.md"

    if not input_file.exists():
        print(f"Error: Input file not found: {input_file}")
        sys.exit(1)

    # --- Resolve artifact extension from the previous version on disk ---
    prev_version    = f"{max(int(version) - 1, 0):02d}"
    artifact_ext    = resolve_artifact_extension(project_dir, prev_version)

    # --- Check target files do not already exist ---
    targets = {
        "artifact":     project_dir / f"{vnn}--artifact.{artifact_ext}",
        "context":      project_dir / f"{vnn}--context.md",
        "instructions": project_dir / f"{vnn}--instructions.md",
    }
    for label, path in targets.items():
        if path.exists():
            print(f"Error: Target file already exists (no overwrite): {path}")
            sys.exit(1)

    # --- Parse input ---
    text   = input_file.read_text(encoding="utf-8")
    blocks = parse_blocks(text, version)

    # --- Sentinel: NO CHANGE artifact ---
    # When the ARTIFACT block body is "NO CHANGE", checkpoint.py copies the previous
    # artifact file and relabels it rather than writing from the block content.
    artifact_no_change = blocks["ARTIFACT"].strip() == "NO CHANGE"

    # --- Extract summaries and build MAP entries ---
    summaries   = extract_summaries(blocks["THREAD ENTRY"])
    map_entries = build_map_entries(slug, version, summaries, artifact_ext)

    # --- Compute sizes ---
    sizes = {label: len(content.encode("utf-8")) for label, content in [
        ("context",      blocks["CONTEXT"]),
        ("instructions", blocks["INSTRUCTIONS"]),
    ]}
    if not artifact_no_change:
        sizes["artifact"] = len(blocks["ARTIFACT"].encode("utf-8"))

    commit_msg = git_commit_message(blocks["THREAD ENTRY"], version)

    # --- Dry-run output ---
    if not write_mode:
        print(f"DRY RUN — pass --write to execute\nInput: {input_file}\n")
        print("WOULD WRITE:")
        if artifact_no_change:
            print(f"  {targets['artifact'].relative_to(library_root)}  (copy of v{prev_version}--artifact.{artifact_ext}, relabelled)")
        else:
            print(f"  {targets['artifact'].relative_to(library_root)}  ({sizes['artifact']} bytes)")
        print(f"  {targets['context'].relative_to(library_root)}  ({sizes['context']} bytes)")
        print(f"  {targets['instructions'].relative_to(library_root)}  ({sizes['instructions']} bytes)")
        print()
        print("WOULD APPEND TO:")
        print(f"  {thread_path.relative_to(library_root)}")
        print(f"  MAP.md  (section: ## projects/{slug}/)")
        print()
        print("MAP.md entries that would be added:")
        for entry in map_entries:
            print(f"  {entry}")
        print()
        deploy_t = deploy_targets(project_dir)
        if deploy_t:
            print("WOULD DEPLOY (artifact verbatim, ARTIFACT label kept):")
            for rel in deploy_t:
                print(f"  {rel}")
            print()
        print(f"Suggested commit message:")
        print(f"  {commit_msg}")
        return

    # --- Execute writes ---
    # Reconstruct label and separator consumed by parse_blocks().
    # Separator width matches label width by convention — consistent with all files on disk.
    artifact_label = f"ARTIFACT v{version}"
    ctx_label      = f"CONTEXT v{version}"
    inst_label     = f"INSTRUCTIONS v{version}"
    if artifact_no_change:
        copy_and_relabel_artifact(library_root, slug, version, prev_version, targets["artifact"])
    else:
        targets["artifact"].write_text(
            artifact_label + "\n" + "-" * len(artifact_label) + "\n" + blocks["ARTIFACT"],
            encoding="utf-8",
        )
    targets["context"].write_text(
        ctx_label + "\n" + "-" * len(ctx_label) + "\n" + blocks["CONTEXT"],
        encoding="utf-8",
    )
    targets["instructions"].write_text(
        inst_label + "\n" + "-" * len(inst_label) + "\n" + blocks["INSTRUCTIONS"],
        encoding="utf-8",
    )

    # Deploy the label-stripped artifact body to any declared targets (e.g.
    # MASTER-PROMPT.md, loaded verbatim via CLAUDE.md). Runs on every checkpoint,
    # NO CHANGE included, so the deployed copy can never lag the artifact.
    deployed = deploy_artifact(library_root, project_dir, targets["artifact"])

    # Append THREAD ENTRY
    existing  = thread_path.read_text(encoding="utf-8")
    separator = "\n" if existing.endswith("\n") else "\n\n"
    thread_path.write_text(
        existing + separator + f"THREAD ENTRY v{version}\n" + blocks["THREAD ENTRY"].rstrip() + "\n",
        encoding="utf-8",
    )

    # Update MAP.md
    updated_map = insert_map_entries(map_path, slug, map_entries)
    map_path.write_text(updated_map, encoding="utf-8")

    # --- Integrity validation ---
    integrity_warnings = validate_new_triplet(
        library_root, slug, version, targets, blocks
    )

    # --- Write checkpoint run log ---
    write_checkpoint_log(library_root, slug, version, integrity_warnings)

    # --- Write confirmation ---
    print("WRITTEN:")
    if artifact_no_change:
        print(f"  {targets['artifact'].relative_to(library_root)}  ({targets['artifact'].stat().st_size} bytes, copied from v{prev_version})")
    else:
        print(f"  {targets['artifact'].relative_to(library_root)}  ({sizes['artifact']} bytes)")
    print(f"  {targets['context'].relative_to(library_root)}  ({sizes['context']} bytes)")
    print(f"  {targets['instructions'].relative_to(library_root)}  ({sizes['instructions']} bytes)")
    for rel, nbytes in deployed:
        print(f"  DEPLOYED {rel}  ({nbytes} bytes, verbatim — ARTIFACT v{version} label kept)")
    print()
    print("APPENDED TO:")
    print(f"  {thread_path.relative_to(library_root)}")
    print(f"  MAP.md  (section: ## projects/{slug}/)")
    print()

    if integrity_warnings:
        print("INTEGRITY WARNINGS:")
        for w in integrity_warnings:
            print(f"  {w}")
        print()
    else:
        print("INTEGRITY  all checks passed")
        print()

    print("Run: git add .")
    print(f"Run: git commit -m \"{commit_msg}\"")


if __name__ == "__main__":
    main()
