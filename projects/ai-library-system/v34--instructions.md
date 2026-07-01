INSTRUCTIONS v34
----------------
PROJECT: AI Document Library System
GOAL: Design, document, and iteratively refine a five-layer vendor-agnostic generational system for managing AI-generated work using plain text files and a prompt-controlled workflow.
BACKGROUND: This session was a short, focused continuation of v33's deferred plan: build test_git_sync.py, the one piece v33 explicitly chose not to do in the same step as the git_sync.py extraction. No new design questions came up. The test suite follows the leaner two-tier design discussed at the end of v33: pure decision logic (sync, push_branch, fast_forward_main's branching) is tested via a FakeGit harness that patches git_sync.run_git and keys fake responses on exact argv tuples, so the bulk of the suite runs with zero real git invocations; a small number of real-throwaway-repo tests are reserved specifically for the diverged-main classification bug found and fixed in v33, proving by direct execution (not just code reading) that origin/main is never touched when a real divergence is detected. The suite (17 tests) passes in both the source location (projects/ai-library-system/code/) and the deployed location (code/), confirmed byte-identical and confirmed runnable from each. It was committed, then MAP.md was updated to register it, and the commit was synced using git_sync.py itself — the new test suite's own first real-world exercise was syncing its own commit.
ARTIFACT STATE: MASTER-PROMPT.md v34 — NO CHANGE, relabelled from v33. No edits to MASTER-PROMPT.md this session; all work was on test_git_sync.py and MAP.md.
KEY DECISIONS:
- test_git_sync.py built and shipped: 17 stdlib-unittest cases, committed at 66c72a5
- Test design: FakeGit harness (patches git_sync.run_git, keyed on exact argv tuples) for all decision-logic branches; real-throwaway-repo tests reserved for the diverged-main regression case specifically
- No tests/ subdirectory or fixture/conftest machinery added — real-git test setup is inlined per-test in a tempdir, consistent with the binding repo-scope constraint
- MAP.md updated to register test_git_sync.py under both projects/ai-library-system/code/ and code/ sections
OPEN QUESTIONS:
- Whether logs/git-sync.log should eventually fold into logs/checkpoint-runs.log or stay separate
- Which v32-era OPEN item to pick up next: related: bare-filename hook warning, MAP.md machine-readable block, MASTER-PROMPT.md artifact-type schema, DELTA design for checkpoint.py, iCloud/USB-C backup, pre-commit.py MASTER-PROMPT.md write protection, flow-vs-ai temp/ cleanup, Layer 4/5
EXPLICITLY RULED OUT:
- Mocking subprocess.run directly — patching git_sync's own run_git() function instead, since it reads closer to the real call sites
- A tests/ subdirectory with fixtures/conftest for the real-git cases — inline tempdir setup per test, per the binding repo-scope constraint
- (Plus all prior ruled-out items — see v34--context.md)
NEXT TASK: Pick the next OPEN item — most plausibly one of the longer-standing v32-era items now that both test-coverage gaps from v32 are closed, per user direction.
PERSONA: See persona.md
STYLE AND CONSTRAINTS: Plain language. Precise. No lists where prose works better. No suggestions that contradict the established philosophy. When proposing changes to master prompt or documents, show the specific change not a full rewrite. State plan before executing any write, script, or git operation.
