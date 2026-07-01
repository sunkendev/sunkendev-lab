---
title: AI Library Architecture & Code Review
date: 2026-04-15
updated: 2026-04-15
type: document
vendor: claude
model: claude-sonnet-4-6
tags: [architecture, code-review, pre-commit, checkpoint, master-prompt]
related: [2026-04-13--v18-compression-forensics--claude.md, 2026-04-13--thread-growth-analysis--claude.md]
---

# AI Library: Architecture & Code Review

Conducted by Claude Code (claude-sonnet-4-6), 2026-04-15.
Read-only audit. No files created or modified by the evaluator.
Scope: full architecture and code review across five areas.

---

## 1. ARCHITECTURE

### Five-layer coherence

The five-layer stack holds conceptually. Layers 1–3 are implemented; 4–5 are
explicitly deferred. The separation is clean: Layer 1 is file-level structure,
Layer 2 is AI session control, Layer 3 is automation. No cross-layer coupling
violations found.

### Gaps between MASTER-PROMPT.md and scripts

[MAJOR] — `code/` at library root is completely absent from the library
structure diagram in MASTER-PROMPT.md (lines 18–36). The folder conventions
section (line 64) documents it correctly, but an AI reading the diagram first
— which is the document's primary orientation aid — has no path to discover
where deployed scripts live. Any session where the AI needs to reason about the
library layout will start with a wrong mental model.
Recommended fix: Add `|-- code/` to the structure diagram between `logs/` and
`projects/`.

[MINOR] — `logs/` appears in the structure diagram but is not described in the
folder conventions section. Its purpose, exclusion from git, and content format
are documented only in SKILL.md's context awareness section and the v24 context
file.
Recommended fix: Add a `logs/` entry to the folder conventions section in
MASTER-PROMPT.md.

[MINOR] — The `code/` deploy-from-source convention has no mechanical
enforcement. Nothing prevents source (projects/ai-library-system/code/) and
deployed (code/) copies drifting silently.

### Single points of failure

[CRITICAL] — SHA-256 manifests are the sole tamper-detection record, but
`temp/` is excluded from git via `.gitignore`. If `temp/` is cleared —
intentionally or by accident — the tamper-detection chain for every previous
checkpoint is permanently broken with no recovery path. The v24 context even
identifies `temp/` misuse (flow-vs-ai accumulating files there), which means
clearing temp/ is a plausible future action. The manifests are described as
living in `temp/`, but `temp/` is described as "checkpoint files only,
ephemeral." There is a design contradiction: the manifests are meant to be
durable audit records, but they live in an ephemeral, un-versioned folder.
Recommended fix: Commit manifests to git via `.gitignore` exception
(`!temp/*-manifest.json`) or move to a dedicated `manifests/` folder.

[MINOR] — MAP.md is the single traversal index for the entire library.
Corruption that bypasses git would halt workflows.

---

## 2. checkpoint.py

### Parsing logic

The tilde-fence regex is correct. `re.MULTILINE | re.DOTALL` is the right
combination. Three-fence fallback hierarchy (tilde → four-backtick →
three-backtick) provides reasonable backward compatibility.

Separator stripping is correct in intent but creates a cosmetic inconsistency:
older THREAD.md entries (v01–v02) have a separator line; newer entries (v24)
do not.

### Edge cases

[MINOR] — `git_commit_message()` assumes the first non-header, non-separator
line of a THREAD ENTRY will be `**Triggered by:**`. If an AI omits it and leads
with `**Artifact:**`, the artifact summary becomes the commit message. Brittle
but has worked in practice.

[MINOR] — Version 00 bypasses all integrity checks. A v00 stub with a malformed
label or missing STATE section would pass validation.

[MINOR] — The THREAD ENTRY block's `### v[NN] — date` header is not
version-validated against the expected version. An AI that writes `### v23`
inside a v24 block would produce a misleading THREAD.md entry.

[MINOR] — `check_triplet` in pre-commit generates duplicate version-mismatch
errors when three or more different versions are staged together. Noisy but not
incorrect.

### Proposed DELTA design change — assessment

Soundness: Architecturally sound. Moving the append-only merge from AI to
Python is correct. LLMs are unreliable at verbatim list reproduction under
context pressure (the v14 repair incident and the v24 dropped-line incident
confirm this). Python merge is deterministic.

Risks:
- A line reworded slightly between versions is treated as new; both forms
  accumulate. No semantic deduplication is possible without an LLM.
- If the AI omits the DELTA section entirely, checkpoint.py must fall back to
  full-copy mode and validate as superset (current behavior). Both modes coexist.
- The append-only superset check still applies after merge — same safety net.
- `extract_section_lines` would need extension to recognise `DELTA:` subsections.

Migration path: Introduce DELTA as an optional subsection. Add `DELTA
DECISIONS:` and `DELTA RULED OUT:` to the CONTEXT block schema. checkpoint.py
detects their presence: if present, reads previous context, appends DELTA lines,
validates merged result. If absent, runs current superset check. No breaking
change to existing checkpoint files. MASTER-PROMPT.md adds one paragraph
documenting the DELTA option.

Verdict: Implement. The failure mode of the current approach (silent decision
loss under context compression) is worse than the failure modes of DELTA. The
v14 repair incident and the lean-AI audit thread note validate this conclusion
from the project's own history.

---

## 3. pre-commit.py

### Validation rules relative to design

[MAJOR] — Design drift: the RULED OUT section of v24--context.md states
"Blocking on MAP.md missing entry — warn only, legitimate during active
sessions." But `check_map_coverage()` calls `err()` (blocking) for files in
`docs/` or `inbox/`. The selective blocking for docs/inbox is not captured in
DECISIONS anywhere. Either the RULED OUT entry is stale or the code overreaches
the design. The divergence is undocumented.
Recommended fix: Add an explicit DECISIONS entry capturing the selective blocking
upgrade. Update or remove the stale RULED OUT entry.

[MAJOR] — `check_artifact_wrapper()` only verifies the artifact is non-empty.
It does not validate the label line (`ARTIFACT v[NN]`), version consistency, or
extension match — all four requirements listed in MASTER-PROMPT.md's artifact
wrapper schema. A manually created or edited artifact with no label line or wrong
version would pass the hook entirely.
Recommended fix: Add label-line validation to `check_artifact_wrapper()` —
confirm version in label matches vNN prefix in filename.

[MINOR] — `check_map_integrity()` regex extracts display text containing slashes
as fake paths. Known issue, documented in v24 RULED OUT. Fix is identified (bare
filenames in display text) but not enforced. Recommended fix: restrict regex to
match only link URLs inside markdown `(...)` syntax.

[MINOR] — `check_map_coverage()` uses naive substring matching. A filename
appearing in MAP.md description text suppresses the warning.

[MINOR] — `check_frontmatter()` does not validate empty values. `title: ` passes.

### What can slip through undetected

1. Artifact file with wrong or missing `ARTIFACT v[NN]` label
2. Context file that drops a DECISIONS entry (superset check is in checkpoint.py only)
3. Frontmatter with empty values
4. THREAD.md manually edited outside add_note_thread.py
5. Standalone files with wrong date-based naming
6. MASTER-PROMPT.md committed from non-ai-library-system project (enforcement deferred)

---

## 4. MASTER-PROMPT.md

### Contradictions and ambiguities

[MAJOR] — Structure diagram omits `code/` at library root. Folder conventions
section documents it correctly. Primary reference for AI sessions is wrong.

[MINOR] — Checkpoint ritual says "do not wait" (produce all four blocks in one
pass). Behaviour rules say "state what you are about to do and wait for
confirmation." Boundary between phases is implicit. An overly literal AI could
interpret the behaviour rule as requiring confirmation before generating each
checkpoint block.
Recommended fix: Add parenthetical to checkpoint ritual: "(The confirmation rule
applies to writes, script runs, and git operations — not to in-session block
production.)"

[MINOR] — Version determination says "read the last THREAD ENTRY in THREAD.md."
Without format knowledge, "last THREAD ENTRY" is ambiguous between the last
`THREAD ENTRY` keyword line and the last `###` header.
Recommended fix: Replace with "find the highest vNN number in THREAD.md and
increment by one."

[MINOR] — Folder conventions lists temp/ contents (checkpoint.txt,
manifest.json) but does not note that temp/ is excluded from git. Manifests
listed there could be misread as committed.

[MINOR] — v24 context DECISIONS entry (line 119) still states "Cowork project
instructions = MASTER-PROMPT.md + persona.md." This is stale following the
2026-04-15 NOTE removing persona.md from the system prompt.

---

## 5. OVERALL LIBRARY CONSISTENCY

### MAP.md accuracy

[MINOR] — MAP.md describes the SKILL.md as "Cowork orchestration skill v5" but
the deployed skill is v6. The deployed copy entry correctly omits the version
number.
Recommended fix: Update MAP.md description to v6 or adopt version-agnostic
format for the source entry.

### v00 stubs

All three projects with active v00 stubs (legal-research, flow-vs-ai) have all
three files correctly listed in MAP.md. Pre-commit triplet rule will be
satisfied.

### Potential orphaned content

`2026-04-13--kurgan-rostok--other.md` in flow-vs-ai is listed directly under
`## projects/flow-vs-ai/` rather than a `## projects/flow-vs-ai/docs/`
subsection. Inconsistent with ai-library-system formatting but not functionally
wrong.

temp/ misuse in flow-vs-ai (kurgan-rostok-review.html, .skill packages) not
committed and not in MAP.md. No MAP integrity issue, but cleanup is pending.

### Naming violations

None found. All versioned files follow two-digit convention. Standalone docs
follow `YYYY-MM-DD--slug--vendor.ext` format.

---

## PRIORITISED TOP-5 ISSUES

1. [CRITICAL] SHA-256 manifests live in git-excluded temp/
   Design contradiction: manifests are the tamper-detection audit chain but live
   in an ephemeral uncommitted folder. One `rm -rf temp/` silently destroys the
   entire integrity history.
   Fix: `.gitignore` exception (`!temp/*-manifest.json`) or move to `manifests/`.

2. [MAJOR] code/ at library root missing from structure diagram
   The diagram is the primary spatial orientation for every AI session. Every
   session touching Layer 3 tooling starts with a wrong mental model.
   Fix: one line addition to the diagram.

3. [MAJOR] pre-commit does not validate the artifact label line
   MASTER-PROMPT.md artifact wrapper schema requires `ARTIFACT v[NN]` as first
   line. Hook only checks non-empty. A corrupted artifact passes the hook and
   fails the next checkpoint's tamper check silently.
   Fix: add label validation to `check_artifact_wrapper()`.

4. [MAJOR] docs/inbox MAP.md blocking contradicts RULED OUT entry
   Code blocks commits for docs/inbox files missing from MAP.md. RULED OUT says
   blocking is ruled out. Neither the upgrade nor any explanation appears in
   DECISIONS. Silent drift between design and implementation.
   Fix: add DECISIONS entry capturing selective blocking; remove stale RULED OUT.

5. [MAJOR] DELTA design change: implement it
   The append-only verbatim-copy approach has already produced two documented
   failures (v14 repair, v24 dropped line). DELTA migration is backward-
   compatible, Python merge is deterministic, superset validation remains as
   safety net.
