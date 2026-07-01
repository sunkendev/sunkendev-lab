INSTRUCTIONS v21
----------------
PROJECT: AI Document Library System
GOAL: Design, document, and iteratively refine a five-layer vendor-agnostic generational system for managing AI-generated work using plain text files and a prompt-controlled workflow.
BACKGROUND: The system is fully operational at Layers 1, 2, and 3. This session completed the context detection feature: the ai-library-ops skill v4 now outputs a one-line context status at the start of every operation, estimates token load from fixed overhead (~57K) plus per-call weights, and logs Tier 1 (>=130K) and Tier 2 (>=155K) events to logs/context-pressure.log. The log folder is excluded from git — operational telemetry only. MASTER-PROMPT.md v21 adds logs/ to the library structure diagram.
ARTIFACT STATE: MASTER-PROMPT.md v21 — logs/ added to library structure diagram. Approximately 93 lines.
KEY DECISIONS:
- logs/ folder at library root for context pressure events — excluded from git
- logs/context-pressure.log: append-only plaintext, Tier 1/Tier 2 events only
- ai-library-ops skill v4: automatic context status at every operation start
- Estimate model: fixed ~57K + per-call weights (exchange ~300, bash ~200, file read ~1K, web search/fetch ~1.5K, write/edit ~500)
- Automatic status is primary detection; CONTEXT CHECK is fallback only
- Tier 1 at 130K tokens (warn), Tier 2 at 155K tokens (urgent)
OPEN QUESTIONS:
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
NEXT TASK: GitHub remote setup. Create a remote repository (GitHub recommended per WORM strategy) and configure git remote origin. Push main branch. Then configure branch protection for WORM compliance.
PERSONA: See persona.md
STYLE AND CONSTRAINTS: Plain language. Precise. No lists where prose works better. No suggestions that contradict the established philosophy. When proposing changes to master prompt or documents, show the specific change not a full rewrite. State plan before executing any write, script, or git operation.
