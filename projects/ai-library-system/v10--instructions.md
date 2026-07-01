INSTRUCTIONS v10
----------------
PROJECT: AI Document Library System
GOAL: Design, document, and iteratively refine a five-layer vendor-agnostic generational system for managing AI-generated work using plain text files and a prompt-controlled workflow.
BACKGROUND: Layers 1, 2, and 3 are fully operational. Three improvements were made since v09: tilde fence replaces four-backtick for ARTIFACT outer fence, CHECKPOINT FILE block added as step 5 of the checkpoint ritual, and a version guard added requiring THREAD.md to be present before checkpoint proceeds. The first live test of checkpoint.py failed because the input file was missing fence delimiters — this is now understood and resolved by using the CHECKPOINT FILE block directly.
ARTIFACT STATE: MASTER-PROMPT.md v10 — CHECKPOINT FILE block and version guard added. Complete and operational. Approximately 90 lines.
KEY DECISIONS:
- CHECKPOINT FILE block added as step 5 — all four blocks with fences, ready for checkpoint.py input
- checkpoint.py input file must be saved outside the library folder
- Version guard added — THREAD.md must be present before checkpoint version is determined
- Tilde fence canonical for ARTIFACT block — confirmed working
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
- checkpoint.py steps 10–11 as originally designed
- checkpoint.py artifact extension as CLI argument
- checkpoint.py executing git commands
- Cloud-native execution of checkpoint.py at this stage
- Four-backtick outer fence for ARTIFACT block
- Saving checkpoint input file inside library folder
NEXT TASK: Run checkpoint.py against this checkpoint output for the first successful live test. Copy the CHECKPOINT FILE block below, save it outside the library folder as v10-checkpoint.txt, then run: python3 code/checkpoint.py ai-library-system 10 ~/Desktop/v10-checkpoint.txt. Dry run first, then --write. Verify all files placed correctly and git commit lands clean.
PERSONA: See persona.md
STYLE AND CONSTRAINTS: Plain language. Precise. No lists where prose works better. No suggestions that contradict the established philosophy. When proposing changes to master prompt or documents, show the specific change not a full rewrite.
