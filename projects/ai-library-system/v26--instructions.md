INSTRUCTIONS v26
----------------
PROJECT: AI Document Library System
GOAL: Design, document, and iteratively refine a five-layer vendor-agnostic generational system for managing AI-generated work using plain text files and a prompt-controlled workflow.
BACKGROUND: This session added checkpoint run logging. write_checkpoint_log() was added to checkpoint.py — it appends one line to logs/checkpoint-runs.log after every --write run, recording the timestamp, slug, version, and integrity outcome. The key insight: integrity warnings are the only non-redundant output of checkpoint.py; all other terminal output is already captured in git. The .gitignore was updated to selectively include logs/checkpoint-runs.log (tracked in git as a permanent audit record) while keeping context-pressure.log and session.log excluded as runtime telemetry. Same selective-include pattern as manifests.
ARTIFACT STATE: MASTER-PROMPT.md v26 — unchanged from v25. Approximately 111 lines.
KEY DECISIONS:
- write_checkpoint_log() appends one line to logs/checkpoint-runs.log after every --write run
- Log entry format: YYYY-MM-DDTHH:MMZ | slug | vNN | integrity: clean OR integrity: N warnings — TYPE1; TYPE2
- Integrity warnings are the only non-redundant checkpoint.py output worth logging
- .gitignore: logs/* + !logs/checkpoint-runs.log — checkpoint-runs.log in git; telemetry logs excluded
OPEN QUESTIONS:
- temp/ cleanup in flow-vs-ai: move kurgan-rostok-review.html to projects/flow-vs-ai/docs/; clarify .skill package disposition
- pre-commit.py MASTER-PROMPT.md write protection — optional, deferred; env var pattern agreed
- GitHub remote not yet set up
- iCloud passive rsync backup not yet in workflow
- ARCHITECTURE.tex discrepancies not yet corrected
- related: field path validation in pre-commit hook not yet added
- Lightweight metadata convention for project triplet files not yet defined
- MAP.md machine-readable block not yet added
- DELTA design for checkpoint.py — backward-compatible Python-side append-only merge; not yet implemented
EXPLICITLY RULED OUT:
- Any proprietary file format
- Any platform as source of truth
- Specific cloud storage recommendations
- Layers 2-5 before Layer 1 is stable
- research/ and creative/ as top-level folders
- PHILOSOPHY section in context files
- META sections in THREAD.md and MAP.md
- Optional sections in any schema
- Newest-first ordering in THREAD.md
- Resuming from instructions file alone
- Blocking on MAP.md missing entry — warn only
- Blocking on section header checks — warn only
- Pre-commit hook checking itself
- Warn-only for triplet or version mismatch — hard blocks
- API tier for Layers 1 and 2
- Updating ARCHITECTURE.tex and USER-GUIDE.tex before scripted live
- Cloud-native platforms for personal library use
- scripts/ as folder name — code/ throughout
- Clipboard as default input for checkpoint.py
- checkpoint.py artifact extension as CLI argument
- checkpoint.py executing git commands
- Cloud-native execution of checkpoint.py at this stage
- Four-backtick outer fence for ARTIFACT block
- Saving checkpoint input file outside library folder
- Printing CHECKPOINT FILE block in chat
- Manual THREAD.md editing for NOTE entries
- Blocking integrity validation — warn only
- MASTER-PROMPT.md in SHA-256 manifest
- ~/Documents/ as library location
- Folder names with spaces
- Git branch as fork mechanism
- iCloud Drive as git working directory
- Manual terminal operations in Cowork sessions
- Writing to paths outside ~/Claude/Projects/AI-Library/
- Path('.').rglob() for library discovery in skill context
- ### Heading / Path: / Summary: block format for MAP.md entries
- Character count heuristics on JSONL for threshold detection
- Output behaviour signals as sole compression detection
- Context pressure events in THREAD.md
- Manual CONTEXT CHECK as primary detection — automatic per-operation status is more reliable
- Context pressure log in temp/ — too ephemeral
- session_info for self-monitoring of current session
- Slash-containing display text in MAP.md bullet entries
- Out-of-band fixes to library files without explicit user approval — kernel rule, no exceptions
- Management interface as a separate project construct — not needed at this stage
- Developer mode / user mode distinction for shipped library — unnecessary complexity
- --no-verify as escape hatch for MASTER-PROMPT.md write protection — env var pattern preferred
NEXT TASK: (1) Clean up temp/ misuse in flow-vs-ai — move kurgan-rostok-review.html to projects/flow-vs-ai/docs/ with correct naming and frontmatter; clarify whether .skill packages should be deleted or retained. (2) GitHub remote setup for open source publication.
PERSONA: See persona.md
STYLE AND CONSTRAINTS: Plain language. Precise. No lists where prose works better. No suggestions that contradict the established philosophy. When proposing changes to master prompt or documents, show the specific change not a full rewrite. State plan before executing any write, script, or git operation.
