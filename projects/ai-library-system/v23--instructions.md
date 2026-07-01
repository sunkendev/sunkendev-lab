INSTRUCTIONS v23
----------------
PROJECT: AI Document Library System
GOAL: Design, document, and iteratively refine a five-layer vendor-agnostic generational system for managing AI-generated work using plain text files and a prompt-controlled workflow.
BACKGROUND: Three decisions made this session: (1) no-out-of-band-fix rule added to MASTER-PROMPT.md behaviour rules — never alter any library file without explicit approval, treat the library as a kernel; (2) MASTER-PROMPT.md write access restricted to ai-library-system by rule in MASTER-PROMPT.md, with pre-commit enforcement as a pending open item; (3) library designated for open source release with ai-library-system project included intact — GitHub remote serves as publication and update channel for shipped libraries.
ARTIFACT STATE: MASTER-PROMPT.md v23 — two new behaviour rules added. Approximately 97 lines.
KEY DECISIONS:
- No out-of-band fix rule: treat library as kernel; surface, design, approve, implement through correct path only
- Only ai-library-system may alter MASTER-PROMPT.md — rule in MASTER-PROMPT.md; pre-commit enforcement pending
- Library ships open source with ai-library-system intact — full history included
- GitHub remote is publication channel, not just backup
OPEN QUESTIONS:
- legal-research has no v00 stubs — needs backfill (created before v5)
- pre-commit.py MASTER-PROMPT.md write protection not yet implemented — block commit if MASTER-PROMPT.md staged and project is not ai-library-system
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
- Remote git for now (superseded — GitHub remote now planned as publication channel)
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
- Slash-containing display text in MAP.md bullet entries
- Out-of-band fixes to library files without explicit user approval — kernel rule, no exceptions
- Management interface as a separate project construct — not needed at this stage
- Developer mode / user mode distinction for shipped library — unnecessary complexity
NEXT TASK: (1) Backfill legal-research v00 stubs — write v00--context.md and v00--instructions.md to projects/legal-research/. (2) Implement MASTER-PROMPT.md write protection in pre-commit.py — block commit if MASTER-PROMPT.md is staged and the committing project triplet does not belong to ai-library-system. (3) GitHub remote setup for open source publication.
PERSONA: See persona.md
STYLE AND CONSTRAINTS: Plain language. Precise. No lists where prose works better. No suggestions that contradict the established philosophy. When proposing changes to master prompt or documents, show the specific change not a full rewrite. State plan before executing any write, script, or git operation.
