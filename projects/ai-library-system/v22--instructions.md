INSTRUCTIONS v22
----------------
PROJECT: AI Document Library System
GOAL: Design, document, and iteratively refine a five-layer vendor-agnostic generational system for managing AI-generated work using plain text files and a prompt-controlled workflow.
BACKGROUND: The system is fully operational at Layers 1, 2, and 3. This session made three post-v21 fixes: (1) NEW PROJECT gap closed — skill v5 writes v00--context.md and v00--instructions.md stubs so RESUME works on fresh projects before any checkpoint exists; (2) skill source deployed to code/ai-library-ops/ at library root so it ships with the library independently of the projects/ folder; (3) pre-commit false positive fixed — MAP.md display text must be bare filename with no slashes, as the integrity check regex extracts all slash-containing strings including display text.
ARTIFACT STATE: MASTER-PROMPT.md v22 — unchanged from v21. Approximately 93 lines.
KEY DECISIONS:
- ai-library-ops skill v5: NEW PROJECT writes v00 stubs — RESUME works on any project from day one
- v00 stubs are minimal but schema-conformant; superseded by v01 after first real checkpoint
- Skill source at code/ai-library-ops/SKILL.md — ships with library, independent of projects/
- MAP.md display text convention: bare filename only, no slashes
OPEN QUESTIONS:
- legal-research has no v00 stubs — needs backfill (created before v5)
- GitHub remote not yet set up
- iCloud passive rsync backup not yet in workflow
- ARCHITECTURE.tex discrepancies not yet corrected
- related: field path validation in pre-commit hook not yet added
- Lightweight metadata convention for project triplet files not yet defined
- MAP.md machine-readable block not yet added
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
- Remote git for now
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
NEXT TASK: Backfill v00 stubs for legal-research (write v00--context.md and v00--instructions.md to projects/legal-research/). Then GitHub remote setup.
PERSONA: See persona.md
STYLE AND CONSTRAINTS: Plain language. Precise. No lists where prose works better. No suggestions that contradict the established philosophy. When proposing changes to master prompt or documents, show the specific change not a full rewrite. State plan before executing any write, script, or git operation.
