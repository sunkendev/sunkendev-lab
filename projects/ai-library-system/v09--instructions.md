INSTRUCTIONS v09
----------------
PROJECT: AI Document Library System
GOAL: Design, document, and iteratively refine a five-layer vendor-agnostic generational system for managing AI-generated work using plain text files and a prompt-controlled workflow.
BACKGROUND: Layers 1 and 2 are fully operational. checkpoint.py (Layer 3) has been designed, built, and tested this session. The script uses sentinel-based library root discovery, file-path input, dry-run default with --write to execute, four-backtick and three-backtick fence parsing, and extracts MAP.md summaries directly from the THREAD ENTRY block. It does not execute git — it prints the commands. Source lives at projects/ai-library-system/code/checkpoint.py; deployed copy goes to code/checkpoint.py at library root.
ARTIFACT STATE: MASTER-PROMPT.md v09 — unchanged from v08. Complete, operational, approximately 80 lines.
KEY DECISIONS:
- checkpoint.py built: sentinel root discovery, file-path input, dry-run default, --write to execute
- Four-backtick and three-backtick outer fence parsing both handled correctly
- MAP.md summaries extracted from THREAD ENTRY **Artifact:**, **Context:**, **Instructions:** fields
- Artifact extension hardcoded to .md — correct for all current projects
- checkpoint.py does not execute git — prints commands for user to run
- checkpoint.py source: projects/ai-library-system/code/checkpoint.py
- checkpoint.py deployment target: code/checkpoint.py at library root
- Cloud-native execution ruled out at this stage — Layer 5 concern
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
NEXT TASK: Deploy checkpoint.py. Save to projects/ai-library-system/code/checkpoint.py and copy to code/checkpoint.py at library root. Add both entries to MAP.md. Commit everything. Then use checkpoint.py on the next real checkpoint to verify the full Layer 3 workflow end to end.
PERSONA: See persona.md
STYLE AND CONSTRAINTS: Plain language. Precise. No lists where prose works better. No suggestions that contradict the established philosophy. When proposing changes to master prompt or documents, show the specific change not a full rewrite.
