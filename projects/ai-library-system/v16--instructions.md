INSTRUCTIONS v16
----------------
PROJECT: AI Document Library System
GOAL: Design, document, and iteratively refine a five-layer vendor-agnostic generational system for managing AI-generated work using plain text files and a prompt-controlled workflow.
BACKGROUND: The system is fully operational at Layer 3. This session pivoted to Cowork as the Layer 2+3 orchestrator, eliminating manual terminal operations. The iCloud library is frozen at v15 as a permanent baseline. The new library was forked to ~/Claude/Projects/AI-Library/ — local SSD, fresh git repo (commit 8e9ac4a), pre-commit hook installed. A Cowork project was created pointing to the new library with MASTER-PROMPT.md + persona.md as project instructions. The Cowork orchestration skill is the immediate next priority.
ARTIFACT STATE: MASTER-PROMPT.md v16 — unchanged from v15, version incremented for triplet sync. Approximately 90 lines.
KEY DECISIONS:
- iCloud library frozen at v15 as permanent baseline
- New library at ~/Claude/Projects/AI-Library/ — local SSD, independent git repo
- Fork is a new folder + new git repo, not a branch
- Cowork is the new Layer 2+3 orchestrator
- WORM strategy: local SSD primary, iCloud passive rsync, GitHub WORM, USB-C 2TB SSD tertiary
- Cowork project instructions = MASTER-PROMPT.md + persona.md
- git is folder-bound — two repos are fully independent
- macOS protected folders avoided as library home
OPEN QUESTIONS:
- ARCHITECTURE.tex discrepancies not yet corrected
- USER-GUIDE.tex not yet rewritten
- related: fields use bare filenames — pre-commit hook warning not yet added
- Lightweight metadata convention for project triplet files not yet defined
- MAP.md machine-readable block not yet added
- Cowork orchestration skill not yet built
- iCloud passive backup (rsync) not yet added to workflow
- GitHub remote not yet set up
- USB-C 2TB SSD backup not yet configured
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
- Blocking integrity validation — warn only
- MASTER-PROMPT.md in SHA-256 manifest
- ~/Documents/ as library location — macOS privacy restrictions
- Folder names with spaces — hyphen convention used throughout
- Git branch as fork mechanism
- iCloud Drive as git working directory
NEXT TASK: Open a new conversation in the Cowork AI-Library project. Paste the four RESUME files. Build the Cowork orchestration skill — a skill that runs checkpoint.py, git add/commit, and add_note_thread.py from within a Cowork session, eliminating all manual terminal operations.
PERSONA: See persona.md
STYLE AND CONSTRAINTS: Plain language. Precise. No lists where prose works better. No suggestions that contradict the established philosophy. When proposing changes to master prompt or documents, show the specific change not a full rewrite.
