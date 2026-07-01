INSTRUCTIONS v12
----------------
PROJECT: AI Document Library System
GOAL: Design, document, and iteratively refine a five-layer vendor-agnostic generational system for managing AI-generated work using plain text files and a prompt-controlled workflow.
BACKGROUND: Layer 3 is fully operational. This session identified and fixed the label/separator restoration bug in checkpoint.py for context and instructions files, then extended the same fix to artifact files after the identical bug was found there. The previous ruling against artifact label lines was reversed — all three file types are now self-describing by the same convention. The checkpoint workflow was simplified: the CHECKPOINT FILE printed block is replaced by a downloadable .txt file produced directly by the AI.
ARTIFACT STATE: MASTER-PROMPT.md v12 — checkpoint ritual restructured to produce a single downloadable file; CHECKPOINT FILE block eliminated; save instructions reduced from eight steps to five. Approximately 90 lines.
KEY DECISIONS:
- All three file types (artifact, context, instructions) begin with label line and separator
- checkpoint.py reconstructs label and separator for all three file types on write
- Separator width equals label width — self-documenting convention
- Checkpoint file delivered as downloadable .txt — no more printed blocks in chat
- Save instructions: download file, run checkpoint.py dry-run, --write, update MASTER-PROMPT.md if changed, git commit
- Claude Code evaluation prompt pattern established as reusable technique
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
NEXT TASK: Apply the artifact label/separator fix to checkpoint.py (same pattern as context and instructions). Then run checkpoint.py against this file: move v12-checkpoint.txt outside the library folder and run python3 code/checkpoint.py ai-library-system 12 ~/Desktop/v12-checkpoint.txt. Dry run first, then --write. Verify label lines appear in all three written files.
PERSONA: See persona.md
STYLE AND CONSTRAINTS: Plain language. Precise. No lists where prose works better. No suggestions that contradict the established philosophy. When proposing changes to master prompt or documents, show the specific change not a full rewrite.
