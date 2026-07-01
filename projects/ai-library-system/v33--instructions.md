INSTRUCTIONS v33
----------------
PROJECT: AI Document Library System
GOAL: Design, document, and iteratively refine a five-layer vendor-agnostic generational system for managing AI-generated work using plain text files and a prompt-controlled workflow.
BACKGROUND: This session, like v32, did no artifact-content work on MASTER-PROMPT.md itself. It closed out both gaps surfaced at the end of v32: the lack of automated test coverage for checkpoint.py, and the lack of test coverage and durable logging for the ai-library-ops skill's git-sync logic. Before building either, several scoping questions were resolved: the user declined a separate repo for tests/scripts, fixing instead a single-repo discipline (no CI, no dependency manifests, no tests/ sprawl, stdlib-only); the signal-lost rigor test's prose-voice "gap" was re-examined and reclassified as an artifact of thin test authoring, not a schema flaw, retiring the previously-floated style-anchor field; and a user-floated idea about using an observability/agent platform, or a raw interaction stream, as a future memory layer was discussed, critiqued, and explicitly paused for after the library is otherwise finished. test_checkpoint.py (25 tests) was then built, verified, and shipped. For the second item, the SKILL.md git-sync bash was extracted into git_sync.py, live-tested against four scenarios in throwaway repos (which caught and fixed a real bug — diverged main was being misclassified as a push failure rather than as diverged, though origin/main itself was never actually at risk), wired into SKILL.md v9, committed, and then used on itself for a real production sync. Building git_sync.py's own automated test file was deliberately deferred, per explicit user direction to treat the extraction and live verification as one complete step.
ARTIFACT STATE: MASTER-PROMPT.md v33 — NO CHANGE, relabelled from v32. No edits to MASTER-PROMPT.md this session; all work was on test_checkpoint.py, git_sync.py, ai-library-ops SKILL.md (now v9, three deployed copies kept in sync), .gitignore, and MAP.md.
KEY DECISIONS:
- No separate repo for ai-library-system's tests/scripts; single-repo, no-CI, no-dependency-manifest, stdlib-only discipline adopted as a binding constraint
- The signal-lost prose-voice gap is a test-authoring artifact, not a schema flaw; the style-anchor field idea is retired (moved from open candidate to ruled out)
- test_checkpoint.py built and shipped: 25 stdlib-unittest cases, committed at 73db0f2
- git_sync.py built, live-verified (4 scenarios, including a real bug fix for diverged-main misclassification), wired into SKILL.md v9, committed at fcf23ea, and already used in production for this checkpoint's own sync
- NOTE stays push-only (does not fast-forward main); reconfirmed via explicit pros/cons this session
- The observability-as-storage / streaming-interaction-as-memory idea is paused, not ruled out — revisit only if the user raises it again, and only after the library is otherwise finished
OPEN QUESTIONS:
- Whether and when to build test_git_sync.py, now that the script it would test is already in production use
- Whether logs/git-sync.log should eventually fold into logs/checkpoint-runs.log or stay separate
- Which other v32-era OPEN item to pick up next: related: bare-filename hook warning, MAP.md machine-readable block, MASTER-PROMPT.md artifact-type schema, DELTA design for checkpoint.py, iCloud/USB-C backup, pre-commit.py MASTER-PROMPT.md write protection, flow-vs-ai temp/ cleanup, Layer 4/5
EXPLICITLY RULED OUT:
- A separate repo for tests/scripts — single-repo discipline confirmed instead
- The style-anchor verbatim-excerpt field for context.md — retired as a test-authoring artifact, not a real schema gap
- Observability/agent platform as a memory-storage layer — wrong tool, vendor lock-in
- Logging bolted onto SKILL.md's bash prose without first extracting it into a script — reproduces the exact bug it would fix
- JSON Lines as the new log format — plain pipe-delimited text kept for consistency with logs/checkpoint-runs.log
- Folding NOTE into full CHECKPOINT/COMMIT-style main-sync — reconfirmed as ruled out via fresh pros/cons
- (Plus all prior ruled-out items — see v33--context.md)
NEXT TASK: Pick the next OPEN item, most plausibly test_git_sync.py (now that git_sync.py is in production with no regression coverage) or one of the longer-standing v32-era items, per user direction.
PERSONA: See persona.md
STYLE AND CONSTRAINTS: Plain language. Precise. No lists where prose works better. No suggestions that contradict the established philosophy. When proposing changes to master prompt or documents, show the specific change not a full rewrite. State plan before executing any write, script, or git operation.
