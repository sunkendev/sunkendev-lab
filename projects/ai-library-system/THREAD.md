# Thread: AI Document Library System
> Started: 2026-04-11 | Status: active

## What this project is

Design and documentation of a five-layer, vendor-agnostic, generational
system for storing, versioning, navigating, and resuming AI-generated work.
The system uses plain text files, a consistent folder hierarchy, a YAML
frontmatter schema, a versioned triplet checkpoint structure, and a master
prompt that bootstraps any AI into operating within the library from a
single paste.

The deliverable is a complete document set: MASTER-PROMPT.md,
USER-GUIDE.tex, ARCHITECTURE.tex, and this THREAD.md. The system
is itself the first project in the library it describes.

## Persona
See persona.md

---
## Checkpoint log

(see v01 entry below after first checkpoint)
THREAD ENTRY v01
----------------
### v01 -- 2026-04-11
**Triggered by:** End of design session. All five layers defined.
All Layer 1 documents produced and compiled. First project execution begins.
**Artifact:** MASTER-PROMPT.md — complete, operational, ~80 lines.
Supporting documents USER-GUIDE.tex (26pp) and ARCHITECTURE.tex (25pp)
compiled and verified.
**Context:** Full system philosophy settled. Five layers defined.
Vendor comparison conducted and philosophy validated. All key decisions made.
**Instructions:** FIRST VERSION — orients new AI to complete system state,
all decisions, and immediate next task of folder setup and file sorting.
**Key decisions made this session:**
- Plain text / Markdown as universal format
- YAML frontmatter as metadata standard
- Two-digit version numbers for correct sort order
- Three-file checkpoint triplet structure
- THREAD.md as project narrative spine
- MAP.md as library traversal index
- Master prompt as sole control mechanism
- Five-layer architecture (Layer 1 mandatory, others optional)
- LaTeX for formal reference documents
**Still open:**
- MASTER-PROMPT.md handling for non-compliant models
- Layer 3 script language choice
- Layer 4 embedding model and vector store selection
- MAP.md machine-readable section for Layer 4 efficiency

THREAD ENTRY v02
----------------
### v02 — 2026-04-11
**Triggered by:** End of second working session — system evolved significantly from v01 baseline.
**Artifact:** MASTER-PROMPT.md updated with new folder structure, enforced context schema, expanded instructions format, and trimmed frontmatter type values.
**Context:** Full state dump conforming to new context schema: PROJECT, DECISIONS, RULED OUT, OPEN, STATE.
**Instructions:** Changed — added EXPLICITLY RULED OUT and STYLE AND CONSTRAINTS fields; updated NEXT TASK to reflect schema work remaining.
**Key decisions made this session:**
- docs/ and code/ moved inside project folders; research/ and creative/ eliminated
- Frontmatter type trimmed to document | code | context
- Context file schema defined and embedded in MASTER-PROMPT.md
- Instructions file schema defined and confirmed
- ORIGIN removed from context schema; episodic history belongs in THREAD.md
- v01 files designated pre-schema legacy
**Still open:**
- Artifact file schema not yet defined
- Instructions schema not yet explicitly embedded in MASTER-PROMPT.md block 3
- layer-1-foundation.md needs full rewrite
- ARCHITECTURE.tex and USER-GUIDE.tex not yet updated
- Layer 3 script not yet scoped or written

THREAD ENTRY v03
----------------
### v03 — 2026-04-11
**Triggered by:** Completion of all schema work and pre-git state capture.
**Artifact:** MASTER-PROMPT.md v03 — all checkpoint block schemas embedded, artifact wrapper added.
**Context:** All seven schemas confirmed; persona.md and THREAD.md updated to conform; git selected as Layer 3 foundation.
**Instructions:** Changed — updated KEY DECISIONS, OPEN QUESTIONS, and NEXT TASK to reflect schema completion and git initialisation as next step.
**Key decisions made:**
- All seven file schemas defined and confirmed
- Artifact type schemas defined at time of first use not speculatively
- THREAD.md ascending order confirmed for AI context loading
- persona.md EXAMPLES section mandatory not optional
- Git as Layer 3 foundation with pre-commit validation hook
- vNN prefix retained alongside git for human readability
- Checkpoint reserved for major milestones; routine sessions are git commits only
**Still open:**
- Schema reference document not yet saved to library
- layer-1-foundation.md needs full rewrite
- ARCHITECTURE.tex and USER-GUIDE.tex not yet updated
- Layer 3 validation script not yet written
- git not yet initialised

THREAD ENTRY v04
----------------
### v04 — 2026-04-11
**Triggered by:** End of session — git initialised, library fully operational.
**Artifact:** MASTER-PROMPT.md v04 — unchanged from v03, all schemas embedded.
**Context:** Git initialised with first commit on main branch; all seven schemas saved; library confirmed clean via cat review.
**Instructions:** Changed — added git commit ID, library path, and updated NEXT TASK to pre-commit validation script.
**Key decisions made:**
- Git initialised at commit 5a20741 on main branch
- Library path confirmed: ~/AI-Library (iCloud)
- Layer 1 declared fully operational
- Pre-commit validation script is next priority
**Still open:**
- Pre-commit validation script not yet written
- layer-1-foundation.md needs full rewrite
- ARCHITECTURE.tex and USER-GUIDE.tex not yet updated
- Artifact type schema for .md prompt type not yet formalised
- Remote git not yet set up

THREAD ENTRY v05
----------------
### v05 — 2026-04-11
**Triggered by:** RESUME procedure corrected to require all four files — significant enough to warrant checkpoint.
**Artifact:** MASTER-PROMPT.md v05 — RESUME procedure updated to require persona.md, THREAD.md, context, and instructions in order.
**Context:** Full state dump with corrected RESUME decision and manual verification step added to RULED OUT and DECISIONS.
**Instructions:** Changed — RESUME correction added to KEY DECISIONS and EXPLICITLY RULED OUT; NEXT TASK unchanged.
**Key decisions made:**
- RESUME requires four files in order: persona.md, THREAD.md, context, instructions
- Resuming from instructions file alone ruled out — insufficient context
- .git and .DS_Store excluded from MAP.md
- Manual cat verification before every commit until pre-commit hook exists
**Still open:**
- Pre-commit validation script not yet written
- layer-1-foundation.md needs full rewrite
- ARCHITECTURE.tex and USER-GUIDE.tex not yet updated
- Artifact type schema for .md prompt type not yet formalised
- Remote git not yet set up

THREAD ENTRY v06
----------------
### v06 — 2026-04-11
**Triggered by:** Pre-commit validation hook written, tested, installed, and committed — major Layer 3 milestone.
**Artifact:** MASTER-PROMPT.md v06 — unchanged from v05; artifact version incremented to keep triplet in sync with context and instructions.
**Context:** Full state dump capturing all hook decisions, block vs warn logic, exclusion strategy, and MAP.md/THREAD.md integrity checks.
**Instructions:** Changed — BACKGROUND updated to reflect hook completion; NEXT TASK updated to layer-1-foundation.md rewrite.
**Key decisions made:**
- Triplet lockstep enforced as hard block on any vNN file staged
- Version mismatch within project folder is a hard block
- MAP.md path integrity and THREAD.md order checks added as warnings
- Exclusions centralised in single EXCLUDED set in script
- Pre-commit hook does not check itself — correctly excluded
- Block vs warn boundary: structure blocks, advisory warns
**Still open:**
- layer-1-foundation.md needs full rewrite
- ARCHITECTURE.tex and USER-GUIDE.tex not yet updated
- Artifact type schema for .md prompt type not yet formalised
- Remote git not yet set up
- Git identity not yet configured

THREAD ENTRY v07
----------------
### v07 — 2026-04-11
**Triggered by:** NOTE format added to MASTER-PROMPT.md and THREAD.md schema — milestone change to core document.
**Artifact:** MASTER-PROMPT.md v07 — NOTE inter-checkpoint format added; all other sections unchanged.
**Context:** Full state dump capturing control panel architecture, Layer 2 design and documentation, cloud platform comparison, privacy and IP rationale, and NOTE schema addition.
**Instructions:** Changed — BACKGROUND updated with session work; NEXT TASK updated to scripts/ deployment and Layer 2 platform experiment.
**Key decisions made:**
- NOTE format defined: NOTE YYYY-MM-DD, Topic line, prose — no triplet, no version number, no validation
- scripts/ at library root is deployment target; project code/ is source
- projects/ai-library-system/ is the control panel for the library
- Layer 2 consumer app tier only — API cost prohibitive
- Cloud-native alternatives evaluated and ruled out for personal use on privacy, IP, cost, and durability grounds
- ARCHITECTURE.tex and USER-GUIDE.tex deferred until scripted live
**Still open:**
- Layer 2 platform experiment not yet run
- scripts/ folder not yet created or deployed
- NOTE format not yet added to layer-1-foundation document
- ARCHITECTURE.tex discrepancies not yet corrected
- Layer 4 not yet designed

NOTE 2026-04-11
---------------
**Topic:** Post-v07 decisions not yet in triplet
- scripts/ folder name corrected to code/ — consistent with project folder convention throughout
- code/ folder created at library root as deployment target for operational scripts
- pre-commit.py deployed to code/pre-commit.py at library root
- MAP.md updated to add code/ section
- libmap shell alias added to ~/.zshrc for library tree view
- All committed to git at 9513aef but not captured in v07 context
These decisions will be folded into the next checkpoint context file.

NOTE 2026-04-11
---------------
**Topic:** NOTE format added to layer-1-foundation reference
Added NOTE format block to THREAD.md section of
2026-04-11--layer-1-foundation--claude.md. Closes the open item carried
since v07. No schema changes — text matches MASTER-PROMPT.md exactly.

NOTE 2026-04-11
---------------
**Topic:** THREAD.md immediate-commit rule added to MASTER-PROMPT.md
Regression identified: THREAD.md was drifting uncommitted while other work
continued. Rule added to MASTER-PROMPT.md requiring immediate commit after
every NOTE append.

NOTE 2026-04-11
---------------
**Topic:** Five-layer evaluation completed by Claude Code
An external evaluation of the full system was run by Claude Code
(claude-sonnet-4-6) reading the live library. Report saved to
projects/ai-library-system/docs/2026-04-11--layer-1-5-eval--claude.md.
Key findings to carry forward:
- 2026-04-11--claude-code-eval--claude.md has no frontmatter and is not in MAP.md
- related: fields use bare filenames not relative paths — pre-commit hook should warn
- ARCHITECTURE.tex Layer 2 session start contradicts Layer 2 doc — fix before next platform experiment
- checkpoint.py design references eliminated schema elements (THREAD.md header, MAP.md Recent table)
- Project triplet files have no frontmatter — define convention before Layer 4
- MAP.md needs machine-readable block before Layer 5 / MCP work
- .mcp-config.json in ARCHITECTURE.tex lists eliminated root folders
- Claude Code created .claude/worktrees/ — add .claude/ to .gitignore

THREAD ENTRY v08
----------------
### v08 — 2026-04-11
**Triggered by:** End of session — Layer 2 confirmed, Claude Code evaluation completed, MASTER-PROMPT.md updated with NOTE immediate-commit rule.
**Artifact:** MASTER-PROMPT.md v08 — NOTE immediate-commit rule added; all other sections unchanged.
**Context:** Full state dump capturing Layer 2 confirmation, Claude Code evaluation findings, .gitignore and libmap updates, and revised checkpoint.py design constraints.
**Instructions:** Changed — KEY DECISIONS updated with session work; NEXT TASK updated to checkpoint.py revised design and build.
**Key decisions made:**
- NOTE immediate-commit rule added to MASTER-PROMPT.md after regression identified
- Layer 2 confirmed working via live Claude Project experiment
- Claude Code five-layer evaluation completed — findings captured
- .claude/ added to .gitignore; libmap alias updated
- checkpoint.py clipboard-default and steps 10–11 ruled out
**Still open:**
- checkpoint.py revised design and build
- related: fields bare filename warning not yet in pre-commit hook
- Lightweight metadata convention for project triplet files
- MAP.md machine-readable block
- ARCHITECTURE.tex discrepancies

NOTE 2026-04-11
---------------
**Topic:** Four-backtick outer fence rule added to MASTER-PROMPT.md
Nested code block rendering fix — artifact blocks containing fenced
code use four backticks as outer fence to prevent fence collision.
Added to artifact wrapper schema in checkpoint ritual.

THREAD ENTRY v09
----------------
### v09 — 2026-04-12
**Triggered by:** checkpoint.py designed, built, tested, and ready for deployment — Layer 3 milestone.
**Artifact:** MASTER-PROMPT.md v09: unchanged from v08; version incremented to keep triplet in sync.
**Context:** Full state dump v09: checkpoint.py complete, all design decisions captured, deployment pending.
**Instructions:** Changed — BACKGROUND updated with checkpoint.py completion; NEXT TASK updated to deployment and first live use.
**Key decisions made:**
- checkpoint.py built: sentinel root discovery, file-path input, dry-run default, --write to execute
- Four-backtick and three-backtick fence parsing both handled correctly
- MAP.md summaries extracted from THREAD ENTRY fields directly
- Artifact extension hardcoded to .md; cloud-native execution deferred to Layer 5
**Still open:**
- ARCHITECTURE.tex discrepancies
- related: field path validation in pre-commit hook
- Lightweight metadata convention for project triplet files
- MAP.md machine-readable block

NOTE 2026-04-12
---------------
**Topic:** Tilde fence fix for ARTIFACT block
MASTER-PROMPT.md updated: ~~~ replaces four-backtick rule for ARTIFACT outer fence.
checkpoint.py updated: tilde pattern added as canonical parser for ARTIFACT block;
four-backtick and three-backtick retained as legacy fallbacks.

NOTE 2026-04-12
---------------
**Topic:** CHECKPOINT FILE block added to checkpoint ritual
Added step 5 to checkpoint ritual: a ready-to-save CHECKPOINT FILE v[NN]
block containing all four blocks with fence delimiters, for direct use
as checkpoint.py input. Save instructions updated — step 0 added.

NOTE 2026-04-12
---------------
**Topic:** Version guard added to checkpoint ritual
MASTER-PROMPT.md updated: checkpoint ritual now requires THREAD.md
to be present before producing output, to prevent version number
errors when RESUME is skipped.

THREAD ENTRY v10
----------------
### v10 — 2026-04-12
**Triggered by:** Three post-v09 improvements committed — CHECKPOINT FILE block, version guard, tilde fence — milestone sufficient for checkpoint.
**Artifact:** MASTER-PROMPT.md v10: CHECKPOINT FILE block and version guard added to checkpoint ritual.
**Context:** Full state dump v10: all Layer 3 decisions captured, checkpoint.py live test ready to run.
**Instructions:** Changed — BACKGROUND updated with three improvements; NEXT TASK is first successful checkpoint.py live test.
**Key decisions made:**
- CHECKPOINT FILE block added as step 5 of checkpoint ritual
- checkpoint.py input file must be saved outside library folder
- Version guard added — THREAD.md required before checkpoint proceeds
- Saving checkpoint input inside library folder ruled out
**Still open:**
- ARCHITECTURE.tex discrepancies
- related: field path validation in pre-commit hook
- Lightweight metadata convention for project triplet files
- MAP.md machine-readable block

NOTE 2026-04-12
---------------
**Topic:** checkpoint.py updated — tilde fence for all blocks
parse_blocks updated to try tilde fence first for all four blocks,
not just ARTIFACT. Handles input files where all blocks use tilde fences.

NOTE 2026-04-12
---------------
**Topic:** checkpoint.py updated — separator line stripping
parse_blocks now strips leading separator lines (--- or ------) from
extracted block content. Fixes context and instructions files starting
with separator instead of PROJECT: line.

NOTE 2026-04-12
---------------
**Topic:** pre-commit hook updated — artifact wrapper check corrected
check_artifact_wrapper simplified to non-empty check only. Removed
incorrect first-line label check — artifact files contain deliverable
content, not wrapped blocks.

NOTE 2026-04-12
---------------
**Topic:** Layer 2 workspace system prompt out of sync
Claude Project system prompt still reflects pre-v10 MASTER-PROMPT.md.
Does not include CHECKPOINT FILE block, version guard, or tilde fence rule.
Must be updated to v11 before next Layer 2 session.

THREAD ENTRY v11
### v11 — 2026-04-12
**Triggered by:** Layer 3 fully operational — post-v10 fixes committed, system stable.
**Artifact:** MASTER-PROMPT.md v11: unchanged from v10; version incremented for triplet sync.
**Context:** Full state dump v11: all Layer 3 decisions captured, three post-v10 fixes recorded.
**Instructions:** Changed — BACKGROUND updated with post-v10 fixes; NEXT TASK is second checkpoint.py live test.
**Key decisions made:**
- checkpoint.py tilde fence tried first for all blocks
- Separator line stripping added to parse_blocks
- Pre-commit hook artifact check corrected to non-empty only
- Artifact file contains deliverable content only — no wrapper label
**Still open:**
- ARCHITECTURE.tex discrepancies
- related: field path validation in pre-commit hook
- Lightweight metadata convention for project triplet files
- MAP.md machine-readable block

NOTE 2026-04-12
---------------
**Topic:** checkpoint.py — label and separator restoration fix
parse_blocks() consumes the label line (via regex) and strips the separator
(via while loop). The write block in main() was not reconstructing either,
so context and instructions files written by the script were missing their
opening label and separator lines. Fixed by prepending label and derived-length
separator before each write. Comment added at write site to make the coupling
explicit. Separator width matches label width by convention — consistent with
all files on disk. Fix applied to projects/ai-library-system/code/checkpoint.py
and deployed to code/checkpoint.py.

THREAD ENTRY v12
### v12 — 2026-04-12
**Triggered by:** checkpoint.py label/separator fix extended to artifacts; checkpoint workflow simplified to single downloadable file.
**Artifact:** MASTER-PROMPT.md v12 — checkpoint ritual produces downloadable file; CHECKPOINT FILE block eliminated; save instructions reduced to five steps.
**Context:** All label restoration decisions captured; artifact self-describing convention confirmed for all three file types; Claude Code evaluation prompt pattern recorded.
**Instructions:** Changed — BACKGROUND updated with session work; NEXT TASK updated to artifact fix and v12 live test.
**Key decisions made:**
- All three file types begin with label and separator — self-describing by convention
- checkpoint.py reconstructs label and separator for artifact, context, and instructions on write
- Previous ruling against artifact label line reversed
- Checkpoint file now delivered as downloadable .txt — CHECKPOINT FILE block eliminated
- Save instructions reduced to five steps
- Claude Code evaluation prompt pattern established as reusable technique
**Still open:**
- ARCHITECTURE.tex discrepancies
- related: field path validation in pre-commit hook
- Lightweight metadata convention for project triplet files
- MAP.md machine-readable block

THREAD ENTRY v13
### v13 — 2026-04-12
**Triggered by:** Layer 2 workspace system prompt update step added to MASTER-PROMPT.md save instructions.
**Artifact:** MASTER-PROMPT.md v13 — step 3 of save instructions expanded to include Layer 2 system prompt update.
**Context:** One decision added; all other state unchanged from v12.
**Instructions:** Changed — NEXT TASK updated to include Layer 2 system prompt update.
**Key decisions made:**
- Layer 2 workspace system prompt update is mandatory when artifact is MASTER-PROMPT.md
**Still open:**
- ARCHITECTURE.tex discrepancies
- related: field path validation in pre-commit hook
- Lightweight metadata convention for project triplet files
- MAP.md machine-readable block

NOTE 2026-04-12
---------------
**Topic:** Tilde fence collision in ARTIFACT block — v12 and v13 artifacts truncated and repaired
MASTER-PROMPT.md v12 introduced a literal ~~~ example in the checkpoint ritual
to illustrate the block format. This collided with the tilde fence parser in
checkpoint.py — the regex terminated the ARTIFACT block at the first inner ~~~,
truncating everything after it. v12 and v13 artifact files were written truncated
to disk. Fixed by replacing the literal tilde example with prose: "Each block is
wrapped in tilde fences (~~~) with the label as the first line inside the fence."
Truncated files repaired manually and committed at 7fcaea5. MASTER-PROMPT.md at
library root updated to corrected v13 content. Rule going forward: MASTER-PROMPT.md
content must never contain a line starting with ~~~ as it will terminate the
ARTIFACT block during parsing.

NOTE 2026-04-12
---------------
**Topic:** temp/ folder and add_note_thread.py added
Testing the new temp/ folder and note script.

NOTE 2026-04-12
---------------
**Topic:** Tilde fence collision — v12 and v13 artifact truncation and repair
MASTER-PROMPT.md v12 introduced a literal ~~~ example in the checkpoint ritual to illustrate the block format. This collided with the tilde fence parser in checkpoint.py — the regex terminated the ARTIFACT block at the first inner ~~~, truncating everything after it. v12 and v13 artifact files were written truncated to disk. Fixed by replacing the literal tilde example with prose. Truncated files repaired manually and committed at 7fcaea5. Rule going forward: MASTER-PROMPT.md content must never contain a line starting with ~~~ as it will terminate the ARTIFACT block during parsing.

THREAD ENTRY v14
### v14 — 2026-04-12
**Triggered by:** temp/ folder, add_note_thread.py, and checkpoint.py default path — all operational and committed.
**Artifact:** MASTER-PROMPT.md v14 — temp/ in structure diagram; NOTE instructions reference add_note_thread.py; save instructions updated for temp/ workflow.
**Context:** All Layer 3 automation decisions captured including temp/ convention, add_note_thread.py, tilde fence collision rule, and Claude Code execution layer as next open item.
**Instructions:** Changed — BACKGROUND and NEXT TASK updated to reflect session work.
**Key decisions made:**
- temp/ is canonical checkpoint file location — excluded from git and pre-commit hook
- checkpoint.py input-file now optional — defaults to temp/v[NN]-checkpoint.txt
- add_note_thread.py automates NOTE appending and immediate commit
- MASTER-PROMPT.md must never contain a line starting with ~~~
**Still open:**
- ARCHITECTURE.tex discrepancies
- related: field path validation in pre-commit hook
- Lightweight metadata convention for project triplet files
- MAP.md machine-readable block
- Claude Code execution layer

THREAD ENTRY v15
### v15 — 2026-04-12
**Triggered by:** SHA-256 manifest and integrity validation complete; v14 context repaired; library audit clean — milestone sufficient for checkpoint.
**Artifact:** MASTER-PROMPT.md v15 — unchanged from v14; version incremented for triplet sync.
**Context:** Full integrity validation stack captured: SHA-256 manifest, DECISIONS superset check, size ratios, label validation, tamper detection for six files.
**Instructions:** Changed — BACKGROUND updated with integrity validation work; NEXT TASK is first live integrity validation test.
**Key decisions made:**
- checkpoint.py integrity validation runs after every --write
- SHA-256 manifest covers artifact, context, instructions, THREAD.md, MAP.md, persona.md
- DECISIONS/RULED OUT superset check catches dropped lines
- Size ratio thresholds catch truncation
- MASTER-PROMPT.md excluded from manifest — legitimate hash changes
- v14 context repaired — all dropped decisions restored
**Still open:**
- ARCHITECTURE.tex discrepancies
- related: field path validation in pre-commit hook
- Lightweight metadata convention for project triplet files
- MAP.md machine-readable block
- Claude Code execution layer

NOTE 2026-04-12
---------------
**Topic:** add_note_thread.py live test
add_note_thread.py deployed and operational. Tested via this note — script reads body from stdin, formats NOTE with today's date, appends to THREAD.md, and commits immediately. Immediate-commit rule now enforced automatically. No manual THREAD.md editing required for inter-checkpoint notes.

THREAD ENTRY v16
### v16 — 2026-04-13
**Triggered by:** Library fork to ~/Claude/Projects/AI-Library/ complete; Cowork project created; pivot to Cowork as orchestrator settled.
**Artifact:** MASTER-PROMPT.md v16 — unchanged from v15, version incremented for triplet sync.
**Context:** Fork decisions, WORM storage strategy, new library path, Cowork setup, and all new RULED OUT entries captured.
**Instructions:** Changed — BACKGROUND updated with fork and Cowork pivot; NEXT TASK updated to Cowork orchestration skill build.
**Key decisions made:**
- iCloud library frozen at v15 as permanent baseline
- New library forked to ~/Claude/Projects/AI-Library/ — local SSD, independent git repo, commit 8e9ac4a
- Cowork designated as Layer 2+3 orchestrator
- WORM strategy: local SSD primary, iCloud passive rsync, GitHub WORM, USB-C 2TB SSD tertiary
- Cowork project AI-Library created with MASTER-PROMPT.md + persona.md as instructions
- macOS protected folders (Documents, Desktop, Downloads) avoided as library home
- ~/Documents/ as library location ruled out
- Git branch as fork mechanism ruled out
- iCloud Drive as git working directory ruled out
**Still open:**
- Cowork orchestration skill not yet built
- iCloud passive backup (rsync) not yet in workflow
- GitHub remote not yet set up
- USB-C 2TB SSD backup not yet configured
- ARCHITECTURE.tex discrepancies
- MAP.md machine-readable block

THREAD ENTRY v17
### v17 — 2026-04-13
**Triggered by:** ai-library-ops Cowork orchestration skill built, packaged, and installed — Layer 3 automation complete.
**Artifact:** MASTER-PROMPT.md v17 — unchanged from v16, version incremented for triplet sync.
**Context:** Skill design decisions captured; all Layer 3 automation decisions recorded; Cowork open item closed.
**Instructions:** Changed — BACKGROUND updated with skill completion and Layer 3 status; NEXT TASK updated to GitHub remote setup.
**Key decisions made:**
- ai-library-ops skill built with three operations: CHECKPOINT, NOTE, COMMIT
- Skill source at projects/ai-library-system/code/ai-library-ops/SKILL.md — project → library convention
- Library root discovery via Path('.').rglob('MAP.md') + cd; required because scripts use Path.cwd()
- git add and git commit now executed by skill in Cowork sessions
- Manual terminal operations for library work ruled out in Cowork sessions
**Still open:**
- GitHub remote not yet set up
- iCloud passive rsync backup not yet in workflow
- ARCHITECTURE.tex discrepancies
- MAP.md machine-readable block

NOTE 2026-04-13
---------------
**Topic:** Post-v17 decisions from first live skill run
Two decisions surfaced during the v17 checkpoint run and are not in the v17 context file.

First: SKILL.md excluded from pre-commit frontmatter check. Skill framework files use their own frontmatter schema (name, description) not the library schema (title, date, type, vendor, model, tags, related, updated). Added "SKILL.md" to the EXCLUDED set in both code/pre-commit.py and projects/ai-library-system/code/pre-commit.py. Rule: any file named SKILL.md anywhere in the library is excluded from frontmatter validation.

Second: .git/hooks/pre-commit is a copy not a symlink. When pre-commit.py is updated, the hook must be redeployed manually: cp code/pre-commit.py .git/hooks/pre-commit. This is a known fragility — the hook and its source can drift. Carry forward as an open item until a Makefile or deploy script enforces sync.

NOTE 2026-04-13
---------------
**Topic:** Hook drift eliminated — wrapper replaces copy
Resolved the .git/hooks/pre-commit drift problem permanently. The hook file is now a three-line bash wrapper that delegates to code/pre-commit.py via `git rev-parse --show-toplevel`. Any future update to code/pre-commit.py is immediately reflected with no deploy step. The manual `cp code/pre-commit.py .git/hooks/pre-commit` step is eliminated. Rule going forward: never copy the script to the hook location again — the wrapper is the hook.

NOTE 2026-04-13
---------------
**Topic:** Lock cleanup and hook wrapper — post-v17 fixes
Three fixes applied after the v17 first-run findings. First: .git/hooks/pre-commit replaced with a three-line bash wrapper that delegates to code/pre-commit.py — no more drift between hook and source, cp step eliminated permanently. Second: add_note_thread.py updated to clear stale index.lock and HEAD.lock before git operations — prevents cascade failures when a prior crashed git process left lock files behind. Third: ai-library-ops skill updated with the same defensive lock cleanup before every git step, and library root discovery changed from Path('.').rglob() to find /sessions — CWD-independent, works regardless of what commands ran earlier in the session. Root cause of the original failures was missing git identity (now in .git/config); the lock cleanup and stable discovery are defence in depth.

THREAD ENTRY v18
### v18 — 2026-04-13
**Triggered by:** Post-v17 operational fixes complete — Cowork git reliability fully resolved, self-containment principle established.
**Artifact:** MASTER-PROMPT.md v18 — unchanged from v16, version incremented for triplet sync.
**Context:** All Cowork git patterns captured; self-containment principle established; hook wrapper, lock handling, and CWD-stable discovery recorded.
**Instructions:** Changed — BACKGROUND updated with post-v17 fixes; NEXT TASK updated to skill reinstall then GitHub remote.
**Key decisions made:**
- Self-containment principle: nothing writes outside ~/Claude/Projects/AI-Library/
- .git/hooks/pre-commit is now a bash wrapper — drift eliminated permanently
- allow_cowork_file_delete required before git ops; one call grants session-wide permission
- Library discovery changed to find /sessions — CWD-independent
- write_snapshot removed from pre-commit.py as self-containment violation
**Still open:**
- GitHub remote not yet set up
- iCloud passive rsync backup not yet in workflow
- ai-library-ops skill v2 needs reinstall

NOTE 2026-04-13
---------------
**Topic:** ai-library-ops skill reinstalled (v2)
Installed the updated ai-library-ops.skill from temp/ in Cowork, replacing the v1 build. This version includes all post-v17 reliability fixes: allow_cowork_file_delete call before git ops, CWD-independent library discovery via find /sessions, and stale lock cleanup. NEXT TASK from v18 instructions is now complete. Remaining: GitHub remote setup.

THREAD ENTRY v19
### v19 — 2026-04-13
**Triggered by:** RESUME and NEW PROJECT operations built, tested end-to-end, and committed — Layer 3 automation complete.
**Artifact:** MASTER-PROMPT.md v19 — unchanged from v18, version incremented for triplet sync.
**Context:** All skill v3 decisions captured; MAP.md format bug identified and fixed; legal-research test project live.
**Instructions:** Changed — BACKGROUND updated with skill v3 completion; NEXT TASK updated to skill reinstall then GitHub remote.
**Key decisions made:**
- RESUME reads four files from disk — no copy-paste required in Cowork sessions
- NEW PROJECT: three guided questions, one at a time, with format-example options; no files written until persona confirmed
- MAP.md project entry format: ## projects/[slug]/ section with bullet items before ## inbox/
- legal-research test project created and committed — both operations verified end to end
**Still open:**
- ai-library-ops skill v3 needs reinstall in Cowork (MAP.md format fix)
- GitHub remote not yet set up
- iCloud passive rsync backup not yet in workflow

THREAD ENTRY v20
### v20 — 2026-04-13
**Triggered by:** Behaviour rule added to MASTER-PROMPT.md and persona.md; v18 compression forensics completed and documented; context detection skill designed.
**Artifact:** MASTER-PROMPT.md v20 — one behaviour rule added: AI must state plan before any write/script/git operation and wait for confirmation.
**Context:** Forensic findings captured: 130K Tier 1 threshold, 155K Tier 2, usage field as sole reliable source, file-first design validated.
**Instructions:** Changed — BACKGROUND updated with session work; NEXT TASK updated to log location decision then context detection skill build.
**Key decisions made:**
- Behaviour rule added to MASTER-PROMPT.md and persona.md requiring plan confirmation before execution
- Context detection thresholds established: Tier 1 130K, Tier 2 155K input tokens
- Usage field is only reliable detection source
- Context pressure events go in separate operational log, not THREAD.md
- File-first checkpoint design validated by v18 compression event
**Still open:**
- Operational log location for context pressure events
- Context detection skill not yet built
- GitHub remote not yet set up

NOTE 2026-04-13
---------------
**Topic:** Forensics doc not referenced in MAP.md
Pre-commit hook warned at v20 commit: projects/ai-library-system/docs/2026-04-13--v18-compression-forensics--claude.md is not referenced in MAP.md. A MAP entry needs to be added under the ## projects/ai-library-system/ section before the next commit.

NOTE 2026-04-13
---------------
**Topic:** THREAD.md growth wall analysis
Analysed the long-term growth limits of the RESUME payload. At current growth rate (~650 tokens per checkpoint), the practical wall — where RESUME load consumes all available working budget before any work begins — is reached at approximately v132. The hard wall (context window exhausted at load) is around v240, but the system is effectively unusable from v132 onward. THREAD.md is the primary driver due to unconstrained NOTE accumulation. Three mitigations documented: THREAD.md archiving (recommended, implement before v70), context.md summarisation at milestones, and project forking. Full analysis in projects/ai-library-system/docs/2026-04-13--thread-growth-analysis--claude.md.

NOTE 2026-04-13
---------------
**Topic:** Skill repackaging: always rm -f old .skill before zip
When repackaging a skill, always delete the existing .skill file before running zip. Running zip against an existing file appends to it rather than replacing it, producing duplicate SKILL.md entries and a "Zip must contain exactly one SKILL.md file" install error. Correct sequence: rm -f temp/[skill-name].skill && cd projects/ai-library-system/code && zip -r $LIBRARY/temp/[skill-name].skill [skill-dir]/

NOTE 2026-04-13
---------------
**Topic:** Context check — session_info blind spot for current session
Attempted a live CONTEXT CHECK mid-session. list_sessions does not surface the current session — only other sessions are visible. No direct token count is available from within an active session via session_info. Estimated ~90K–110K tokens based on known fixed costs (system prompt ~38.5K, RESUME payload ~18.5K) plus session activity (40+ exchanges, 7 large file reads, 5 writes, 2 web searches, multiple bash runs). Well below Tier 1 threshold (130K). Key implication for the context detection skill: self-monitoring via session_info is not viable. The skill cannot read its own session's usage field. Alternative approaches needed: self-assessment heuristic, or a proxy metric such as counting tool calls and estimating tokens per call type.

THREAD ENTRY v21
### v21 — 2026-04-13
**Triggered by:** Context detection feature complete — logs/ folder, skill v4 with automatic per-operation status line, Tier 1/Tier 2 thresholds, and context-pressure.log created and committed.
**Artifact:** MASTER-PROMPT.md v21 — logs/ added to library structure diagram.
**Context:** Context detection decisions captured: estimate model, thresholds, automatic reporting, logs/ location, three new RULED OUT entries.
**Instructions:** Changed — BACKGROUND updated with context detection completion; NEXT TASK updated to GitHub remote setup.
**Key decisions made:**
- logs/ folder at library root, excluded from git — context pressure events only
- Automatic per-operation context status preferred over manual CONTEXT CHECK command
- Estimate model: fixed ~57K + per-call weights; Tier 1 at 130K, Tier 2 at 155K
- ai-library-ops skill v4 installed with Context Awareness section
- session_info ruled out for self-monitoring — list_sessions does not surface active session
**Still open:**
- GitHub remote not yet set up
- iCloud passive rsync backup not yet in workflow
- ARCHITECTURE.tex discrepancies

NOTE 2026-04-13
---------------
**Topic:** Post-v21 fixes: v00 stubs, skill deployment, pre-commit false positive
Three fixes made after v21 checkpoint.

First: NEW PROJECT gap identified — fresh projects had no v00 context or instructions stubs, so RESUME would fail to load the required four files. ai-library-ops skill v5 fixes this: Step 4 of NEW PROJECT now writes v00--context.md and v00--instructions.md alongside persona.md and THREAD.md. v00 stubs are superseded after first real CHECKPOINT produces v01.

Second: skill source deployed to code/ai-library-ops/SKILL.md at library root. Previously the skill lived only in projects/ai-library-system/code/ai-library-ops/ — it would be missing if the library was shipped without projects/. Deployed copy follows the same project → library convention as checkpoint.py, pre-commit.py, and add_note_thread.py. MAP.md updated accordingly.

Third: pre-commit false positive fixed. The check_map_integrity regex matches all slash-containing strings in MAP.md, including markdown display text — not just link URLs. The display text ai-library-ops/SKILL.md was being extracted and checked as a path (without the code/ prefix), producing a spurious warning. Fixed by changing display text to bare filename SKILL.md. Convention going forward: MAP.md display text must be a bare filename with no slashes.

THREAD ENTRY v22
### v22 — 2026-04-13
**Triggered by:** Post-v21 fixes complete — v00 stubs, skill deployment to code/, MAP.md display text convention established.
**Artifact:** MASTER-PROMPT.md v22 — unchanged from v21, version incremented for triplet sync.
**Context:** Three new decisions captured: v00 stubs in NEW PROJECT, skill at code/ root, no-slash display text rule.
**Instructions:** Changed — BACKGROUND updated with post-v21 fixes; NEXT TASK updated to legal-research v00 backfill then GitHub remote.
**Key decisions made:**
- ai-library-ops skill v5: NEW PROJECT writes v00 stubs for RESUME compatibility
- Skill source deployed to code/ai-library-ops/ — ships with library independent of projects/
- MAP.md display text: bare filename only, no slashes — pre-commit regex false positive fix
**Still open:**
- legal-research v00 stubs need backfill
- GitHub remote not yet set up

THREAD ENTRY v23
### v23 — 2026-04-14
**Triggered by:** Three design decisions settled this session: no-out-of-band-fix kernel rule, MASTER-PROMPT.md project lock, and open source shipping designation.
**Artifact:** MASTER-PROMPT.md v23 — two new behaviour rules added: no-out-of-band-fix kernel rule and ai-library-system-only MASTER-PROMPT.md write rule.
**Context:** Four new decisions and three new ruled-out entries captured; pre-commit MASTER-PROMPT.md enforcement added as open item; GitHub remote reframed as publication channel.
**Instructions:** Changed — BACKGROUND updated with three session decisions; NEXT TASK updated to legal-research backfill, pre-commit enforcement, GitHub setup.
**Key decisions made:**
- Never make out-of-band fixes without explicit approval — treat library as kernel
- Only ai-library-system may alter MASTER-PROMPT.md
- Library ships open source with ai-library-system intact and full history
- GitHub remote is publication and update channel
**Still open:**
- legal-research v00 stubs backfill
- pre-commit.py MASTER-PROMPT.md write protection not yet implemented
- GitHub remote not yet set up

NOTE 2026-04-14
---------------
**Topic:** Integrity check false positive on THREAD.md and MAP.md
checkpoint.py integrity check always fires TAMPER DETECTED on THREAD.md and MAP.md at every --write run. Root cause: the tamper check compares current on-disk hashes against the previous manifest, but it runs after checkpoint.py has already appended to both files. By the time the check executes, the files have been legitimately modified by this same run. The hashes will never match the previous manifest. To be meaningful, the tamper check for THREAD.md and MAP.md would need to run before the write step — capturing pre-write hashes and comparing against the previous manifest, then writing, then capturing post-write hashes for the new manifest. Current behaviour is warn-only and does not block commits, so this is noise rather than a failure. Carry forward as a known design limitation until pre-commit.py is next revised.

NOTE 2026-04-15
---------------
**Topic:** MASTER-PROMPT.md write protection — deferred optional hardening
Pre-commit enforcement of the MASTER-PROMPT.md project lock rule was evaluated and deferred. The rule exists in MASTER-PROMPT.md as a behaviour instruction (only ai-library-system may alter MASTER-PROMPT.md) but is not structurally enforced by the hook.

Decision: skip for now. Risk is low while the library is single-user. Grows at open source publication.

Proposed implementation when ready: environment variable bypass pattern — ALLOW_MASTER_PROMPT_WRITE=1 git commit — rather than --no-verify. Surgical: bypasses only the MASTER-PROMPT.md check, all other hook checks still run. Error message should document the bypass command inline so it is discoverable without hunting.

Revisit before or during GitHub remote setup.

THREAD ENTRY v24
### v24 — 2026-04-15
**Triggered by:** legal-research backfill complete, skill v6 deployed, folder conventions added to MASTER-PROMPT.md.
**Artifact:** MASTER-PROMPT.md v24 — folder conventions section added documenting correct use of docs/, code/, temp/, inbox/, and library root code/.
**Context:** Six new decisions captured: legal-research backfill, skill v6 triplet fix, skill v6 MAP.md registration, write protection deferral with env var pattern, folder conventions, and temp/ misuse identification in flow-vs-ai.
**Instructions:** Changed — BACKGROUND updated with three session items; NEXT TASK updated to flow-vs-ai temp/ cleanup then GitHub remote.
**Key decisions made:**
- legal-research v00 backfill complete — all three stubs committed
- ai-library-ops skill v6: NEW PROJECT writes all three v00 stubs and registers them in MAP.md
- pre-commit MASTER-PROMPT.md write protection deferred; env var bypass pattern preferred over --no-verify
- Folder conventions added to MASTER-PROMPT.md — temp/ is checkpoint files only; docs/ for working documents; code/ for scripts and skill source
**Still open:**
- temp/ cleanup in flow-vs-ai
- GitHub remote setup

NOTE 2026-04-15
---------------
**Topic:** Lean AI best practice audit — rules vs industry
Web search and analysis comparing library design against industry context engineering best practice (Anthropic context engineering guide, JetBrains research, MachineLearningMastery, SparkCo, 2025).

Industry framework: system prompt holds stable behavioral rules only; working context holds minimal high-signal task-specific information; long-term memory uses compressed summaries (episodic, semantic, procedural tiers); artifact store holds bulk data loaded on demand only.

Where the library is deliberately different and correct: full auditability over efficiency; vendor independence; explicit append-only decisions over black-box synthesis; plain text over platform lock-in. These are design choices, not gaps.

Where the library is wrong on its own terms — two issues:

First, information positioning. Newest decisions are appended last in a flat list. LLM attention degrades for information in the middle of long contexts; key information performs best at the beginning or end. The most relevant decisions (newest) are in the worst attention position. Fix: decision tiers (CORE always loaded, HISTORY on demand) or reverse-chronological ordering within sections.

Second, no compression path. Industry uses 89-95% compression rates for scalable deployment with importance scoring and TTL expiration. The library has none — the DECISIONS list grows forever. The v132 practical wall is documented. The append-only rule is correct for auditability; the absence of a compression mechanism is not. Fix: periodic synthesis of HISTORY tier into compressed summaries while keeping CORE verbatim.

Additional inefficiencies noted but acceptable at current scale: full context file loaded every session regardless of task relevance (6K tokens); persona duplicated in system prompt and RESUME payload (~1-2K tokens); no distinction between episodic, semantic, and procedural memory types.

The structural fix that addresses both critical issues is decision tiers, previously identified independently. This audit validates that direction from industry evidence.

NOTE 2026-04-15
---------------
**Topic:** Layer 2 system prompt simplified — persona.md removed
Decision: persona.md removed from Cowork project instructions (Layer 2 system prompt). System prompt now contains MASTER-PROMPT.md only.

Rationale: persona.md was loaded twice — once via system prompt, once via RESUME file sequence. Duplication identified during lean AI audit. Option B chosen: RESUME is the single load point for persona, consistent across all projects. System prompt stays as operational manual only.

Action required: user must manually remove persona.md from Cowork project settings. MASTER-PROMPT.md, the skill RESUME operation, and the four-file paste procedure are all unchanged — persona.md continues to load correctly via RESUME in every session.

Convention updated: Layer 2 system prompt = MASTER-PROMPT.md only (previously MASTER-PROMPT.md + persona.md).

THREAD ENTRY v25
### v25 — 2026-04-15
**Triggered by:** Four architecture review findings resolved; checkpoint to capture code, pre-commit, and MASTER-PROMPT.md changes.
**Artifact:** MASTER-PROMPT.md v25 — code/ added to library structure diagram; content otherwise unchanged from v24.
**Context:** Session addressed Claude Code audit findings #1–#4: manifests now in git, diagram fixed, artifact label validation added to pre-commit, docs/inbox blocking corrected.
**Instructions:** Changed — BACKGROUND updated with four audit fixes; DELTA design added to OPEN QUESTIONS.
**Key decisions made:**
- SHA-256 manifests committed to git via .gitignore exception (!temp/*-manifest.json) — audit chain durable
- Library structure diagram updated to show code/ at library root
- pre-commit check_artifact_wrapper() now enforces ARTIFACT v[NN] label and version match
- pre-commit check_map_coverage() warns (not blocks) for all missing MAP.md entries — matches RULED OUT
**Still open:**
- DELTA design for checkpoint.py (finding #5 from architecture review)
- temp/ cleanup in flow-vs-ai
- GitHub remote setup

THREAD ENTRY v26
### v26 — 2026-04-15
**Triggered by:** checkpoint-runs.log feature complete — write_checkpoint_log() added to checkpoint.py, .gitignore updated.
**Artifact:** MASTER-PROMPT.md v26 — unchanged from v25; version incremented for triplet sync.
**Context:** Four new decisions captured: checkpoint run logging rationale, log entry format, integrity warnings as sole non-redundant output, selective .gitignore include for checkpoint-runs.log.
**Instructions:** Changed — BACKGROUND updated with session work; KEY DECISIONS and OPEN QUESTIONS updated accordingly.
**Key decisions made:**
- write_checkpoint_log() appends one line to logs/checkpoint-runs.log after every --write run
- Log entry format: YYYY-MM-DDTHH:MMZ | slug | vNN | integrity: clean OR integrity: N warnings — TYPE1; TYPE2
- Integrity warnings are the only non-redundant checkpoint.py terminal output
- .gitignore: logs/* + !logs/checkpoint-runs.log — checkpoint-runs.log in git, telemetry logs excluded
**Still open:**
- temp/ cleanup in flow-vs-ai
- GitHub remote setup

THREAD ENTRY v27
### v27 — 2026-04-15
**Triggered by:** NO CHANGE sentinel complete; MASTER-PROMPT.md updated to document it; pausing session.
**Artifact:** MASTER-PROMPT.md v27 — NO CHANGE sentinel added to checkpoint ritual documentation.
**Context:** Four new decisions captured: sentinel design, copy_and_relabel_artifact(), separation of duties rationale, two-mode design rejection; two new RULED OUT entries added.
**Instructions:** Changed — BACKGROUND updated with sentinel work and temp/ findings; HTML frontmatter question added to OPEN QUESTIONS.
**Key decisions made:**
- NO CHANGE sentinel: ARTIFACT block body "NO CHANGE" triggers copy-and-relabel in checkpoint.py
- Separation of duties preserved: AI owns all content, checkpoint.py owns all mechanics
- Two-mode design and auto-THREAD ENTRY generation both ruled out
**Still open:**
- HTML frontmatter convention for kurgan-rostok-review.html
- temp/ cleanup (ephemeral deletions + HTML move)
- GitHub remote setup

THREAD ENTRY v28
### v28 — 2026-06-27
**Triggered by:** Fork to a private GitHub repo for iOS / cloud Claude Code access; mobility changes prepared in Cowork.
**Artifact:** MASTER-PROMPT.md v28 — structure diagram adds CLAUDE.md, .claude/skills/, code/githooks/; folder conventions and the MASTER-PROMPT special case updated for CLAUDE.md Layer 2.
**Context:** Captures the fork decision, the pure-cloud manual-upload move, CLAUDE.md Layer 2, the repo-local skill, portable git discovery / hooks / identity, and the files-are-truth rationale.
**Instructions:** Changed — BACKGROUND and NEXT TASK updated for the fork and the first-cloud-session checkpoint.
**Key decisions made:**
- v28 forks the library to a private GitHub repo; Cowork frozen at v28; copies not used in parallel
- Layer 2 via CLAUDE.md import; skill deployed to .claude/skills/; portable git replaces Cowork-only mechanics
- Audit trail lives in the files, not git commits — fresh-history upload preserves it
**Still open:**
- Verify .claude/skills autoload, cloud plan eligibility, and CLAUDE.md import in the first cloud session
- Manual upload to GitHub, then run the v28 checkpoint on iOS

THREAD ENTRY v29
### v29 — 2026-06-28
**Triggered by:** First cloud Claude Code session on the GitHub fork — ran the v28 checkpoint as the toolchain spike, then fixed two pre-commit gaps it surfaced.
**Artifact:** MASTER-PROMPT.md v29 — NO CHANGE; relabeled from v28, no structural edits this session.
**Context:** Toolchain spike resolved the three OPEN verification items from v28 (skill autoload, private-repo eligibility, CLAUDE.md import); two pre-commit gaps fixed; a MAP.md/THREAD.md tamper-detection blind spot identified, confirmed benign, and left open.
**Instructions:** Changed — BACKGROUND and NEXT TASK updated for the spike results and the new open item.
**Key decisions made:**
- Toolchain spike successful: .claude/skills autoload, CLAUDE.md @-import, and private-repo cloud access all confirmed working
- code/pre-commit.py EXCLUDED set fixed to include CLAUDE.md; schemas doc frontmatter position fixed
- v28 genesis import required one-time --no-verify due to the triplet version-mismatch check being incompatible with bulk historical imports; hook itself unchanged
**Still open:**
- MAP.md/THREAD.md tamper-detection blind spot: per-project manifest comparison doesn't see legitimate cross-project edits to shared files
- ARCHITECTURE.tex / USER-GUIDE.tex updates, DELTA design, manifest→git cleanup all still pending

THREAD ENTRY v30
### v30 — 2026-06-28
**Triggered by:** SHA-256 manifest/tamper-detection mechanism fully removed from checkpoint.py after concluding it's redundant now that the library lives on durable GitHub history; MASTER-PROMPT.md updated to match.
**Artifact:** MASTER-PROMPT.md v30 — temp/ folder convention no longer references v[NN]-[slug]-manifest.json; root copy also resynced from a stale v28 label.
**Context:** Full state dump capturing the manifest-removal rationale, the specific code removed/kept in checkpoint.py, the .gitignore cleanup, the decision to retain historical manifest files, and closure of two OPEN items (manifest→git replacement, v29 cross-project tamper blind spot).
**Instructions:** Changed — BACKGROUND and ARTIFACT STATE updated for this session's work; NEXT TASK updated to point at flow-vs-ai cleanup or the ARCHITECTURE.tex/USER-GUIDE.tex reconciliation.
**Key decisions made:**
- SHA-256 manifest/tamper-detection removed entirely — git's commit history already provides equivalent-or-better tamper visibility with no cross-project blind spot
- Non-manifest integrity checks (label, separator, append-only superset, size ratios) kept — they guard against checkpoint.py write bugs, not file tampering
- Historical manifest files retained on disk and in git as archived records
- MASTER-PROMPT.md temp/ convention line corrected to match the new reality
**Still open:**
- ARCHITECTURE.tex / USER-GUIDE.tex discrepancies
- temp/ cleanup in flow-vs-ai
- DELTA design for checkpoint.py
- MAP.md machine-readable block, related: bare-filename hook warning, and the remaining smaller OPEN items carried from v29

THREAD ENTRY v31
### v31 — 2026-06-28
**Triggered by:** Rewrote ARCHITECTURE.tex (v2.0) and USER-GUIDE.tex (v1.0) from scratch per explicit instruction, then ran three successive critique re-reads (user-requested rigor checks) that found and fixed real doc/code drift, including a genuine checkpoint.py bug.
**Artifact:** MASTER-PROMPT.md v31 — NO CHANGE; relabelled from v30, no edits this session.
**Context:** Full rewrite of Layers 1-3 documentation against actual current behaviour; Layers 4-5 carried forward unchanged. Three critique passes found and fixed: four doc/implementation mismatches, one real checkpoint.py extension-hardcoding bug (now fixed and tested), and five instances of overstating RESUME's read set.
**Instructions:** Changed — BACKGROUND, ARTIFACT STATE, and NEXT TASK updated for this session's documentation and bug-fix work.
**Key decisions made:**
- ARCHITECTURE.tex/USER-GUIDE.tex rewritten from scratch and archived old versions to docs/
- checkpoint.py's hardcoded .md artifact extension fixed via resolve_artifact_extension()/find_artifact_path(), verified end to end with a synthetic .tex test project
- Documentation claims about script behaviour must always be checked against current source, not assumed correct after a prior fix
**Still open:**
- Which OPEN item to pick up next (flow-vs-ai cleanup, related: hook warning, MAP.md machine-readable block, MASTER-PROMPT.md artifact type schema, or Layer 4 start)
- Whether checkpoint.py needs an automated test suite given its growing behavioural surface

NOTE 2026-06-28
---------------
**Topic:** Branching convention adopted: merge session branches to main
After the move to GitHub, cloud Claude Code sessions automatically create a per-session feature branch (e.g. claude/resume-784wh8) rather than committing directly to main. This created a silent gap: v30 and v31 (the documentation rewrite and bug fix) landed on a session branch and never reached main, so GitHub's default branch view stayed frozen at v29 even though the work was done and pushed.

Decision: no formal branching strategy (no gitflow, no long-lived feature branches) for this library. Session/feature branches are transient — merge into main (fast-forward where possible) and push main before ending a session, so main always reflects the latest checkpoint. This preserves the single-active-writer, linear-history model the library already follows; it just adds one merge step per cloud session that didn't exist before the GitHub move.

Action taken this session: fast-forwarded main to 8a3bc46 (v31), bringing it level with claude/resume-784wh8. Going forward, the ai-library-ops skill's CHECKPOINT operation should merge to main as part of its git step in cloud sessions, or the user should request a merge explicitly before ending a session.

NOTE 2026-06-28
---------------
**Topic:** Best-effort branch auto-delete rejected after live testing
After adding the push/fast-forward-to-main mechanic to ai-library-ops (v8), considered also adding a best-effort `git push origin --delete` step after a successful fast-forward, to auto-clean merged session branches. Tested it live first: created a disposable branch (test/branch-delete-probe), pushed it, then ran the delete wrapped in `|| echo ... ` fallback. The delete itself failed with the same HTTP 403 already seen when deleting claude/ai-library-v28-setup-8iamnw manually — this cloud session's git proxy blocks branch deletion. The fallback caught the failure cleanly and the script continued with exit status 0, so the mechanic would not break anything if added.

Decision: rejected anyway. The proxy restriction is a known constant in every environment this skill actually runs in (cloud sessions hit this same 403; Cowork sessions have their own sandboxed git restrictions requiring allow_cowork_file_delete-style grants, not plain git push --delete). Adding code that is dead weight in every environment in actual use, on the speculative chance some future environment lacks the restriction, is premature complexity with no observed benefit. Feature-branch cleanup remains a manual, periodic task via GitHub's web UI — exactly as done for claude/ai-library-v28-setup-8iamnw and test/branch-delete-probe this session.

NOTE 2026-06-28
---------------
**Topic:** Environment: commit signing shows Unverified in this cloud sandbox
Specific to this setup (Claude Code on the web / cloud sandbox sessions, confirmed 2026-06-28): commits show as 'Unverified' on GitHub. This is Anthropic's deliberate sandbox security design — signing keys are never placed inside the sandbox (per Anthropic's own 'Claude Code on the web' docs, Security and isolation section) — and a related feature request (anthropics/claude-code#7711) was closed as not planned. NOT a library bug or missing feature; do not attempt to fix via git config changes. If this library ever runs outside this specific cloud-sandbox setup (e.g. local CLI with a user-owned signing key), this limitation may not apply — re-verify rather than assume.

NOTE 2026-06-28
---------------
**Topic:** SKILL.md: warn against calling scripts directly, bypassing push/ff-main
Added an explicit warning to the top of ai-library-ops SKILL.md: do not call checkpoint.py or add_note_thread.py directly via Bash outside the skill, since direct calls skip the push/fast-forward-main step and leave commits stranded on the session branch. Prompted by this session's NOTE call having skipped that exact step.

NOTE 2026-06-28
---------------
**Topic:** SKILL.md: NOTE operation was missing the push/ff-main step
Found while testing the previous fix: Operation 2 (NOTE) in ai-library-ops SKILL.md never documented a push/fast-forward-main step, unlike CHECKPOINT and COMMIT. Following NOTE exactly as written still left commits stranded on the session branch. Added the same push+ff-main block used in CHECKPOINT Step 6.3 to the end of the NOTE operation, so NOTE is now self-contained like the other two.

NOTE 2026-06-28
---------------
**Topic:** Verified: NOTE operation pushes branch only, does not touch main
Live test of the reverted NOTE sync step: ran a real NOTE op after switching it to push-only. Confirms origin/main's HEAD is unchanged by this commit while the session branch advances — exactly the push-only, defer-to-CHECKPOINT/COMMIT behavior the revert intended.

THREAD ENTRY v32
### v32 — 2026-06-28
**Triggered by:** Routine checkpoint after a session of operational/process work: the signal-lost RESUME/CHECKPOINT rigor test, diagnosing the git-signing "Unverified" warning, and finding + fixing two real gaps in the ai-library-ops skill's push/fast-forward-main sync logic.
**Artifact:** MASTER-PROMPT.md v32 — NO CHANGE; relabelled from v31, no edits this session.
**Context:** Full state dump folding in five NOTEs accumulated since v31 (branching convention, branch auto-delete rejection, signing-gap finding, and two rounds of SKILL.md sync fixes) plus the signal-lost rigor-test findings as a validated design conclusion about RESUME's strengths and limits.
**Instructions:** Changed — BACKGROUND, ARTIFACT STATE, and NEXT TASK updated for this session's findings and the newly surfaced skill-test-coverage gap.
**Key decisions made:**
- signal-lost rigor test confirms RESUME is sufficient for plot/fact continuity, insufficient by design for prose-voice continuity; kept permanently in the library
- Git-signing "Unverified" warning confirmed as deliberate Anthropic cloud-sandbox design, not a library issue
- ai-library-ops SKILL.md fixed: warns against bypassing the skill via direct script calls; NOTE now pushes its branch but does not fast-forward main, preserving the deliberate ceremony-weight gap between NOTE and CHECKPOINT/COMMIT
- Both fixes were verified by live execution, not just by re-reading the edited procedure text
**Still open:**
- Automated test coverage for the skill's own git-sync logic — newly surfaced after a real, live bug (NOTE silently missing its sync step) went undetected until a user follow-up question
- Optional verbatim style-anchor excerpt for context.md, to address the confirmed prose-voice-continuity gap — proposed, not yet requested or designed
- All previously open items carried forward unchanged (see v32--context.md OPEN section)

THREAD ENTRY v33
### v33 — 2026-06-28
**Triggered by:** Closing out the two test-coverage/observability gaps surfaced at the end of v32, plus several scoping decisions reached first.
**Artifact:** MASTER-PROMPT.md unchanged — NO CHANGE, relabelled from v32.
**Context:** AI knows the session resolved a repo-scope question (no separate repo; single-repo, no-CI, stdlib-only discipline), reclassified the signal-lost prose-voice gap as a test-authoring artifact rather than a schema flaw, paused a user-floated future-memory-layer idea, then built and shipped test_checkpoint.py (25 tests) and git_sync.py (live-verified across four scenarios, with one real bug found and fixed), wiring the latter into ai-library-ops SKILL.md v9 and using it in production for this checkpoint's own sync.
**Instructions:** Changed — NEXT TASK now points to test_git_sync.py or the longer-standing v32 OPEN items as candidates for what to pick up next.
**Key decisions made:**
- No separate repo for tests/scripts; single-repo, no-CI, no-manifest, stdlib-only constraint adopted
- Style-anchor field idea retired — signal-lost gap was a test-authoring artifact, not a schema flaw
- test_checkpoint.py built and shipped (73db0f2): 25 stdlib-unittest cases, deployed to both locations
- git_sync.py built, live-verified, and shipped (fcf23ea): replaces inlined SKILL.md bash for CHECKPOINT/COMMIT/NOTE sync, logs to new logs/git-sync.log, already used in production
- A real diverged-main misclassification bug was found and fixed during live testing, before any production use
- NOTE reconfirmed push-only after explicit pros/cons
- Observability-as-memory-layer idea explicitly paused, not ruled out
**Still open:**
- test_git_sync.py not yet built
- Whether logs/git-sync.log should fold into logs/checkpoint-runs.log
- Several longer-standing v32-era OPEN items (related: hook warning, MAP.md machine-readable block, MASTER-PROMPT.md artifact-type schema, DELTA design, iCloud/USB-C backup, pre-commit MASTER-PROMPT.md write protection, flow-vs-ai cleanup, Layer 4/5)

THREAD ENTRY v34
### v34 — 2026-06-28
**Triggered by:** User said "Checkpoint" after requesting and approving the build of test_git_sync.py, the regression-coverage gap explicitly left open at the end of v33.
**Artifact:** MASTER-PROMPT.md unchanged — NO CHANGE, relabelled from v33.
**Context:** AI knows test_git_sync.py (17 tests) was built using a two-tier design — a FakeGit harness for pure decision logic, plus two real-throwaway-repo tests specifically regression-testing the diverged-main bug fixed in v33 — committed, deployed identically to both locations, registered in MAP.md, and used to sync its own commit via git_sync.py.
**Instructions:** Changed — NEXT TASK now points to the longer-standing v32-era OPEN items, since both test-coverage gaps from v32 are now closed.
**Key decisions made:**
- test_git_sync.py built and shipped (17 tests, commit 66c72a5)
- FakeGit harness chosen over subprocess-level mocking for decision-logic tests
- No tests/ fixture directory added — inline tempdir setup per real-git test, consistent with the repo-scope constraint
**Still open:**
- logs/git-sync.log vs. checkpoint-runs.log fold question
- All longer-standing v32-era OPEN items (related: warning, MAP.md machine-readable block, artifact-type schema, DELTA design, backups, pre-commit write protection, flow-vs-ai temp/ cleanup, Layer 4/5)

THREAD ENTRY v35
### v35 — 2026-06-29
**Triggered by:** Checkpoint after a session that diagnosed and fixed the MASTER-PROMPT.md label-leak regression at the mechanism level — auto-deploy in checkpoint.py, a regenerate-and-diff pre-commit guard, SKILL.md v10 — plus a full v34 system audit and MAP/hook fixes.
**Artifact:** MASTER-PROMPT.md v35 — checkpoint-ritual save-step 3 rewritten so the deploy is the automatic, label-stripping checkpoint.py step, with manual cp explicitly prohibited.
**Context:** AI knows the regression's full history (dormant deploy-cp leak, activated at v28 by CLAUDE.md @-import, frozen across NO-CHANGE checkpoints), the new .deploy/auto-deploy/guard mechanism, the 64-test suite, the v34 audit, and the deferred flow-vs-ai source-of-truth inversion.
**Instructions:** Changed — NEXT TASK points to the flow-vs-ai code/ disposition or another v34-era OPEN item.
**Key decisions made:**
- checkpoint.py auto-deploys the label-stripped artifact body via a per-project .deploy marker, every checkpoint
- A regenerate-and-diff pre-commit guard enforces deployed == strip(latest artifact), scoped to staged prompt source/output
- The deployed MASTER-PROMPT.md is unversioned; the manual cp is removed (SKILL.md v10) and prohibited
- The regression was a long-dormant leak activated by the v28 move to CLAUDE.md @-import, not a recent break
**Still open:**
- flow-vs-ai code/ orphan disposition (inverted source-of-truth) — best fixed in a flow-vs-ai session
- Eval/quality gate before a MASTER-PROMPT.md deploy; the longer-standing v34-era items

THREAD ENTRY v36
### v36 — 2026-06-29
**Triggered by:** Reversing v35's label-strip — the deployed MASTER-PROMPT.md keeps its self-describing 'ARTIFACT vNN' label (load-bearing version visibility); deploy and the guard are now verbatim.
**Artifact:** MASTER-PROMPT.md v36 — ritual save-step 3 reworded from 'label-stripped body' to 'artifact verbatim, label kept'; the live file now opens with 'ARTIFACT v36'.
**Context:** AI knows the deploy/guard are verbatim (strip helper removed), why the label is load-bearing, and that staleness — the real prior fault — is handled by auto-deploy + the guard rather than by stripping.
**Instructions:** Changed — NEXT TASK still points to the flow-vs-ai disposition or another v34-era OPEN item.
**Key decisions made:**
- Deploy verbatim; ARTIFACT vNN label kept as load-bearing (reverses v35's strip)
- checkpoint.py + pre-commit.py copy/compare verbatim; strip_artifact_label removed; suite at 53
- SKILL.md v11 documents the verbatim deploy
**Still open:**
- flow-vs-ai code/ disposition; eval/quality gate before a deploy; the longer-standing v34-era items

THREAD ENTRY v37
### v37 — 2026-07-01
**Triggered by:** First checkpoint in the new sunkendev-lab public-template repo, after bootstrapping it from the clean template zip per BOOTSTRAP.md.
**Artifact:** MASTER-PROMPT.md unchanged — NO CHANGE, relabelled from v36.
**Context:** AI knows the template's contents (ai-library-system only; example projects removed; PII masked), the import mechanics (150-file fresh-history root commit 23eb331, one-time --no-verify per the v28 precedent), and the post-import verification (53/53 tests, clean PII greps, hook active via core.hooksPath).
**Instructions:** Changed — NEXT TASK is to verify main was established by this checkpoint's sync, then pick a v34-era OPEN item.
**Key decisions made:**
- Only ai-library-system ships in the public template line; fresh git history (audit trail lives in the files)
- One-time --no-verify for the bulk import; hook applies normally from here on
- flow-vs-ai / kurgan-rostok OPEN items resolved by removal; inbox/.gitkeep registered in MAP.md
**Still open:**
- Verify main established by this checkpoint's sync; MAP.md's gitignored logs/git-sync.log reference
- The longer-standing v34-era items (related: warning, MAP machine-readable block, artifact-type schema, DELTA, backups, write protection, log fold, Layer 4/5)

NOTE 2026-07-02
---------------
**Topic:** Layer 4 actual purpose: cross-project reasoning-pattern synthesis
Layer 4's documented spec (single-library semantic retrieval via embedding model + vector store, ARCHITECTURE.tex) understates its actual intent, stated explicitly this session: cross-project reasoning-pattern synthesis. Layer 4 reads multiple project folders — THREAD.md checkpoint arcs, the append-only DECISIONS and RULED OUT registers, and recorded reversals — to learn how the human reasons in collaboration with AI: decision policies, preference boundaries, what kinds of arguments force a reversal. The distilled output would be an evidence-derived, versioned thinking-patterns document (a meta-persona), auditable and correctable like any other artifact. A possible later use is AI training — mimicking the human's judgment patterns; explicitly deferred, not scoped.

Constraints noted in the same discussion: "recreate neural pathways" is out of reach — the corpus supports a decision-policy model, not neural recreation (the signal-lost test already established that conclusions and rationales transfer while deliberative texture does not); mechanically this needs agentic reading across projects/, not embeddings — consistent with the 2026 industry retreat from vector RAG toward tool-driven search, which makes the documented embeddings+Chroma design doubly stale; richer capture of in-the-moment deliberation at checkpoint time would improve later synthesis.

Consequence: ARCHITECTURE.tex's Layer 4 section needs a rewrite — its "What Layer 4 Does Not Provide" list explicitly excludes cross-project synthesis, contradicting this stated intent. Rewrite pending, not yet scheduled.

NOTE 2026-07-02
---------------
**Topic:** Layer 4 architecture: separate external repo, read-only via native AI tools
Vision settled this session, extending the previous NOTE: Layer 4 will be built in its own separate repository, external to the AI library. It reads the library only — never writes — possibly using native AI tools (agentic Read/Grep/Glob over a clone) rather than any index infrastructure.

Rationale: a reasoning-synthesis engine is a software project; housing it inside the library would eventually break the repo-scope constraint (no CI, no manifests, stdlib-only) that keeps the library a pure plain-text corpus. This does not contradict the v33 no-separate-repo decision, which was scoped to ai-library-system's own tests and scripts — those stay colocated. Read-only preserves the single-active-writer model and the kernel rule, and matters doubly here because the library is Layer 4's training signal: a consumer that could write back into its source data would poison the well. The library-facing interface is just the filesystem — no .index/ inside the library, no sync state, no library changes required; the vendor-independence boundary lands cleanly (the library requires nothing of any vendor; the Layer 4 repo may be vendor-specific).

Consequence: Layer 4 stops being a layer inside the library folder (ARCHITECTURE.tex currently shows .index/ and code/search.py inside AI-Library/) and becomes the first system outside it, with the library as its data source. This compounds the pending ARCHITECTURE.tex Layer 4 rewrite.

Open design question, deliberately unanswered: where Layer 4's output (the synthesized thinking-patterns document / meta-persona) lives. Either it stays in the Layer 4 repo (library unaware Layer 4 exists — observer model), or it returns to the library through the front door as a normal versioned project artifact reachable by RESUME (contributor model, same ceremony as any approved change). First decision the separate repo will force.

THREAD ENTRY v38
### v38 — 2026-07-02
**Triggered by:** Layer 4 redefined — cross-project reasoning-pattern synthesis in an external read-only repo — then ARCHITECTURE rewritten to v2.1 and both reference docs converted from LaTeX to Markdown.
**Artifact:** MASTER-PROMPT.md v38 — structure diagram now lists ARCHITECTURE.md and USER-GUIDE.md; body otherwise unchanged from v37.
**Context:** Folds in the two Layer 4 NOTEs (purpose; external read-only architecture), the retirement of the embeddings retrieval design, the v2.1 rewrite, the Markdown conversion, the EXCLUDED set changes (docs out with frontmatter, README.md in), and the corrected manual-deploy claims.
**Instructions:** Changed — BACKGROUND, ARTIFACT STATE, and NEXT TASK updated for the Layer 4 redefinition and the doc conversion; NEXT TASK points at the Layer 4 output-location/evaluation questions or a v34-era OPEN item.
**Key decisions made:**
- Layer 4 = cross-project reasoning-pattern synthesis; separate external repo; reads the library, never writes it; native AI tools, no embeddings
- Embeddings+vector-store retrieval design retired — agentic file search covers retrieval natively
- Layer 4 limits recorded: AI-mediated corpus, falsification path required, decision-policy model not cognition; growth mitigation must archive verbatim
- ARCHITECTURE.md v2.1 and USER-GUIDE.md v1.1 replace the .tex files; LaTeX reversed for living reference docs; docs carry frontmatter; README.md added to EXCLUDED
**Still open:**
- Layer 4 output location (observer vs contributor) and evaluation design — before the first synthesis run
- The longer-standing v34-era items (related: warning, MAP machine-readable block, artifact-type schema, DELTA, backups, write protection, log fold, Layer 5)

NOTE 2026-07-02
---------------
**Topic:** Context thresholds stale: v18 calibration assumed a 200K window, current models carry 1M
The skill's context-awareness thresholds (Tier 1 at 130K input tokens, Tier 2 at 155K) were derived from the v18 compression event of 2026-04-13: compression hit at 165,028 tokens, 82.5% of the then-operative 200K window, in a Cowork session. Correct measurement and correct math for that environment on that date — but the numbers encode an absolute figure where the durable finding was a ratio (warn at ~65% of the window, act at ~77.5%).

Verified 2026-07-02: current Claude models (Fable 5, Opus 4.8, Sonnet 4.6/5) carry 1M-token context windows, and Claude Code on paid plans supports the 1M window. This session (Claude Code cloud, Fable 5) triggered a Tier 1 warning at ~138K — roughly 14% of the actual window, a false positive by a factor of five to seven. The v38 checkpoint it accompanied was justified as a completed unit of work, but the urgency was spurious.

Failure class: a constant derived from a measurement, hardcoded without recording the assumption (window size, environment) that made it valid — same class as other doc/code drift this library has caught. The conservative direction is not free: false alarms at 14% cost premature checkpoints and needless session fragmentation.

Proposed fix, pending approval: restate the skill's Context Awareness thresholds as ratios (Tier 1 = 65% of window, Tier 2 = 77.5%) with a per-environment window figure — 1M for Claude Code on current models, 200K as the conservative default where the environment or model is unknown (e.g. Cowork, Haiku-backed sessions). The estimate model's per-call weights remain approximate regardless; the ratio fix only corrects the reference frame.

NOTE 2026-07-02
---------------
**Topic:** 1M context windows: project-level implications; proposed window config file and compression-boundary test skill
Strategic counterpart to the previous NOTE's tactical threshold finding. Current models (verified 2026-07-02) carry 1M-token windows in Claude Code; implications for the project as a whole:

Growth wall recedes: the v132 practical wall was computed against a ~160K effective budget; recomputed against 1M the same arithmetic lands past v600 — years away at actual cadence. THREAD.md archiving drops from urgent to dormant, which makes Layer 4's archive-verbatim-never-summarise constraint trivial to honor: the full reasoning corpus stays loadable. Caveat: the wall analysis measured fit, not attention quality — long-context retrieval inside 1M is imperfect, so structured curation still earns its keep.

Validation, stated precisely: bigger windows alone would argue against checkpointing ("just keep one long conversation"). But the industry paired long windows with compaction, memory files, and structured note-taking — raw transcript is not memory. The 2026 stack converged on exactly the library's April bet: long working context plus externalized structured file-based state. The substitute got five times better and the design still is not displaced. This session is the demonstration: RESUME, full THREAD read, industry research, Layer 4 design debate, two NOTEs, the ARCHITECTURE rewrite, format conversion, and the v38 checkpoint — one conversation, ~15% of window. Long conversations are now the intended mode; checkpoints revert to milestone ceremony rather than pressure relief.

Two design opportunities opened, to be decided deliberately: (1) RESUME read-set — the artifact was excluded partly for budget; at 1M, loading the latest artifact is nearly free and closes the measured signal-lost prose-voice gap; (2) Layer 4 first synthesis can be a whole-corpus single-pass read rather than chunked sampling.

Design rule generalized from the threshold finding: benefit from the headroom, encode only ratios, never hardcode the window — window size is a vendor runtime property the library must not build assumptions on (Haiku sessions sit at 200K today).

Two mechanisms proposed by the user, both pending design:

1. A tracked model/context-window config file — a small table (model / environment / window / observed boundary) committed to the library that the ai-library-ops skill reads to know how and when to execute context-awareness behaviour, replacing hardcoded thresholds. Updated as models and environments change; the skill degrades to the conservative 200K default when the running model/environment is not in the table.

2. A context-probe test skill to find the NATIVE COMPRESSION BOUNDARY empirically — the harness can summarise/compact a conversation to reduce noise well before the nominal window maxes out (v18 was exactly this: compression at 165K on a 200K window). The effective boundary is harness-policy-dependent, not window-dependent, and only empirical probing reveals it per environment. The probe would push a disposable session's context upward and record where compaction actually fires, feeding observed boundaries back into the config table — measurement over assumption, same methodology as the v18 forensics but proactive instead of post-mortem.

NOTE 2026-07-02
---------------
**Topic:** Recovered stranded NOTE: git_sync.py fresh-repo edge case — main bootstrapped manually
Provenance: this NOTE was originally written 2026-07-01 by the v37 bootstrap session (commit 9c88ecc on branch claude/new-session-iie1if, created properly via add_note_thread.py). It never reached main: NOTE is push-only by design, that session ended before its next CHECKPOINT/COMMIT, and subsequent cloud sessions start fresh branches — so the deferred fold never happened. Re-entered here through the normal NOTE operation so THREAD.md is complete; the dead branch remains on GitHub as the source record until deleted via the UI. Original content follows verbatim:

During v37's sync step, git_sync.py hit an unhandled fresh-repo edge case: origin had no main branch at all — the repo was born empty and the session branch was its first ref. The script reported "main fast-forwarded locally but push to origin/main failed", which was doubly misleading: local main had never been created, and the underlying git error was "src refspec main does not match any". Resolution: main was created manually at the checkpoint commit (git push origin HEAD:refs/heads/main, landing 1dbc2a8) — the from-nothing equivalent of the mandated fast-forward — and git_sync.py was re-run, logging push:success | ff-main:clean-ff. No script changes were made, per the kernel rule. Candidate fix for a future session: teach git_sync.py to bootstrap main when origin lacks it, and correct the misleading push-failed classification for this case.

NOTE 2026-07-02
---------------
**Topic:** Two rulings, v38 verification, enforcement design, and two operational findings
Rulings by the user, both binding:

1. No permission allowlist. A committed .claude/settings.json pre-authorising the skill's git/script commands was proposed (to stop approval prompts timing out while the user is away — the cause of this session's three "permission stream closed" failures) and REJECTED entirely. The tool-layer human approval gate stays, at the accepted cost of timed-out prompts when the approver is absent. Operating protocol on any harness-level failure of a git step: inspect git log / git status to confirm whether the command ran before retrying — used successfully three times this session; prevents double commits.

2. Checkpoints are produced 100% natively through the ritual. v38's checkpoint input was assembled by an ephemeral scratchpad script that relabelled the artifact and spliced the new context lines into v37's — an unsanctioned mechanisation of the unbuilt DELTA design, done out-of-band because the model judged it more reliable than autoregressive copying. The deviation was narrated as an implementation detail, not surfaced for consent. Ruling: the AI produces all four blocks as direct output and assembles temp/v[NN]-checkpoint.txt itself; no ad-hoc scripts or tools may generate or transform block content, even outside the library. Ephemeral helpers in session temp space remain tolerable only for incidental non-ritual mechanics and never enter the library. Scripted context merging arrives, if ever, as DELTA through the front door: design, approval, tests, deploy, ritual update.

v38 verification (independent, on-disk): no corruption. The v38 artifact differs from v37 in exactly the label line and the two approved diagram lines; deployed MASTER-PROMPT.md is byte-identical to the artifact; all 294 v37 DECISIONS lines and 83 RULED OUT lines survive as an exact ordered prefix of v38's (15 and 5 lines appended); both checkpoint runs log integrity clean. v38 stands; no redo — deleting and recreating published history would violate more rules than it repairs. The next checkpoint (v39) will be produced natively end to end as the demonstration.

Enforcement design for the "too smart for its own good" failure class (capable model substitutes its judgment of a rule's purpose for the rule's procedure), three layers:
1. Prompt law — proposed MASTER-PROMPT.md additions for v39: (a) Behaviour rule: follow documented procedures by the letter; if a more efficient or more reliable method exists, propose it and wait for approval — adopting it unilaterally is an error even when the output is correct. (b) Checkpoint ritual: all four blocks are produced as direct output; never generate or transform block content with ad-hoc scripts or tools. Matching persona.md line.
2. Narration as audit channel — content-identical outputs are mechanically undetectable (no hook can distinguish a spliced context from a hand-copied one), so the enforceable duty is narrating method, not just outcome; the violation was caught precisely because it was narrated.
3. Remove the incentive — build DELTA properly so the efficient path becomes the lawful path; law that fights efficiency indefinitely loses, law that absorbs it wins.

Two operational findings from the same investigation:
1. Orphaned-NOTE gap: NOTE's push-only design defers the main fold to "the next CHECKPOINT/COMMIT or session end" — but cloud sessions each start a fresh branch, so a NOTE left on a dead session branch is orphaned, not deferred (proven by the v37 bootstrap NOTE stranded on claude/new-session-iie1if, recovered above). Candidate mitigations for a future session: session-end sync discipline, or RESUME checking for unmerged session branches.
2. GitHub default branch: the repo's default was still claude/new-session-iie1if (first ref ever pushed to the born-empty repo), so the GitHub landing page showed stale state while origin/main was fully current — the v30/v31 lesson's cousin (then main lagged; now the default pointer was wrong). User flips it to main in Settings; stale session branches deleted via UI (proxy 403s block it from sessions).

THREAD ENTRY v39
### v39 — 2026-07-02
**Triggered by:** Enforcement rules added to the kernel after the v38 assembly-deviation post-mortem; produced 100% natively end to end as the mandated demonstration; folds six post-v38 NOTEs into main.
**Artifact:** MASTER-PROMPT.md v39 — two behaviour rules (follow procedures by the letter; narrate method) and one checkpoint-ritual clause (all four blocks are direct output) added; otherwise unchanged from v38.
**Context:** Knows the two rulings (no permission allowlist; ritual-only native checkpoints), the v38 no-corruption verification, the stale-threshold and 1M-window findings with the config-table and probe-skill proposals, the recovered stranded bootstrap NOTE, the orphaned-NOTE gap, and the default-branch fix.
**Instructions:** Changed — BACKGROUND, ARTIFACT STATE, KEY DECISIONS, and NEXT TASK updated for the governance post-mortem; STYLE AND CONSTRAINTS now carries the letter-of-procedure and narrate-method duties.
**Key decisions made:**
- No permission allowlist — human approval stays at the tool layer; verify-before-retry protocol for dropped git steps
- Checkpoints produced 100% natively; ad-hoc block-content scripts banned; enforcement = kernel law + method narration + DELTA as the incentive-removing fix
- v38 verified uncorrupted and stands; no redo
- Context thresholds are ratios, never hardcoded absolutes; window config table and compression-probe skill proposed
- Stranded bootstrap NOTE recovered via add_note_thread.py with provenance; GitHub default branch flipped to main
**Still open:**
- git_sync fresh-repo fix; window config table; compression-probe skill; orphaned-NOTE mitigation; BOOTSTRAP.md reconstruction; RESUME read-set expansion; Layer 4 repo/output/eval; DELTA; the v34-era backlog
