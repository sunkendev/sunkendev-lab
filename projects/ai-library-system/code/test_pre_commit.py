#!/usr/bin/env python3
"""
test_pre_commit.py — unit tests for pre-commit.py.

Source:  projects/ai-library-system/code/test_pre_commit.py
Deploys: code/test_pre_commit.py (library root)

Run:  python3 code/test_pre_commit.py
      (or: python3 projects/ai-library-system/code/test_pre_commit.py)

Stdlib unittest only — no pytest, no external dependencies. Each test builds a
throwaway git repo in a tempdir and runs pre-commit.py against it as a subprocess,
exactly as the real hook does, so the checks are exercised end to end. Focus is
the regenerate-and-diff deploy guard (check_master_prompt_sync), with a couple of
adjacent checks for smoke coverage.
"""

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HOOK = Path(__file__).resolve().parent / "pre-commit.py"

ARTIFACT = "ARTIFACT v34\n------------\nYou are operating inside.\nBody line.\n"
BODY = "You are operating inside.\nBody line.\n"


def _git(repo, *args):
    return subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True)


def _run_hook(repo):
    """Run pre-commit.py with cwd=repo, exactly as the portable hook wrapper does."""
    return subprocess.run([sys.executable, str(HOOK)], cwd=str(repo),
                          capture_output=True, text=True)


def _init_repo(td, files, stage):
    """Create a git repo at td, write `files` (relpath -> content), stage `stage` paths."""
    repo = Path(td)
    _git(repo, "init", "-q")
    _git(repo, "config", "user.email", "t@t")
    _git(repo, "config", "user.name", "t")
    for rel, content in files.items():
        p = repo / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8")
    for rel in stage:
        _git(repo, "add", rel)
    return repo


def _base_files(master_prompt=ARTIFACT, extra=None):
    """A minimal but valid library: one project with a .deploy marker, a complete
    v34 triplet on disk, and a deployed MASTER-PROMPT.md. Deploy is verbatim, so an
    in-sync MASTER-PROMPT.md equals the artifact (ARTIFACT label included)."""
    files = {
        "MAP.md": ("# Map\n\n## projects/ai-library-system/\n\n"
                   "- [v34--artifact.md](projects/ai-library-system/v34--artifact.md) — x\n\n"
                   "## inbox/\n"),
        "projects/ai-library-system/.deploy": "MASTER-PROMPT.md\n",
        "projects/ai-library-system/v34--artifact.md": ARTIFACT,
        "projects/ai-library-system/v34--context.md":
            "CONTEXT v34\n-----------\nPROJECT: x\nDECISIONS:\nRULED OUT:\nOPEN:\nSTATE:\ns\n",
        "projects/ai-library-system/v34--instructions.md":
            "INSTRUCTIONS v34\n----------------\nPROJECT: x\nGOAL: g\nBACKGROUND: b\n"
            "ARTIFACT STATE: a\nKEY DECISIONS: k\nOPEN QUESTIONS: o\n"
            "EXPLICITLY RULED OUT: r\nNEXT TASK: n\nPERSONA: p\nSTYLE AND CONSTRAINTS: s\n",
        "MASTER-PROMPT.md": master_prompt,
    }
    if extra:
        files.update(extra)
    return files


ARTIFACT_REL = "projects/ai-library-system/v34--artifact.md"
# Under verbatim deploy the target must equal ARTIFACT exactly; the old label-stripped
# body is now an out-of-sync state, as is a wrong-version label.
STALE = BODY


class TestMasterPromptSyncGuard(unittest.TestCase):
    def test_in_sync_artifact_staged_passes(self):
        with tempfile.TemporaryDirectory() as td:
            repo = _init_repo(td, _base_files(), [ARTIFACT_REL])
            r = _run_hook(repo)
            self.assertNotIn("out of sync", r.stdout)
            self.assertEqual(r.returncode, 0, msg=r.stdout + r.stderr)

    def test_stale_target_blocks_when_artifact_staged(self):
        with tempfile.TemporaryDirectory() as td:
            repo = _init_repo(td, _base_files(master_prompt=STALE), [ARTIFACT_REL])
            r = _run_hook(repo)
            self.assertIn("out of sync", r.stdout)
            self.assertEqual(r.returncode, 1)

    def test_stale_target_blocks_when_target_staged(self):
        with tempfile.TemporaryDirectory() as td:
            repo = _init_repo(td, _base_files(master_prompt=STALE), ["MASTER-PROMPT.md"])
            r = _run_hook(repo)
            self.assertIn("out of sync", r.stdout)
            self.assertEqual(r.returncode, 1)

    def test_unrelated_commit_not_trapped_by_stale_target(self):
        with tempfile.TemporaryDirectory() as td:
            repo = _init_repo(td, _base_files(master_prompt=STALE,
                                              extra={"code/foo.py": "x = 1\n"}),
                              ["code/foo.py"])
            r = _run_hook(repo)
            self.assertNotIn("out of sync", r.stdout)
            self.assertEqual(r.returncode, 0, msg=r.stdout + r.stderr)

    def test_missing_target_reports_error(self):
        with tempfile.TemporaryDirectory() as td:
            files = _base_files()
            del files["MASTER-PROMPT.md"]
            repo = _init_repo(td, files, [ARTIFACT_REL])
            r = _run_hook(repo)
            self.assertIn("deploy target missing", r.stdout)
            self.assertEqual(r.returncode, 1)

    def test_project_without_marker_ignored(self):
        with tempfile.TemporaryDirectory() as td:
            files = _base_files(master_prompt=STALE)
            del files["projects/ai-library-system/.deploy"]
            repo = _init_repo(td, files, [ARTIFACT_REL])
            r = _run_hook(repo)
            self.assertNotIn("out of sync", r.stdout)


class TestAdjacentChecks(unittest.TestCase):
    def test_artifact_label_version_mismatch_blocks(self):
        with tempfile.TemporaryDirectory() as td:
            files = _base_files()
            files[ARTIFACT_REL] = "ARTIFACT v33\n------------\n" + BODY  # label != filename
            repo = _init_repo(td, files, [ARTIFACT_REL])
            r = _run_hook(repo)
            self.assertIn("does not match filename", r.stdout)
            self.assertEqual(r.returncode, 1)

    def test_bad_version_prefix_blocks(self):
        with tempfile.TemporaryDirectory() as td:
            files = _base_files()
            files["projects/ai-library-system/v3--artifact.md"] = "ARTIFACT v33\n------------\n" + BODY
            repo = _init_repo(td, files, ["projects/ai-library-system/v3--artifact.md"])
            r = _run_hook(repo)
            self.assertIn("two digits", r.stdout)
            self.assertEqual(r.returncode, 1)


if __name__ == "__main__":
    unittest.main()
