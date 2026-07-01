INSTRUCTIONS v17
----------------
PROJECT: AI Document Library System
GOAL: Design, document, and iteratively refine a five-layer vendor-agnostic generational system for managing AI-generated work using plain text files and a prompt-controlled workflow.
BACKGROUND: The system is fully operational at Layers 1, 2, and 3. Cowork is now the designated Layer 2+3 orchestrator with the ai-library-ops skill handling all three library operations (CHECKPOINT, NOTE, COMMIT) without manual terminal work. The library lives at ~/Claude/Projects/AI-Library/ on local SSD with an independent git repo. The iCloud library is frozen at v15 as a permanent baseline. The WORM storage strategy is defined but only the local SSD tier is active — GitHub remote and iCloud rsync remain to be set up.
ARTIFACT STATE: MASTER-PROMPT.md v17 — unchanged from v16, version incremented for triplet sync. Approximately 90 lines.
KEY DECISIONS:
- iCloud library frozen at v15 as permanent baseline
- New library at ~/Claude/Projects/AI-Library/ — local SSD, independent git repo
- Fork is a new folder + new git repo, not a branch
- Cowork is the Layer 2+3 orchestrator
- WORM strategy: local SSD primary, iCloud passive rsync, GitHub WORM, USB-C 2TB SSD tertiary
- Cowork project instructions = MASTER-PROMPT.md + persona.md
- git is folder-bound — two repos are fully independent
- macOS protected folders avoided as library home
- ai-library-ops skill installed — three operations automated: CHECKPOINT, NOTE, COMMIT
- Skill source at projects/ai-library-system/code/ai-library-ops/SKILL.md
- Library root discovery: Path('.').rglob('MAP.md') + cd into result
OPEN QUESTIONS:
- ARCHITECTURE.tex discrepancies not yet corrected
- USER-GUIDE.tex not yet rewritten
- related: fields use bare filenames — pre-commit hook warning not yet added
- Lightweight metadata convention for project triplet files not yet defined
- MAP.md machine-readable block not yet added
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
- Manual terminal operations in Cowork sessions — ai-library-ops skill handles all three
NEXT TASK: Set up GitHub remote for the ~/Claude/Projects/AI-Library/ repo to complete the first durable tier of the WORM strategy. Create a new private GitHub repository, add as remote origin, push main branch, then configure branch protection to enforce WORM (no force-push, require PR for deletions). Capture all decisions in the next checkpoint or NOTE.
PERSONA: See persona.md
STYLE AND CONSTRAINTS: Plain language. Precise. No lists where prose works better. No suggestions that contradict the established philosophy. When proposing changes to master prompt or documents, show the specific change not a full rewrite.
