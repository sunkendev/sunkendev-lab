INSTRUCTIONS v19
----------------
PROJECT: AI Document Library System
GOAL: Design, document, and iteratively refine a five-layer vendor-agnostic generational system for managing AI-generated work using plain text files and a prompt-controlled workflow.
BACKGROUND: The system is fully operational at Layers 1, 2, and 3. The ai-library-ops skill now handles all five library operations: CHECKPOINT, NOTE, COMMIT, RESUME, and NEW PROJECT. RESUME loads project files from disk with no copy-paste. NEW PROJECT runs a three-question guided persona flow and creates the full project structure. Both operations were built, tested end-to-end with a legal-research test project, and committed. A MAP.md entry format bug found during the live test was fixed immediately. The skill v3 source is committed; the packaged skill in temp/ needs reinstalling to pick up the MAP.md fix.
ARTIFACT STATE: MASTER-PROMPT.md v19 — unchanged from v18, version incremented for triplet sync. Approximately 90 lines.
KEY DECISIONS:
- ai-library-ops skill v3: RESUME reads four files from disk, no copy-paste required
- NEW PROJECT: three questions one at a time, each with guidance and format-example options; no files written until persona confirmed
- MAP.md project entry format: ## projects/[slug]/ section with bullet items before ## inbox/
- legal-research test project committed — both new operations verified
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
- ### Heading / Path: / Summary: block format for MAP.md entries
NEXT TASK: Install ai-library-ops v3 from temp/ai-library-ops.skill in Cowork settings (replaces v2 — picks up MAP.md format fix). Then set up GitHub remote for ~/Claude/Projects/AI-Library/: create private repo, add as remote origin, push main, configure branch protection (no force-push, require PR for deletions).
PERSONA: See persona.md
STYLE AND CONSTRAINTS: Plain language. Precise. No lists where prose works better. No suggestions that contradict the established philosophy. When proposing changes to master prompt or documents, show the specific change not a full rewrite.
