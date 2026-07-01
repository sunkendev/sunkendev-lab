INSTRUCTIONS v27
----------------
PROJECT: AI Document Library System
GOAL: Design, document, and iteratively refine a five-layer vendor-agnostic generational system for managing AI-generated work using plain text files and a prompt-controlled workflow.
BACKGROUND: This session added the NO CHANGE sentinel to checkpoint.py — when the ARTIFACT block body is "NO CHANGE", checkpoint.py copies the previous artifact file and relabels it, eliminating verbatim reproduction risk for pure version-bump checkpoints. The design was chosen over a two-mode approach to preserve separation of duties (AI owns all content, checkpoint.py owns all mechanics) and future API compatibility. MASTER-PROMPT.md v27 documents the sentinel in the checkpoint ritual. The session also identified the temp/ cleanup items: three ephemeral skill packages to delete and kurgan-rostok-review.html to move to flow-vs-ai/docs/ pending a decision on HTML frontmatter convention.
ARTIFACT STATE: MASTER-PROMPT.md v27 — NO CHANGE sentinel documented in checkpoint ritual. Approximately 113 lines.
KEY DECISIONS:
- NO CHANGE sentinel: ARTIFACT block body "NO CHANGE" triggers copy-and-relabel of previous artifact
- copy_and_relabel_artifact() copies previous file, rewrites label and separator to new version
- Two-mode design rejected: auto-generating THREAD ENTRY in checkpoint.py crosses content boundary
- Separation of duties: AI owns all content blocks; checkpoint.py owns all mechanics
- Four-block structure preserved — future API pipeline expects LLM to produce all content
OPEN QUESTIONS:
- HTML frontmatter convention: add comment block, or treat HTML as exception to frontmatter rule?
- temp/ cleanup: delete kurgan-rostok.skill, ai-library-ops.skill, zi8mb2D7; move kurgan-rostok-review.html once HTML convention settled
- GitHub remote not yet set up
- iCloud passive rsync backup not yet in workflow
- ARCHITECTURE.tex discrepancies not yet corrected
- related: field path validation in pre-commit hook not yet added
- Lightweight metadata convention for project triplet files not yet defined
- MAP.md machine-readable block not yet added
- DELTA design for checkpoint.py — CONTEXT verbatim reproduction; not yet implemented
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
- Two-mode checkpoint design (--light flag) — splits content generation; complicates API port
- Auto-generating THREAD ENTRY in checkpoint.py — crosses content boundary
NEXT TASK: (1) Resolve HTML frontmatter convention decision, then delete ephemeral files (kurgan-rostok.skill, ai-library-ops.skill, zi8mb2D7) and move kurgan-rostok-review.html to projects/flow-vs-ai/docs/ with correct naming. (2) GitHub remote setup.
PERSONA: See persona.md
STYLE AND CONSTRAINTS: Plain language. Precise. No lists where prose works better. No suggestions that contradict the established philosophy. When proposing changes to master prompt or documents, show the specific change not a full rewrite. State plan before executing any write, script, or git operation.
