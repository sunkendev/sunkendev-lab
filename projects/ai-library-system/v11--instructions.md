INSTRUCTIONS v11
----------------
PROJECT: AI Document Library System
GOAL: Design, document, and iteratively refine a five-layer vendor-agnostic generational system for managing AI-generated work using plain text files and a prompt-controlled workflow.
BACKGROUND: Layer 3 is now fully operational following the successful v10 live test. Three post-v10 fixes were committed: checkpoint.py updated to try tilde fence for all blocks, separator line stripping added to parse_blocks, and pre-commit hook artifact check corrected to non-empty only. The system is stable and the workflow is proven end to end.
ARTIFACT STATE: MASTER-PROMPT.md v11 — unchanged from v10. Complete and operational. Approximately 90 lines.
KEY DECISIONS:
- checkpoint.py fully operational — live test passed at v10
- Tilde fence tried first for all four blocks in parse_blocks
- Separator lines stripped from extracted block content
- Pre-commit hook artifact check: non-empty only, no label check
- Artifact file contains deliverable content only — no wrapper label
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
- Artifact label line in saved artifact file
NEXT TASK: Use checkpoint.py to process this checkpoint. Save the CHECKPOINT FILE block to ~/Desktop/v11-checkpoint.txt and run: python3 code/checkpoint.py ai-library-system 11 ~/Desktop/v11-checkpoint.txt. Dry run first, then --write. This is the second live test — it should be clean.
PERSONA: See persona.md
STYLE AND CONSTRAINTS: Plain language. Precise. No lists where prose works better. No suggestions that contradict the established philosophy. When proposing changes to master prompt or documents, show the specific change not a full rewrite.
