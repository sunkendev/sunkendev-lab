#!/usr/bin/env python3
"""
test_checkpoint.py — unit tests for checkpoint.py.

Source:  projects/ai-library-system/code/test_checkpoint.py
Deploys: code/test_checkpoint.py (library root)

Run:  python3 code/test_checkpoint.py
      (or: python3 projects/ai-library-system/code/test_checkpoint.py)

Stdlib unittest only — no pytest, no external dependencies.
"""

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import checkpoint as cp


# ---------------------------------------------------------------------------
# resolve_artifact_extension / find_artifact_path
# ---------------------------------------------------------------------------

class TestResolveArtifactExtension(unittest.TestCase):
    def test_inherits_tex_extension_from_previous_version(self):
        # Regression test for the v31 bug: extension was hardcoded to .md,
        # which silently mis-saved any non-Markdown artifact.
        with tempfile.TemporaryDirectory() as td:
            project_dir = Path(td)
            (project_dir / "v01--artifact.tex").write_text("ARTIFACT v01\n")
            self.assertEqual(cp.resolve_artifact_extension(project_dir, "01"), "tex")

    def test_inherits_md_extension(self):
        with tempfile.TemporaryDirectory() as td:
            project_dir = Path(td)
            (project_dir / "v01--artifact.md").write_text("ARTIFACT v01\n")
            self.assertEqual(cp.resolve_artifact_extension(project_dir, "01"), "md")

    def test_defaults_to_md_when_no_previous_version(self):
        with tempfile.TemporaryDirectory() as td:
            project_dir = Path(td)
            self.assertEqual(cp.resolve_artifact_extension(project_dir, "00"), "md")

    def test_find_artifact_path_returns_none_when_missing(self):
        with tempfile.TemporaryDirectory() as td:
            project_dir = Path(td)
            self.assertIsNone(cp.find_artifact_path(project_dir, "01"))


# ---------------------------------------------------------------------------
# parse_blocks
# ---------------------------------------------------------------------------

TILDE_CHECKPOINT = """\
~~~
ARTIFACT v02
------------
Artifact body text.
~~~
~~~
CONTEXT v02
-----------
PROJECT: Test
DECISIONS:
- one
RULED OUT:
OPEN:
STATE:
Some state.
~~~
~~~
INSTRUCTIONS v02
-----------------
PROJECT: Test
GOAL: test
~~~
~~~
THREAD ENTRY v02
-----------------
### v02 — 2026-01-01
**Artifact:** Did a thing.
**Context:** Knows a thing.
**Instructions:** Unchanged.
~~~
"""


class TestParseBlocks(unittest.TestCase):
    def test_parses_tilde_fenced_blocks(self):
        blocks = cp.parse_blocks(TILDE_CHECKPOINT, "02")
        self.assertEqual(blocks["ARTIFACT"].strip(), "Artifact body text.")
        self.assertIn("PROJECT: Test", blocks["CONTEXT"])
        self.assertIn("GOAL: test", blocks["INSTRUCTIONS"])
        self.assertIn("### v02", blocks["THREAD ENTRY"])

    def test_parses_four_backtick_fenced_blocks(self):
        text = TILDE_CHECKPOINT.replace("~~~", "````")
        blocks = cp.parse_blocks(text, "02")
        self.assertEqual(blocks["ARTIFACT"].strip(), "Artifact body text.")

    def test_parses_three_backtick_fenced_blocks(self):
        text = TILDE_CHECKPOINT.replace("~~~", "```")
        blocks = cp.parse_blocks(text, "02")
        self.assertEqual(blocks["ARTIFACT"].strip(), "Artifact body text.")

    def test_strips_separator_line_after_label(self):
        blocks = cp.parse_blocks(TILDE_CHECKPOINT, "02")
        self.assertFalse(blocks["ARTIFACT"].startswith("-"))

    def test_missing_block_exits(self):
        text = TILDE_CHECKPOINT.replace("THREAD ENTRY v02", "NOT A BLOCK v02")
        with self.assertRaises(SystemExit):
            cp.parse_blocks(text, "02")

    def test_version_mismatch_exits(self):
        with self.assertRaises(SystemExit):
            cp.parse_blocks(TILDE_CHECKPOINT, "03")


# ---------------------------------------------------------------------------
# validate_new_triplet
# ---------------------------------------------------------------------------

class TestValidateNewTriplet(unittest.TestCase):
    def _make_project(self, td, prev_decisions="- one\n", prev_state="Old state.\n"):
        project_dir = Path(td)
        prev_artifact_body = "ARTIFACT v01\n------------\nPrevious artifact body text here.\n"
        (project_dir / "v01--artifact.md").write_text(prev_artifact_body)
        prev_context_body = (
            "CONTEXT v01\n-----------\nPROJECT: Test\nDECISIONS:\n"
            f"{prev_decisions}RULED OUT:\nOPEN:\nSTATE:\n{prev_state}"
        )
        (project_dir / "v01--context.md").write_text(prev_context_body)
        return project_dir

    def _write_targets(self, project_dir, artifact_body, context_body,
                        artifact_label="ARTIFACT v02", context_label="CONTEXT v02"):
        targets = {
            "artifact": project_dir / "v02--artifact.md",
            "context": project_dir / "v02--context.md",
            "instructions": project_dir / "v02--instructions.md",
        }
        targets["artifact"].write_text(
            artifact_label + "\n" + "-" * len(artifact_label) + "\n" + artifact_body
        )
        targets["context"].write_text(
            context_label + "\n" + "-" * len(context_label) + "\n" + context_body
        )
        inst_label = "INSTRUCTIONS v02"
        targets["instructions"].write_text(inst_label + "\n" + "-" * len(inst_label) + "\nGOAL: test\n")
        return targets

    def test_clean_run_no_warnings(self):
        with tempfile.TemporaryDirectory() as td:
            library_root = Path(td)
            proj_root = library_root / "projects" / "proj"
            proj_root.mkdir(parents=True)
            self._make_project(proj_root)
            artifact_body = "Plenty of new artifact content, similar length to before.\n"
            context_body = "PROJECT: Test\nDECISIONS:\n- one\n- two\nRULED OUT:\nOPEN:\nSTATE:\nNew state line here.\n"
            targets = self._write_targets(proj_root, artifact_body, context_body)
            blocks = {"CONTEXT": context_body}
            warnings = cp.validate_new_triplet(library_root, "proj", "02", targets, blocks)
            self.assertEqual(warnings, [])

    def test_label_mismatch_detected(self):
        with tempfile.TemporaryDirectory() as td:
            library_root = Path(td)
            proj_root = library_root / "projects" / "proj"
            proj_root.mkdir(parents=True)
            self._make_project(proj_root)
            context_body = "PROJECT: Test\nDECISIONS:\n- one\nRULED OUT:\nOPEN:\nSTATE:\nNew state.\n"
            targets = self._write_targets(proj_root, "New artifact body.\n", context_body,
                                            artifact_label="ARTIFACT v99")
            blocks = {"CONTEXT": context_body}
            warnings = cp.validate_new_triplet(library_root, "proj", "02", targets, blocks)
            self.assertTrue(any("LABEL MISMATCH" in w for w in warnings))

    def test_missing_state_section_detected(self):
        with tempfile.TemporaryDirectory() as td:
            library_root = Path(td)
            proj_root = library_root / "projects" / "proj"
            proj_root.mkdir(parents=True)
            self._make_project(proj_root)
            context_body = "PROJECT: Test\nDECISIONS:\n- one\nRULED OUT:\nOPEN:\n"
            targets = self._write_targets(proj_root, "New artifact body.\n", context_body)
            blocks = {"CONTEXT": context_body}
            warnings = cp.validate_new_triplet(library_root, "proj", "02", targets, blocks)
            self.assertTrue(any("MISSING STATE" in w for w in warnings))

    def test_dropped_decisions_line_detected(self):
        with tempfile.TemporaryDirectory() as td:
            library_root = Path(td)
            proj_root = library_root / "projects" / "proj"
            proj_root.mkdir(parents=True)
            self._make_project(proj_root, prev_decisions="- one\n- two\n")
            # New context drops "- two" — violates append-only rule.
            context_body = "PROJECT: Test\nDECISIONS:\n- one\nRULED OUT:\nOPEN:\nSTATE:\nNew state.\n"
            targets = self._write_targets(proj_root, "New artifact body.\n", context_body)
            blocks = {"CONTEXT": context_body}
            warnings = cp.validate_new_triplet(library_root, "proj", "02", targets, blocks)
            self.assertTrue(any("DROPPED LINES" in w for w in warnings))

    def test_artifact_size_warning_triggers_below_threshold(self):
        with tempfile.TemporaryDirectory() as td:
            library_root = Path(td)
            proj_root = library_root / "projects" / "proj"
            proj_root.mkdir(parents=True)
            # Previous artifact body is 100 bytes of 'x'.
            prev_artifact_body = "ARTIFACT v01\n------------\n" + ("x" * 100) + "\n"
            (proj_root / "v01--artifact.md").write_text(prev_artifact_body)
            (proj_root / "v01--context.md").write_text(
                "CONTEXT v01\n-----------\nPROJECT: Test\nDECISIONS:\nRULED OUT:\nOPEN:\nSTATE:\nOld.\n"
            )
            context_body = "PROJECT: Test\nDECISIONS:\nRULED OUT:\nOPEN:\nSTATE:\nNew.\n"
            # New artifact body is only 50 bytes — well under the 80% ratio.
            new_artifact_body = "y" * 50 + "\n"
            targets = self._write_targets(proj_root, new_artifact_body, context_body)
            blocks = {"CONTEXT": context_body}
            warnings = cp.validate_new_triplet(library_root, "proj", "02", targets, blocks)
            self.assertTrue(any("SIZE WARNING" in w and "artifact" in w for w in warnings))

    def test_v01_skips_comparison_entirely(self):
        with tempfile.TemporaryDirectory() as td:
            library_root = Path(td)
            proj_root = library_root / "projects" / "proj"
            proj_root.mkdir(parents=True)
            context_body = "PROJECT: Test\nDECISIONS:\nRULED OUT:\nOPEN:\nSTATE:\nFirst.\n"
            targets = self._write_targets(proj_root, "First artifact.\n", context_body,
                                            artifact_label="ARTIFACT v01", context_label="CONTEXT v01")
            blocks = {"CONTEXT": context_body}
            warnings = cp.validate_new_triplet(library_root, "proj", "01", targets, blocks)
            self.assertEqual(warnings, [])


# ---------------------------------------------------------------------------
# deploy_artifact (verbatim — the ARTIFACT vNN label is kept)
# ---------------------------------------------------------------------------

class TestDeploy(unittest.TestCase):
    def test_deploy_no_marker_is_noop(self):
        with tempfile.TemporaryDirectory() as td:
            library_root = Path(td)
            proj = library_root / "projects" / "proj"
            proj.mkdir(parents=True)
            artifact = proj / "v01--artifact.md"
            artifact.write_text("ARTIFACT v01\n------------\nBody.\n")
            self.assertEqual(cp.deploy_artifact(library_root, proj, artifact), [])
            self.assertFalse((library_root / "MASTER-PROMPT.md").exists())

    def test_deploy_writes_artifact_verbatim_to_target(self):
        with tempfile.TemporaryDirectory() as td:
            library_root = Path(td)
            proj = library_root / "projects" / "proj"
            proj.mkdir(parents=True)
            (proj / ".deploy").write_text("MASTER-PROMPT.md\n")
            artifact = proj / "v01--artifact.md"
            content = "ARTIFACT v01\n------------\nPrompt body line.\n"
            artifact.write_text(content)
            written = cp.deploy_artifact(library_root, proj, artifact)
            self.assertEqual(written, [("MASTER-PROMPT.md", len(content.encode()))])
            deployed = (library_root / "MASTER-PROMPT.md").read_text()
            # Verbatim: byte-identical to the artifact, label included.
            self.assertEqual(deployed, content)
            self.assertTrue(deployed.startswith("ARTIFACT v01"))


# ---------------------------------------------------------------------------
# copy_and_relabel_artifact
# ---------------------------------------------------------------------------

class TestCopyAndRelabelArtifact(unittest.TestCase):
    def test_no_change_sentinel_copies_and_relabels(self):
        with tempfile.TemporaryDirectory() as td:
            library_root = Path(td)
            proj_root = library_root / "projects" / "proj"
            proj_root.mkdir(parents=True)
            (proj_root / "v01--artifact.tex").write_text(
                "ARTIFACT v01\n------------\n\\documentclass{article}\nBody.\n"
            )
            target = proj_root / "v02--artifact.tex"
            cp.copy_and_relabel_artifact(library_root, "proj", "02", "01", target)
            content = target.read_text()
            self.assertTrue(content.startswith("ARTIFACT v02\n------------\n"))
            self.assertIn("\\documentclass{article}", content)
            self.assertIn("Body.", content)

    def test_missing_previous_artifact_exits(self):
        with tempfile.TemporaryDirectory() as td:
            library_root = Path(td)
            proj_root = library_root / "projects" / "proj"
            proj_root.mkdir(parents=True)
            target = proj_root / "v02--artifact.md"
            with self.assertRaises(SystemExit):
                cp.copy_and_relabel_artifact(library_root, "proj", "02", "01", target)


# ---------------------------------------------------------------------------
# build_map_entries / insert_map_entries
# ---------------------------------------------------------------------------

class TestMapEntries(unittest.TestCase):
    def test_build_map_entries_uses_correct_extension(self):
        entries = cp.build_map_entries("proj", "02", ("did x", "knows y", "changed z"), "tex")
        self.assertIn("v02--artifact.tex", entries[0])
        self.assertIn("did x", entries[0])

    def test_insert_map_entries_inserts_in_correct_section(self):
        with tempfile.TemporaryDirectory() as td:
            map_path = Path(td) / "MAP.md"
            map_path.write_text(
                "# Map\n\n"
                "## projects/other/\n\n"
                "- [v01--artifact.md](projects/other/v01--artifact.md) — other\n\n"
                "## projects/proj/\n\n"
                "- [v01--artifact.md](projects/proj/v01--artifact.md) — first\n\n"
                "## inbox/\n"
            )
            new_entries = ["- [v02--artifact.md](projects/proj/v02--artifact.md) — second"]
            updated = cp.insert_map_entries(map_path, "proj", new_entries)
            lines = updated.splitlines()
            proj_idx = lines.index("## projects/proj/")
            inbox_idx = lines.index("## inbox/")
            new_idx = next(i for i, l in enumerate(lines) if "second" in l)
            self.assertTrue(proj_idx < new_idx < inbox_idx)

    def test_insert_map_entries_missing_section_exits(self):
        with tempfile.TemporaryDirectory() as td:
            map_path = Path(td) / "MAP.md"
            map_path.write_text("# Map\n\n## projects/other/\n\n- entry\n")
            with self.assertRaises(SystemExit):
                cp.insert_map_entries(map_path, "nonexistent", ["- new"])


# ---------------------------------------------------------------------------
# git_commit_message
# ---------------------------------------------------------------------------

class TestGitCommitMessage(unittest.TestCase):
    def test_extracts_first_content_line(self):
        thread_entry = (
            "### v02 — 2026-01-01\n"
            "**Triggered by:** user request\n"
            "**Artifact:** Did the thing.\n"
        )
        msg = cp.git_commit_message(thread_entry, "02")
        self.assertEqual(msg, "v02: user request")

    def test_strips_bold_label_markdown(self):
        # Only the **Label:** field-marker prefix is stripped, not bold text elsewhere.
        thread_entry = "### v02 — 2026-01-01\n**Triggered by:** plain text reason\n"
        msg = cp.git_commit_message(thread_entry, "02")
        self.assertEqual(msg, "v02: plain text reason")

    def test_fallback_when_no_content_line(self):
        thread_entry = "### v02 — 2026-01-01\n---\n"
        msg = cp.git_commit_message(thread_entry, "02")
        self.assertEqual(msg, "v02: checkpoint")


# ---------------------------------------------------------------------------
# End-to-end: run the script for real against a throwaway project
# ---------------------------------------------------------------------------

class TestEndToEnd(unittest.TestCase):
    def test_write_mode_produces_expected_files(self):
        checkpoint_script = Path(cp.__file__).resolve()
        with tempfile.TemporaryDirectory() as td:
            library_root = Path(td)
            (library_root / "MAP.md").write_text(
                "# Map\n\n## projects/proj/\n\n"
                "- [v01--artifact.tex](projects/proj/v01--artifact.tex) — first\n\n"
                "## inbox/\n"
            )
            proj_root = library_root / "projects" / "proj"
            proj_root.mkdir(parents=True)
            (proj_root / "THREAD.md").write_text("# Thread: Test\n\n## Checkpoint log\n")
            (proj_root / "v01--artifact.tex").write_text(
                "ARTIFACT v01\n------------\n\\documentclass{article}\nFirst body.\n"
            )
            (proj_root / "v01--context.md").write_text(
                "CONTEXT v01\n-----------\nPROJECT: Test\nDECISIONS:\n- one\n"
                "RULED OUT:\nOPEN:\nSTATE:\nFirst state.\n"
            )

            input_file = library_root / "temp" / "v02-checkpoint.txt"
            input_file.parent.mkdir(parents=True)
            input_file.write_text(
                "~~~\nARTIFACT v02\n------------\n\\documentclass{article}\n"
                "Second body, plenty of content here to avoid size warnings on a short test fixture.\n~~~\n"
                "~~~\nCONTEXT v02\n-----------\nPROJECT: Test\nDECISIONS:\n- one\n- two\n"
                "RULED OUT:\nOPEN:\nSTATE:\nSecond state, slightly longer than before to avoid the "
                "context size-ratio warning on this short synthetic fixture file.\n~~~\n"
                "~~~\nINSTRUCTIONS v02\n-----------------\nGOAL: test\n~~~\n"
                "~~~\nTHREAD ENTRY v02\n-----------------\n### v02 — 2026-01-01\n"
                "**Artifact:** Second body written.\n**Context:** Knows second state.\n"
                "**Instructions:** Unchanged.\n~~~\n"
            )

            result = subprocess.run(
                [sys.executable, str(checkpoint_script), "proj", "02", str(input_file), "--write"],
                cwd=library_root, capture_output=True, text=True,
            )
            self.assertEqual(result.returncode, 0, msg=result.stdout + result.stderr)
            self.assertTrue((proj_root / "v02--artifact.tex").exists())
            self.assertTrue((proj_root / "v02--context.md").exists())
            self.assertTrue((proj_root / "v02--instructions.md").exists())
            self.assertIn("Second body written.", (proj_root / "THREAD.md").read_text())
            self.assertIn("v02--artifact.tex", (library_root / "MAP.md").read_text())
            self.assertIn("INTEGRITY  all checks passed", result.stdout)

    def test_write_mode_deploys_master_prompt_verbatim_on_no_change(self):
        # The NO CHANGE path is exactly the case that previously froze the deployed
        # MASTER-PROMPT.md at a stale version. Deploy must run and write verbatim.
        checkpoint_script = Path(cp.__file__).resolve()
        with tempfile.TemporaryDirectory() as td:
            library_root = Path(td)
            (library_root / "MAP.md").write_text(
                "# Map\n\n## projects/proj/\n\n"
                "- [v01--artifact.md](projects/proj/v01--artifact.md) — first\n\n"
                "## inbox/\n"
            )
            proj_root = library_root / "projects" / "proj"
            proj_root.mkdir(parents=True)
            (proj_root / ".deploy").write_text("MASTER-PROMPT.md\n")
            (proj_root / "THREAD.md").write_text("# Thread: Test\n\n## Checkpoint log\n")
            (proj_root / "v01--artifact.md").write_text(
                "ARTIFACT v01\n------------\nYou are operating inside a library. v1 body.\n"
            )
            (proj_root / "v01--context.md").write_text(
                "CONTEXT v01\n-----------\nPROJECT: Test\nDECISIONS:\n- one\n"
                "RULED OUT:\nOPEN:\nSTATE:\nFirst state.\n"
            )

            input_file = library_root / "temp" / "v02-checkpoint.txt"
            input_file.parent.mkdir(parents=True)
            input_file.write_text(
                "~~~\nARTIFACT v02\n------------\nNO CHANGE\n~~~\n"
                "~~~\nCONTEXT v02\n-----------\nPROJECT: Test\nDECISIONS:\n- one\n- two\n"
                "RULED OUT:\nOPEN:\nSTATE:\nSecond state, longer to clear the size-ratio "
                "warning on this short synthetic fixture file.\n~~~\n"
                "~~~\nINSTRUCTIONS v02\n-----------------\nGOAL: test\n~~~\n"
                "~~~\nTHREAD ENTRY v02\n-----------------\n### v02 — 2026-01-01\n"
                "**Artifact:** No change.\n**Context:** Knows state.\n**Instructions:** Unchanged.\n~~~\n"
            )

            result = subprocess.run(
                [sys.executable, str(checkpoint_script), "proj", "02", str(input_file), "--write"],
                cwd=library_root, capture_output=True, text=True,
            )
            self.assertEqual(result.returncode, 0, msg=result.stdout + result.stderr)
            deployed = (library_root / "MASTER-PROMPT.md").read_text()
            # Verbatim copy of the v02 artifact, relabelled by the NO CHANGE sentinel.
            self.assertEqual(
                deployed,
                "ARTIFACT v02\n------------\nYou are operating inside a library. v1 body.\n",
            )
            self.assertTrue(deployed.startswith("ARTIFACT v02"))
            self.assertIn("DEPLOYED MASTER-PROMPT.md", result.stdout)


if __name__ == "__main__":
    unittest.main()
