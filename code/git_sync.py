#!/usr/bin/env python3
"""
git_sync.py — AI Library git push + fast-forward-main automation.

Source:  projects/ai-library-system/code/git_sync.py
Deploys: code/git_sync.py (library root)

Usage:
  git_sync.py <project-slug> <operation-label> [--push-only]

  project-slug      folder name under projects/ (e.g. ai-library-system)
  operation-label   short label for the log line (e.g. CHECKPOINT, COMMIT, NOTE)
  --push-only       push the current branch only; skip fast-forwarding main
                     (used by the NOTE operation, which is lightweight by design)

Replaces the git push / fetch / checkout-main / merge --ff-only / push /
checkout-back sequence previously duplicated as bash across SKILL.md's
CHECKPOINT, COMMIT, and NOTE blocks. Never forces a merge — if main has
diverged, it reports that and leaves main untouched.
"""

import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


def find_library_root() -> Path:
    """Walk upward from CWD until MAP.md is found."""
    current = Path.cwd()
    for parent in [current, *current.parents]:
        if (parent / "MAP.md").exists():
            return parent
    print("Error: No library root found. Run from inside AI-Library.")
    sys.exit(1)


def run_git(args: list, cwd: Path) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True)


def get_current_branch(cwd: Path) -> str:
    result = run_git(["branch", "--show-current"], cwd)
    return result.stdout.strip()


def push_branch(branch: str, cwd: Path) -> bool:
    result = run_git(["push", "-u", "origin", branch], cwd)
    return result.returncode == 0


def fast_forward_main(branch: str, cwd: Path) -> str:
    """Attempt to fast-forward main to match branch. Returns 'clean-ff',
    'diverged', or 'push-failed'. Always leaves the repo back on branch."""
    run_git(["fetch", "origin", "main"], cwd)
    run_git(["checkout", "-B", "main", "origin/main"], cwd)
    merge = run_git(["merge", "--ff-only", branch], cwd)
    if merge.returncode != 0:
        run_git(["checkout", branch], cwd)
        return "diverged"
    push = run_git(["push", "origin", "main"], cwd)
    run_git(["checkout", branch], cwd)
    return "clean-ff" if push.returncode == 0 else "push-failed"


def sync(operation_label: str, push_only: bool, cwd: Path) -> dict:
    branch = get_current_branch(cwd)

    if not push_branch(branch, cwd):
        return {"branch": branch, "push": "failed", "ff_main": "skipped"}

    if push_only:
        return {"branch": branch, "push": "success", "ff_main": "skip-push-only"}

    if branch == "main":
        return {"branch": branch, "push": "success", "ff_main": "skip-already-main"}

    return {"branch": branch, "push": "success", "ff_main": fast_forward_main(branch, cwd)}


def log_result(library_root: Path, slug: str, operation_label: str, result: dict) -> None:
    """Append one line to logs/git-sync.log recording the run outcome."""
    log_path = library_root / "logs" / "git-sync.log"
    log_path.parent.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")
    line = (
        f"{timestamp} | {slug} | {operation_label} | "
        f"branch:{result['branch']} | push:{result['push']} | ff-main:{result['ff_main']}\n"
    )
    with log_path.open("a", encoding="utf-8") as f:
        f.write(line)
    print(f"  Log: {log_path.relative_to(library_root)}")


def main():
    args = sys.argv[1:]
    push_only = "--push-only" in args
    args = [a for a in args if a != "--push-only"]

    if len(args) != 2:
        print(__doc__)
        sys.exit(1)

    slug, operation_label = args
    library_root = find_library_root()

    result = sync(operation_label, push_only, library_root)
    log_result(library_root, slug, operation_label, result)

    print(f"  Branch: {result['branch']}")
    print(f"  Push: {result['push']}")
    print(f"  Fast-forward main: {result['ff_main']}")

    if result["push"] == "failed":
        print("Error: push failed.")
        sys.exit(1)
    if result["ff_main"] == "diverged":
        print("WARNING: main has diverged from this branch — cannot fast-forward. "
              "Surface to user before merging manually.")
        sys.exit(1)
    if result["ff_main"] == "push-failed":
        print("Error: main fast-forwarded locally but push to origin/main failed.")
        sys.exit(1)


if __name__ == "__main__":
    main()
