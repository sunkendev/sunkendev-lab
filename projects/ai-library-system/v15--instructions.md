INSTRUCTIONS v15
----------------
PROJECT: AI Document Library System
GOAL: Design, document, and iteratively refine a five-layer vendor-agnostic generational system for managing AI-generated work using plain text files and a prompt-controlled workflow.
BACKGROUND: Layer 3 is fully operational with integrity validation now built into checkpoint.py. This session added SHA-256 manifest generation covering six files (triplet, THREAD.md, MAP.md, persona.md), DECISIONS/RULED OUT superset checking, size ratio truncation detection, and label/separator validation — all running automatically after every --write. The v14 context was repaired after a library consistency audit revealed dropped decisions and missing label lines. This checkpoint is the first live test of the full integrity validation stack.
ARTIFACT STATE: MASTER-PROMPT.md v15 — unchanged from v14, version incremented for triplet sync. Approximately 90 lines.
KEY DECISIONS:
- checkpoint.py integrity validation runs after every --write — warns, does not block
- SHA-256 manifest written to temp/v[NN]-[slug]-manifest.json covering six files
- DECISIONS and RULED OUT drop detection: new context must be superset of previous
- Artifact size >= 80% of previous; context size >= 90% of previous
- MASTER-PROMPT.md excluded from manifest — legitimate hash change at every MASTER-PROMPT checkpoint
- v14 context repaired — all dropped decisions from v10 onwards restored
- Library consistency audit pattern established via Claude Code
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
- Blocking integrity validation — warn only
- MASTER-PROMPT.md in SHA-256 manifest
NEXT TASK: Run checkpoint.py against this file — first live test of integrity validation. Verify INTEGRITY output shows all checks passed. Then copy v15--artifact.md to MASTER-PROMPT.md and update Layer 2 workspace system prompt.
PERSONA: See persona.md
STYLE AND CONSTRAINTS: Plain language. Precise. No lists where prose works better. No suggestions that contradict the established philosophy. When proposing changes to master prompt or documents, show the specific change not a full rewrite.
