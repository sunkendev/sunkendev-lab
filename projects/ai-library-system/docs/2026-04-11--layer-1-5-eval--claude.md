---
title: Five-Layer Evaluation Report
date: 2026-04-11
updated: 2026-04-11
type: document
vendor: claude
model: claude-sonnet-4-6
tags: [evaluation, layer-1, layer-2, layer-3, layer-4, layer-5]
related: [ARCHITECTURE.tex, MASTER-PROMPT.md, 2026-04-11--claude-code-eval--claude.md]
---

I have all the material I need. Here is the full evaluation.

---

## AI Document Library System — Five-Layer Evaluation

---

### LAYER 1 — Foundation

**Working**

The folder structure matches the MASTER-PROMPT.md schema exactly, including the `code/` correction captured in the THREAD.md NOTE. All seven versioned triplets (v01–v07) are complete and present. File naming is consistent across every file in the library. Standalone docs all carry complete, valid YAML frontmatter. THREAD.md is well-formed and strictly ascending (v01–v07, then three NOTEs in correct format). MAP.md accurately represents all committed files. The pre-commit hook matches the documented validation rules across all six check functions.

**Incomplete**

One file exists on disk that is neither in MAP.md nor in the worktree: `projects/ai-library-system/docs/2026-04-11--claude-code-eval--claude.md` — the prompt used to trigger this session. It has no YAML frontmatter. If staged, the pre-commit hook would block the commit on a missing frontmatter error. It is currently invisible to the library system.

ARCHITECTURE.tex still shows the old folder diagram with `docs/`, `research/`, `creative/` at root and `scripts/` as the deployment folder name. This is a known open item but it creates a genuine divergence between the reference document and the live system.

**At risk**

The `scripts/` → `code/` rename is documented only in THREAD.md notes and context files. Any reader of ARCHITECTURE.tex alone — including a future AI resuming work from that document — will build an incorrect mental model of the folder layout.

The `related:` field in standalone docs contains bare filenames (`layer-1-foundation.md`, not `projects/ai-library-system/docs/2026-04-11--layer-1-foundation--claude.md`). The schemas doc references `layer-1-foundation.md` which has already been renamed. Dead links accumulate silently — the pre-commit hook has no `related:` field validation.

**Recommendation**

Add frontmatter to `2026-04-11--claude-code-eval--claude.md` and add it to MAP.md before the next commit. It's a significant document — the first external evaluation of the system — and leaving it unregistered breaks the completeness invariant MAP.md is supposed to provide. Standardise `related:` field values to full relative paths from library root, and add a path-existence check for `related:` entries to the pre-commit hook (warn only, same as MAP.md integrity).

---

### LAYER 2 — Session

**Working**

The design is complete, internally consistent, and well-reasoned. The separation between static system prompt content (MASTER-PROMPT.md, persona.md) and dynamic session content (RESUME files) is correct. The warning against treating platform memory as permanent is exactly right and placed where a user will encounter it at implementation time. The relationship table between Layer 1 and Layer 2 is accurate and honest about what Layer 2 does not provide.

**Incomplete**

The Layer 2 platform experiment has not been run. The design is untested against actual platform behaviour — specifically whether a system prompt containing both MASTER-PROMPT.md and persona.md actually performs as documented when an AI receives all four RESUME files pasted on top of it.

**At risk**

There is an inconsistency between ARCHITECTURE.tex and the Layer 2 reference doc. ARCHITECTURE.tex describes Layer 2 session start as requiring only the instructions file pasted (5 steps total). The Layer 2 doc correctly requires all four RESUME files (6 steps). An implementer reading ARCHITECTURE.tex would set up a materially different and weaker workflow. The explanation for why all four files are still required — that system prompt content is not guaranteed to be treated as active working context by the AI — is not in ARCHITECTURE.tex and needs to be.

A secondary tension: Layer 2 places persona.md in the system prompt AND requires it to be pasted again via RESUME. If the system prompt version and the pasted version diverge (persona.md is updated but the workspace system prompt is not), the AI will receive two conflicting personas. There is no mechanism that detects this drift.

**Recommendation**

Before running the platform experiment, update ARCHITECTURE.tex Layer 2 section to match the Layer 2 reference doc's session start procedure. Specifically add the "why" for the continued four-file RESUME requirement: system prompt is background, not active context. This is a one-paragraph fix and it closes a real implementation risk for anyone following ARCHITECTURE.tex.

---

### LAYER 3 — Automation

**Highest-value script to build first**

Not `checkpoint.py` as currently designed. The highest-value first script is a file-input extractor: takes a path to a text file containing checkpoint output, parses the four labeled blocks, validates they are present and version-consistent, and saves them to correctly named files in the correct project folder. This addresses the actual bottleneck (save-and-name work after a checkpoint) without the fragility of clipboard mode. Clipboard should be secondary input — the default should be file path.

**Risks in the checkpoint.py design**

The documented step 10 ("Update the THREAD.md header (latest checkpoint: v[NN])") describes a field that does not exist in the THREAD.md schema. THREAD.md has a status field (`active | paused | complete | archived`), not a `latest checkpoint:` header. A script implementing this step as written would corrupt the file. Step 11 ("Insert new row at top of Recent table" in MAP.md) refers to a Recent table that the current MAP.md schema does not have. Both steps are artifacts of an earlier design that was superseded.

The artifact extension determination (step 5: "Determine the artifact file extension from the content type") has no specified mechanism. The block content does not encode file type. The script would need either heuristics or a user-supplied argument. Heuristics are wrong often enough to cause problems silently.

There is no rollback design. If the script saves the artifact successfully then crashes before saving the context file, the project folder is in a state the pre-commit hook will block but the script has no awareness of. A partial checkpoint is worse than no checkpoint.

**Most robust input/output design for this workflow**

Input: a required positional argument for a text file path. The user saves the AI's full checkpoint output to a timestamped file before running the script. This file is inspectable, reproducible, and can be re-run without re-running the AI session. Clipboard mode is an optional flag, not the default.

Output: a dry-run mode (`--dry-run`) that prints what would be saved and where, without writing any files, as the default. Actual write requires `--write`. Confirmation printout after write lists all four files saved with paths and sizes. No THREAD.md header modification. No MAP.md table manipulation beyond appending a new entry in the correct section.

**Recommendation**

Remove steps 10 (THREAD.md header update) and 11 (MAP.md Recent table) from the checkpoint.py design in ARCHITECTURE.tex. They describe schema elements that were eliminated. Replace them with: "Append THREAD ENTRY block to THREAD.md" (already step 9) and "Add new MAP.md entries for the three new files in the correct section." Add a note in ARCHITECTURE.tex that the script requires the artifact extension to be passed as an argument or inferred from a mapping in the instructions file.

---

### LAYER 4 — Retrieval

**Library structure compatibility**

The standalone file structure is well-suited for embedding: consistent frontmatter provides structured metadata, vendor and type fields enable filtered search, date fields support temporal range queries, and the content of context and instructions files is semantically rich and purposeful.

The project file structure is poorly suited. All 21 versioned triplet files (v01–v07 × 3) carry no frontmatter and no structured metadata. An indexer must infer project name, date, and type from the file path alone. Type is determinable (`context.md`, `instructions.md`, `artifact.*`) but date and tags are not. Project files are likely the most valuable retrieval targets — context files are precisely the dense, decision-rich documents a semantic search should return — but they will index without metadata.

**Layer 1 decisions that most affect Layer 4 quality**

The most consequential is the deliberate absence of frontmatter from project files. This was the right call for Layer 1 (project files are managed by the versioning system, not by document metadata) but it creates a structural gap for Layer 4. The second is the `related:` field using bare filenames instead of relative paths — this will make link resolution in a retrieval-augmented session unreliable.

Chunking strategy will matter significantly. THREAD.md files contain checkpoint summaries, notes, and version identifiers. A single-document embedding of THREAD.md captures everything but will return THREAD.md for almost any project-related query, making it low-precision. Chunk-level indexing by section (one chunk per THREAD.md entry) is essential.

**Recommendation**

Before implementing Layer 4, define a lightweight metadata header convention for project files — not YAML frontmatter (that would violate the schema) but a parseable structured comment at the top of context and instructions files, e.g. a single comment line `<!-- project: ai-library-system | version: v07 | type: context | date: 2026-04-11 -->`. This gives the indexer structured metadata without changing the schema. 21 files need updating now; 210 files would need it later. The cost is low; the retrieval precision gain is significant.

---

### LAYER 5 — Orchestration

**Foundation assessment**

The Layer 1 foundation is largely solid enough to support the Layer 5 design, with three specific corrections needed before implementation begins.

The consistent folder structure is critical for MCP navigation — it is achieved and stable. THREAD.md as navigable project narrative is present, ascending, and informative. MAP.md as traversal index is operational. Git history is clean. The exclusion of platform lock-in is built into the philosophy and never compromised.

**Specific risks**

The `.mcp-config.json` example in ARCHITECTURE.tex lists `allowed_write_paths` including `docs/`, `research/`, and `creative/` — folders that do not exist and were explicitly eliminated from the design. An MCP agent following this configuration would behave incorrectly on write operations that should be valid (writing to `projects/ai-library-system/docs/`). The correct write paths are `projects/*/docs/`, `projects/*/code/`, and `inbox/`.

MAP.md is not machine-readable. The current format is human-friendly markdown. An MCP agent parsing MAP.md to locate projects and files must parse prose, headers, and markdown links without any structural guarantee. The v01 context file noted "MAP.md machine-readable section for Layer 4 efficiency" as an open question — it was never implemented. At Layer 5, this becomes a reliability issue for agent traversal, not just a performance question.

The crontab example (`0 8 * * 0 /path/to/AI-Library/scripts/weekly-synthesis.py`) hardcodes the library path and uses the old `scripts/` folder name. The library is in iCloud at a path that includes a space and may change across machine migrations. A hardcoded crontab path is fragile in this environment.

**Recommendation**

Before Layer 5, add a machine-readable project index to MAP.md — a fenced YAML or JSON block at the top of the file that lists each project with its folder path, status, and latest checkpoint version. This block is ignored by human readers but gives MCP agents and scheduled scripts a reliable traversal entry point without needing to parse markdown. Human-readable sections below it remain unchanged. This single addition decouples agent navigation from the human-readable format and is a prerequisite for any reliable Layer 5 automation.

---

### Summary table

| Layer | Status | Primary gap | Priority action |
|---|---|---|---|
| 1 | Operational | `claude-code-eval` doc unregistered; `related:` fields use bare names | Add frontmatter + MAP entry; fix `related:` paths |
| 2 | Designed, untested | ARCHITECTURE.tex session start is wrong | Update ARCHITECTURE.tex before running experiment |
| 3 | Not built | Steps 10–11 reference eliminated schema elements | Revise design before writing code |
| 4 | Not built | Project files have no metadata for indexer | Define lightweight project file metadata convention now |
| 5 | Not built | MAP.md not machine-readable; MCP config paths stale | Add machine-readable index block to MAP.md |
