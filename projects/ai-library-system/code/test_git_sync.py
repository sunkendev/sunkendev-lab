#!/usr/bin/env python3
"""
test_git_sync.py — unit tests for git_sync.py.

Source:  projects/ai-library-system/code/test_git_sync.py
Deploys: code/test_git_sync.py (library root)

Run:  python3 code/test_git_sync.py
      (or: python3 projects/ai-library-system/code/test_git_sync.py)

Stdlib unittest only — no pytest, no external dependencies.

Most tests run against a FakeGit stand-in for subprocess git calls, so
decision logic (sync's branching, fast_forward_main's classification) is
covered without touching a real repository. A small number of tests at
the bottom run real git against throwaway repos built in a tempdir — kept
to the cases that matter most: the diverged-main classification this
script exists to get right, which is exactly where a real bug was found
and fixed (checkout main -> checkout -B main origin/main).
"""

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import git_sync as gs


# ---------------------------------------------------------------------------
# FakeGit — stand-in for subprocess git calls, keyed by exact argv tuple
# ---------------------------------------------------------------------------

class FakeGit:
    """Replaces git_sync.run_git. Returns rc=0 for any call unless an
    override is given for that exact args tuple. Records every call."""

    def __init__(self, overrides=None, branch="feature"):
        self.overrides = overrides or {}
        self.branch = branch
        self.calls = []

    def __call__(self, args, cwd):
        self.calls.append(tuple(args))
        if args == ["branch", "--show-current"]:
            return subprocess.CompletedProcess(args, 0, stdout=self.branch + "\n", stderr="")
        rc = self.overrides.get(tuple(args), 0)
        return subprocess.CompletedProcess(args, rc, stdout="", stderr="")


class FakeGitTestCase(unittest.TestCase):
    """Base class that patches gs.run_git with a FakeGit and restores it."""

    def make_fake(self, overrides=None, branch="feature"):
        fake = FakeGit(overrides, branch)
        self._original_run_git = gs.run_git
        gs.run_git = fake
        self.addCleanup(self._restore)
        return fake

    def _restore(self):
        gs.run_git = self._original_run_git


# ---------------------------------------------------------------------------
# get_current_branch / push_branch
# ---------------------------------------------------------------------------

class TestGetCurrentBranch(FakeGitTestCase):
    def test_strips_trailing_newline(self):
        self.make_fake(branch="claude/resume-wkc9dz")
        self.assertEqual(gs.get_current_branch(Path(".")), "claude/resume-wkc9dz")


class TestPushBranch(FakeGitTestCase):
    def test_success(self):
        self.make_fake(branch="feature")
        self.assertTrue(gs.push_branch("feature", Path(".")))

    def test_failure(self):
        self.make_fake(overrides={("push", "-u", "origin", "feature"): 1})
        self.assertFalse(gs.push_branch("feature", Path(".")))


# ---------------------------------------------------------------------------
# fast_forward_main — decision logic via FakeGit
# ---------------------------------------------------------------------------

class TestFastForwardMainLogic(FakeGitTestCase):
    def test_clean_ff(self):
        self.make_fake(branch="feature")
        self.assertEqual(gs.fast_forward_main("feature", Path(".")), "clean-ff")

    def test_diverged_when_merge_fails(self):
        fake = self.make_fake(overrides={("merge", "--ff-only", "feature"): 1})
        self.assertEqual(gs.fast_forward_main("feature", Path(".")), "diverged")
        # Must never attempt to push main when the merge itself failed.
        self.assertNotIn(("push", "origin", "main"), fake.calls)
        # Must always land back on the original branch.
        self.assertEqual(fake.calls[-1], ("checkout", "feature"))

    def test_push_failed_when_merge_succeeds_but_push_rejected(self):
        fake = self.make_fake(overrides={("push", "origin", "main"): 1})
        self.assertEqual(gs.fast_forward_main("feature", Path(".")), "push-failed")
        self.assertEqual(fake.calls[-1], ("checkout", "feature"))

    def test_resets_local_main_to_origin_before_merging(self):
        # Regression test for the bug found during live testing: using
        # "checkout main" instead of "checkout -B main origin/main" let a
        # stale local main absorb the merge instead of the fetched ref.
        fake = self.make_fake(branch="feature")
        gs.fast_forward_main("feature", Path("."))
        self.assertIn(("checkout", "-B", "main", "origin/main"), fake.calls)
        self.assertNotIn(("checkout", "main"), fake.calls)


# ---------------------------------------------------------------------------
# sync — orchestration logic via FakeGit
# ---------------------------------------------------------------------------

class TestSync(FakeGitTestCase):
    def test_push_failure_skips_fast_forward_entirely(self):
        fake = self.make_fake(
            branch="feature",
            overrides={("push", "-u", "origin", "feature"): 1},
        )
        result = gs.sync("COMMIT", False, Path("."))
        self.assertEqual(result, {"branch": "feature", "push": "failed", "ff_main": "skipped"})
        self.assertNotIn(("fetch", "origin", "main"), fake.calls)

    def test_push_only_skips_fast_forward(self):
        fake = self.make_fake(branch="feature")
        result = gs.sync("NOTE", True, Path("."))
        self.assertEqual(result, {"branch": "feature", "push": "success", "ff_main": "skip-push-only"})
        self.assertNotIn(("fetch", "origin", "main"), fake.calls)

    def test_already_on_main_skips_fast_forward(self):
        self.make_fake(branch="main")
        result = gs.sync("CHECKPOINT", False, Path("."))
        self.assertEqual(result, {"branch": "main", "push": "success", "ff_main": "skip-already-main"})

    def test_feature_branch_runs_full_fast_forward(self):
        self.make_fake(branch="feature")
        result = gs.sync("CHECKPOINT", False, Path("."))
        self.assertEqual(result, {"branch": "feature", "push": "success", "ff_main": "clean-ff"})

    def test_feature_branch_reports_diverged(self):
        self.make_fake(
            branch="feature",
            overrides={("merge", "--ff-only", "feature"): 1},
        )
        result = gs.sync("CHECKPOINT", False, Path("."))
        self.assertEqual(result["ff_main"], "diverged")


# ---------------------------------------------------------------------------
# log_result
# ---------------------------------------------------------------------------

class TestLogResult(unittest.TestCase):
    def test_appends_one_line_with_expected_fields(self):
        with tempfile.TemporaryDirectory() as td:
            library_root = Path(td)
            result = {"branch": "feature", "push": "success", "ff_main": "clean-ff"}
            gs.log_result(library_root, "ai-library-system", "CHECKPOINT", result)
            line = (library_root / "logs" / "git-sync.log").read_text()
            self.assertIn("ai-library-system", line)
            self.assertIn("CHECKPOINT", line)
            self.assertIn("branch:feature", line)
            self.assertIn("push:success", line)
            self.assertIn("ff-main:clean-ff", line)

    def test_appends_without_truncating_previous_runs(self):
        with tempfile.TemporaryDirectory() as td:
            library_root = Path(td)
            result = {"branch": "feature", "push": "success", "ff_main": "clean-ff"}
            gs.log_result(library_root, "proj", "COMMIT", result)
            gs.log_result(library_root, "proj", "NOTE", result)
            lines = (library_root / "logs" / "git-sync.log").read_text().splitlines()
            self.assertEqual(len(lines), 2)


# ---------------------------------------------------------------------------
# main — argument handling (no git involved; exits before sync() runs)
# ---------------------------------------------------------------------------

class TestMainArgParsing(unittest.TestCase):
    def test_wrong_arg_count_exits(self):
        original_argv = sys.argv
        sys.argv = ["git_sync.py", "only-one-arg"]
        try:
            with self.assertRaises(SystemExit):
                gs.main()
        finally:
            sys.argv = original_argv


# ---------------------------------------------------------------------------
# Real-git regression tests — the diverged-main classification
# ---------------------------------------------------------------------------

def _run(args, cwd):
    subprocess.run(["git", *args], cwd=cwd, check=True, capture_output=True, text=True)


def _make_repo_pair(root: Path):
    """Bare 'origin' plus a clone ('work') with an initial commit on main
    and a 'feature' branch checked out, one commit ahead of main."""
    origin = root / "origin.git"
    work = root / "work"
    _run(["init", "--bare", str(origin)], root)
    _run(["symbolic-ref", "HEAD", "refs/heads/main"], origin)
    _run(["clone", str(origin), str(work)], root)
    _run(["config", "user.email", "test@example.com"], work)
    _run(["config", "user.name", "Test"], work)
    (work / "file.txt").write_text("initial\n")
    _run(["add", "file.txt"], work)
    _run(["commit", "-m", "initial"], work)
    _run(["push", "origin", "main"], work)
    _run(["checkout", "-b", "feature"], work)
    (work / "file.txt").write_text("feature change\n")
    _run(["commit", "-am", "feature work"], work)
    return origin, work


class TestFastForwardMainRealGit(unittest.TestCase):
    def test_clean_fast_forward(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            origin, work = _make_repo_pair(root)
            outcome = gs.fast_forward_main("feature", work)
            self.assertEqual(outcome, "clean-ff")
            self.assertEqual(gs.get_current_branch(work), "feature")
            log = subprocess.run(["git", "log", "--oneline", "main"], cwd=origin,
                                  capture_output=True, text=True, check=True)
            self.assertIn("feature work", log.stdout)

    def test_diverged_main_is_detected_and_origin_is_untouched(self):
        # Regression test: a second clone pushes a commit straight to main
        # so that origin/main no longer descends from the commit "feature"
        # branched off. fast_forward_main must report "diverged" and must
        # not touch origin's main.
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            origin, work = _make_repo_pair(root)

            other = root / "other"
            _run(["clone", str(origin), str(other)], root)
            _run(["config", "user.email", "test@example.com"], other)
            _run(["config", "user.name", "Test"], other)
            (other / "file.txt").write_text("diverged main change\n")
            _run(["commit", "-am", "diverged main commit"], other)
            _run(["push", "origin", "main"], other)

            origin_main_before = subprocess.run(
                ["git", "rev-parse", "main"], cwd=origin, capture_output=True, text=True, check=True
            ).stdout.strip()

            outcome = gs.fast_forward_main("feature", work)

            self.assertEqual(outcome, "diverged")
            self.assertEqual(gs.get_current_branch(work), "feature")
            origin_main_after = subprocess.run(
                ["git", "rev-parse", "main"], cwd=origin, capture_output=True, text=True, check=True
            ).stdout.strip()
            self.assertEqual(origin_main_before, origin_main_after)


if __name__ == "__main__":
    unittest.main()
