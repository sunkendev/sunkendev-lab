INSTRUCTIONS v20
----------------
PROJECT: AI Document Library System
GOAL: Design, document, and iteratively refine a five-layer vendor-agnostic generational system for managing AI-generated work using plain text files and a prompt-controlled workflow.
BACKGROUND: The system is fully operational at Layers 1, 2, and 3. This session added a critical behaviour rule to MASTER-PROMPT.md and persona.md requiring the AI to state its plan before any write, script, or git operation and wait for confirmation. A context compression event from v18 was forensically analysed: compression hit at 82.5% of the context window (165,028 tokens), system prompt overhead is fixed at ~38,521 tokens, and the usage field is the only reliable detection source. Thresholds for a context detection skill have been established: Tier 1 at 130,000 input tokens, Tier 2 at 155,000. The forensics findings are documented at projects/ai-library-system/docs/2026-04-13--v18-compression-forensics--claude.md.
ARTIFACT STATE: MASTER-PROMPT.md v20 — behaviour rule added (state plan before executing). Approximately 92 lines.
KEY DECISIONS:
- Behaviour rule added to MASTER-PROMPT.md and persona.md: state plan and wait for confirmation before any write/script/git
- Context detection thresholds: Tier 1 130K tokens (warn), Tier 2 155K tokens (urgent + auto-generate checkpoint)
- Usage field is the only reliable detection source — not character counts, not output behaviour
- Context pressure events go in a separate operational log, not THREAD.md — log location TBD
- File-first checkpoint design validated: blocks on disk before dry-run saved v18 session
OPEN QUESTIONS:
- Context detection skill: CONTEXT CHECK command vs. woven into ai-library-ops operations
- Operational log location for context pressure events (temp/? logs/ folder? chat-only?)
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
NEXT TASK: Decide the operational log location for context pressure events (one question: temp/, new logs/ folder, or chat-only). Then build the context detection feature — read session transcript via session_info, check input token count against thresholds, implement as CONTEXT CHECK command or woven into ai-library-ops. After that: GitHub remote setup.
PERSONA: See persona.md
STYLE AND CONSTRAINTS: Plain language. Precise. No lists where prose works better. No suggestions that contradict the established philosophy. When proposing changes to master prompt or documents, show the specific change not a full rewrite. State plan before executing any write, script, or git operation.
