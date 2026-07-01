#!/usr/bin/env python3
"""
add_note_thread.py — Append a NOTE to a project THREAD.md and commit immediately.

Source:  projects/ai-library-system/code/add_note_thread.py
Deploys: code/add_note_thread.py (library root)

Usage:
  add_note_thread.py <project-slug> <topic> [--write]

  project-slug   folder name under projects/ (e.g. ai-library-system)
  topic          one-line topic description (quote if it contains spaces)
  --write        execute write and commit; omit for dry-run (default)

The script reads the note body from stdin. End input with Ctrl-D (macOS/Linux).

Example:
  echo "Body text here." | python3 code/add_note_thread.py ai-library-system "My topic" --write

  Or interactively:
  python3 code/add_note_thread.py ai-library-system "My topic" --write
  [type body, then Ctrl-D]
"""

import sys
import re
import subprocess
from datetime import date
from pathlib import Path


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
# NOTE formatting
# ---------------------------------------------------------------------------

def format_note(topic: str, body: str) -> str:
    """Format a NOTE block per the THREAD.md schema."""
    today = date.today().strftime("%Y-%m-%d")
    separator = "-" * 15  # matches convention in existing THREAD.md notes
    return f"\nNOTE {today}\n{separator}\n**Topic:** {topic}\n{body.rstrip()}\n"


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    # --- Argument parsing ---
    args = sys.argv[1:]
    write_mode = "--write" in args
    args = [a for a in args if a != "--write"]

    if len(args) != 2:
        print(__doc__)
        sys.exit(1)

    slug, topic = args[0], args[1]

    # --- Resolve paths ---
    library_root = find_library_root()
    project_dir  = library_root / "projects" / slug

    if not project_dir.exists():
        print(f"Error: Project folder not found: {project_dir}")
        sys.exit(1)

    thread_path = project_dir / "THREAD.md"
    if not thread_path.exists():
        print(f"Error: THREAD.md not found in {project_dir}")
        sys.exit(1)

    # --- Read body from stdin ---
    if sys.stdin.isatty():
        print("Enter note body (Ctrl-D when done):")
    body = sys.stdin.read().strip()

    if not body:
        print("Error: Note body is empty.")
        sys.exit(1)

    note = format_note(topic, body)

    # --- Dry-run output ---
    if not write_mode:
        print("DRY RUN — pass --write to execute\n")
        print(f"WOULD APPEND TO: {thread_path.relative_to(library_root)}\n")
        print("NOTE CONTENT:")
        print(note)
        print(f"WOULD COMMIT: {thread_path.relative_to(library_root)}")
        return

    # --- Execute ---
    existing = thread_path.read_text(encoding="utf-8")
    thread_path.write_text(existing + note, encoding="utf-8")
    print(f"Appended NOTE to {thread_path.relative_to(library_root)}")

    # Clear stale lock files before git operations — a failed prior run may
    # have left these behind. Safe to remove: if a real git process held them,
    # it would have cleaned up before exiting.
    for lock in ["index.lock", "HEAD.lock"]:
        lock_path = library_root / ".git" / lock
        try:
            lock_path.unlink()
            print(f"Removed stale {lock}")
        except FileNotFoundError:
            pass

    # Commit immediately — mandatory per THREAD.md immediate-commit rule
    result = subprocess.run(
        ["git", "add", str(thread_path)],
        cwd=library_root,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"Error staging THREAD.md: {result.stderr}")
        sys.exit(1)

    commit_msg = f"note: {topic}"
    result = subprocess.run(
        ["git", "commit", "-m", commit_msg],
        cwd=library_root,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"Error committing: {result.stderr}")
        sys.exit(1)

    print(f"Committed: {commit_msg}")


if __name__ == "__main__":
    main()
