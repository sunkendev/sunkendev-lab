INSTRUCTIONS v08
----------------
PROJECT: AI Document Library System
GOAL: Design, document, and iteratively refine a five-layer vendor-agnostic generational system for managing AI-generated work using plain text files and a prompt-controlled workflow.
BACKGROUND: Layer 1 is fully operational with pre-commit validation. Layer 2 is designed, documented, and confirmed working via a live Claude Project experiment this session. A Claude Code five-layer evaluation was completed — key findings include: checkpoint.py design references eliminated schema elements (steps 10–11 must be revised before building), related: fields use bare filenames not relative paths, project triplet files need a lightweight metadata convention before Layer 4, and MAP.md needs a machine-readable block before Layer 5. The NOTE immediate-commit rule was added to MASTER-PROMPT.md after a regression where THREAD.md drifted uncommitted during active work.
ARTIFACT STATE: MASTER-PROMPT.md v08 — complete, operational, NOTE immediate-commit rule added. Approximately 80 lines. Reference documents: 2026-04-11--layer-1-foundation--claude.md, 2026-04-11--layer-2-session--claude.md, 2026-04-11--layer-1-5-eval--claude.md all written and committed.
KEY DECISIONS:
- NOTE immediate-commit rule added to MASTER-PROMPT.md — THREAD.md must be committed immediately after every NOTE
- Layer 2 confirmed working — Claude Project with MASTER-PROMPT.md and persona.md in system prompt, four-file RESUME still required
- Claude Code evaluation completed — findings captured in THREAD.md and eval report
- .claude/ added to .gitignore — Claude Code worktree excluded from git and libmap
- libmap alias updated to exclude .claude/ path
- checkpoint.py clipboard-default design ruled out — file path input is more robust
- checkpoint.py steps 10–11 ruled out as designed — reference eliminated schema elements
- code/ at library root confirmed as deployment target (not scripts/)
OPEN QUESTIONS:
- checkpoint.py revised design not yet written
- related: fields use bare filenames — pre-commit hook warning not yet added
- Lightweight metadata convention for project triplet files not yet defined
- MAP.md machine-readable block not yet added
- ARCHITECTURE.tex discrepancies not yet corrected
- Layer 4 embedding model and vector store not yet chosen
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
- checkpoint.py steps 10–11 as originally designed
NEXT TASK: Revise the checkpoint.py design. Remove steps 10–11 (THREAD.md header update and MAP.md Recent table — both reference eliminated schema elements). Define correct replacement behaviour: append THREAD ENTRY to THREAD.md, add three new MAP.md entries in the correct section. Define artifact extension handling — require it as a CLI argument. Define dry-run mode as default, --write to execute. Then build the script.
PERSONA: See persona.md
STYLE AND CONSTRAINTS: Plain language. Precise. No lists where prose works better. No suggestions that contradict the established philosophy. When proposing changes to master prompt or documents, show the specific change not a full rewrite.
