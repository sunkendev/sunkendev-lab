INSTRUCTIONS v24
----------------
PROJECT: AI Document Library System
GOAL: Design, document, and iteratively refine a five-layer vendor-agnostic generational system for managing AI-generated work using plain text files and a prompt-controlled workflow.
BACKGROUND: Three items addressed this session: (1) legal-research v00 stubs backfilled — all three files written and committed, closing the RESUME compatibility gap for that project; (2) ai-library-ops skill updated to v6 — NEW PROJECT now writes all three v00 stubs (including artifact) and registers them in MAP.md, closing the same gap for future projects; (3) folder conventions section added to MASTER-PROMPT.md — explicitly documents what belongs in docs/, code/, temp/, inbox/, and library root code/, addressing the temp/ misuse pattern observed in flow-vs-ai.
ARTIFACT STATE: MASTER-PROMPT.md v24 — folder conventions section added. Approximately 110 lines.
KEY DECISIONS:
- legal-research v00 backfill complete — artifact, context, instructions all committed
- skill v6: NEW PROJECT writes all three v00 stubs and registers them in MAP.md
- pre-commit MASTER-PROMPT.md write protection deferred — advisory only; env var bypass agreed for when implemented
- Folder conventions now explicit in MASTER-PROMPT.md — temp/ is checkpoint files only
OPEN QUESTIONS:
- temp/ cleanup in flow-vs-ai: move kurgan-rostok-review.html to projects/flow-vs-ai/docs/; clarify .skill package disposition
- pre-commit.py MASTER-PROMPT.md write protection — optional, deferred; env var pattern agreed
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
- --no-verify as escape hatch for MASTER-PROMPT.md write protection — env var pattern preferred
NEXT TASK: (1) Clean up temp/ misuse in flow-vs-ai — move kurgan-rostok-review.html to projects/flow-vs-ai/docs/ with correct naming and frontmatter; clarify whether .skill packages should be deleted or retained. (2) GitHub remote setup for open source publication.
PERSONA: See persona.md
STYLE AND CONSTRAINTS: Plain language. Precise. No lists where prose works better. No suggestions that contradict the established philosophy. When proposing changes to master prompt or documents, show the specific change not a full rewrite. State plan before executing any write, script, or git operation.
