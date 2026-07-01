INSTRUCTIONS v14
----------------
PROJECT: AI Document Library System
GOAL: Design, document, and iteratively refine a five-layer vendor-agnostic generational system for managing AI-generated work using plain text files and a prompt-controlled workflow.
BACKGROUND: Layer 3 is fully operational. This session added temp/ as the canonical location for checkpoint input files (excluded from git), made checkpoint.py input-file argument optional with temp/ as default, built add_note_thread.py to automate NOTE appending and immediate commit, and updated MASTER-PROMPT.md to reflect all three changes. The tilde fence collision bug was identified, repaired, and documented. The workflow is now significantly more automated.
ARTIFACT STATE: MASTER-PROMPT.md v14 — temp/ added to structure diagram; NOTE instructions updated to reference add_note_thread.py; save instructions updated to reflect temp/ as checkpoint file location. Approximately 90 lines.
KEY DECISIONS:
- temp/ at library root is canonical location for checkpoint input files
- temp/ excluded from git (.gitignore) and pre-commit hook (EXCLUDED set)
- checkpoint.py input-file argument optional — defaults to temp/v[NN]-checkpoint.txt
- add_note_thread.py automates NOTE appending and immediate THREAD.md commit
- MASTER-PROMPT.md must never contain a line starting with ~~~ — tilde fence collision
- Library structure diagram updated to show temp/
OPEN QUESTIONS:
- ARCHITECTURE.tex discrepancies not yet corrected
- USER-GUIDE.tex not yet rewritten
- related: fields use bare filenames — pre-commit hook warning not yet added
- Lightweight metadata convention for project triplet files not yet defined
- MAP.md machine-readable block not yet added
- Claude Code execution layer not yet implemented
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
- Artifact label line ruled out — reversed, all three file types are self-describing
- Manual THREAD.md editing for NOTE entries
NEXT TASK: Run checkpoint.py against this file (it will read from temp/v14-checkpoint.txt automatically). Then copy v14--artifact.md to MASTER-PROMPT.md and update Layer 2 workspace system prompt.
PERSONA: See persona.md
STYLE AND CONSTRAINTS: Plain language. Precise. No lists where prose works better. No suggestions that contradict the established philosophy. When proposing changes to master prompt or documents, show the specific change not a full rewrite.
