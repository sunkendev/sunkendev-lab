INSTRUCTIONS v18
----------------
PROJECT: AI Document Library System
GOAL: Design, document, and iteratively refine a five-layer vendor-agnostic generational system for managing AI-generated work using plain text files and a prompt-controlled workflow.
BACKGROUND: The system is fully operational at Layers 1, 2, and 3. Cowork is the Layer 2+3 orchestrator with the ai-library-ops skill automating all three library operations. The post-v17 session resolved all Cowork git reliability issues: hook drift eliminated via wrapper, lock cascade fixed via allow_cowork_file_delete, library discovery made CWD-independent, and the self-containment principle established (nothing writes outside the project folder). The updated skill is packaged in temp/ and needs reinstalling.
ARTIFACT STATE: MASTER-PROMPT.md v18 — unchanged from v16, version incremented for triplet sync. Approximately 90 lines.
KEY DECISIONS:
- Self-containment principle: no script writes outside ~/Claude/Projects/AI-Library/
- .git/hooks/pre-commit is a bash wrapper delegating to code/pre-commit.py — no drift
- allow_cowork_file_delete required before git ops in Cowork sandbox — one call per session
- Library root discovery: find /sessions -maxdepth 7 — CWD-independent
- Git identity in .git/config — persists across sessions
- write_snapshot removed from pre-commit.py — violated self-containment
- SKILL.md excluded from pre-commit frontmatter check
OPEN QUESTIONS:
- GitHub remote not yet set up
- iCloud passive rsync backup not yet in workflow
- USB-C 2TB SSD backup not yet configured
- ARCHITECTURE.tex discrepancies not yet corrected
- related: field path validation in pre-commit hook not yet added
- Lightweight metadata convention for project triplet files not yet defined
- MAP.md machine-readable block not yet added
- Layer 2 project instructions update has no automation path — manual paste required
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
NEXT TASK: Install the updated ai-library-ops.skill from temp/. Then set up GitHub remote for ~/Claude/Projects/AI-Library/ to complete WORM tier 1: create private repo, add as remote origin, push main, configure branch protection (no force-push, require PR for deletions).
PERSONA: See persona.md
STYLE AND CONSTRAINTS: Plain language. Precise. No lists where prose works better. No suggestions that contradict the established philosophy. When proposing changes to master prompt or documents, show the specific change not a full rewrite.
