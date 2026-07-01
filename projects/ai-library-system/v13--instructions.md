INSTRUCTIONS v13
----------------
PROJECT: AI Document Library System
GOAL: Design, document, and iteratively refine a five-layer vendor-agnostic generational system for managing AI-generated work using plain text files and a prompt-controlled workflow.
BACKGROUND: Layer 3 is fully operational and verified through the v12 live test. The checkpoint workflow now produces a single downloadable file. This session adds one standing step to the save instructions: when the artifact is MASTER-PROMPT.md, the Layer 2 workspace system prompt must also be updated. This closes a recurring drift risk identified after v08 and v11.
ARTIFACT STATE: MASTER-PROMPT.md v13 — one change from v12: step 3 of save instructions expanded to include Layer 2 system prompt update. Approximately 90 lines.
KEY DECISIONS:
- Layer 2 workspace system prompt update is mandatory when artifact is MASTER-PROMPT.md
- Step added to post-checkpoint save instructions in MASTER-PROMPT.md
OPEN QUESTIONS:
- ARCHITECTURE.tex discrepancies not yet corrected
- USER-GUIDE.tex not yet rewritten
- related: fields use bare filenames — pre-commit hook warning not yet added
- Lightweight metadata convention for project triplet files not yet defined
- MAP.md machine-readable block not yet added
- checkpoint.py extension handling if non-.md artifact ever needed
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
- Saving checkpoint input file inside library folder
- Printing CHECKPOINT FILE block in chat — replaced by downloadable file
- Artifact label line ruling reversed — no longer ruled out; all three file types are self-describing
NEXT TASK: Run checkpoint.py against this file. Then update the Layer 2 workspace system prompt with MASTER-PROMPT.md v13 contents.
PERSONA: See persona.md
STYLE AND CONSTRAINTS: Plain language. Precise. No lists where prose works better. No suggestions that contradict the established philosophy. When proposing changes to master prompt or documents, show the specific change not a full rewrite.
