---
title: AI Library Full System Audit (at v34)
date: 2026-06-29
updated: 2026-06-29
type: document
vendor: claude
model: claude
tags: [audit, master-prompt, pre-commit, map, code-deploy, drift]
related: [MASTER-PROMPT.md, MAP.md, THREAD.md, 2026-04-15--architecture-review--claude.md]
---

# AI Library: Full System Audit

A fresh critical read of the live library as it stands at v34, conducted by reading the
on-disk artifacts directly (scripts, MASTER-PROMPT.md, MAP.md, ARCHITECTURE.tex,
USER-GUIDE.tex, the deployed `code/` tree) and verifying each finding with a reproducible
command. The goal was drift, gaps, bugs, and inconsistencies — not redesign.

This document **surfaces** issues only. Per the kernel rule, no fix is applied here; each
remediation below is a recommendation to be designed and approved separately, then
implemented through its correct path (MASTER-PROMPT.md only via an ai-library-system
checkpoint; scripts via the project→deploy convention; MAP.md/docs via normal edits).

---

## What is healthy (verified)

- **Script deployment is in sync.** All six Python scripts are byte-identical between source
  (`projects/ai-library-system/code/`) and the deployed `code/` root. `SKILL.md` is
  byte-identical across all three locations (source, `code/ai-library-ops/`,
  `.claude/skills/ai-library-ops/`).
- **Tests pass.** `test_checkpoint.py` (25) + `test_git_sync.py` (17) = 42 tests, all green.
- **Prior bug fixes are in place and correct.** checkpoint.py's v31 artifact-extension
  resolution (`find_artifact_path` / `resolve_artifact_extension`) and git_sync.py's v33
  diverged-main reset (`git checkout -B main origin/main` before the ff-only check) are both
  present and behave as designed.
- **Narrative integrity holds.** THREAD.md entries v01–v34 are in ascending order; every
  triplet is complete; the working tree is clean.
- **The LaTeX references are accurate.** ARCHITECTURE.tex and USER-GUIDE.tex each mention the
  SHA-256 manifest only in the past tense, correctly describing it as the *removed* mechanism
  (post-v30), and they describe `core.hooksPath` as the current hook wiring. No drift.

---

## Findings (severity-ranked)

### A. MEDIUM-HIGH — The deployed MASTER-PROMPT.md carries a stray, stale artifact label

`head -4 MASTER-PROMPT.md`:

```
ARTIFACT v31
------------
You are operating inside a structured plain-text document library.
```

The live Layer 2 control prompt — imported into every session's system prompt via CLAUDE.md's
`@MASTER-PROMPT.md` — begins with the artifact **wrapper label** instead of the prompt text,
and the label is stale (`v31` while the library is at v34). The body beneath the label is
otherwise identical to the v34 artifact body, so this is cosmetic-to-functional, not content
loss — but it is noise inside the kernel, and the version number actively misinforms.

**Root cause.** The checkpoint ritual's step 3 copies the *labelled* artifact file verbatim:
`cp projects/[slug]/vNN--artifact.md MASTER-PROMPT.md`. Since v12, artifact files self-describe
with a `LABEL` + separator as their first two lines, so this copy injects `ARTIFACT vNN` / `----`
into the deployed kernel on every MASTER-PROMPT.md checkpoint. The defect is latent in the
ritual and will recur.

**Recommended fix (needs approval; MASTER-PROMPT.md changes only via an ai-library-system
checkpoint).** Change the ritual's step-3 copy to strip the first two lines, e.g.
`tail -n +3 vNN--artifact.md > MASTER-PROMPT.md`, and re-deploy a clean MASTER-PROMPT.md.

### B. MEDIUM — flow-vs-ai experiment code leaked into library-root `code/`, orphaned and divergent

`code/` at root is reserved for *library-wide operational scripts and skills*. It also contains
single-project experiment code from flow-vs-ai, in a degraded state:

- `code/kurgan/`, `code/rostok/`, `code/schemas/` — **orphaned**: no corresponding source in any
  project folder, and not referenced anywhere in MAP.md.
- `code/kurgan-rostok/` — **divergent from its source** (`projects/flow-vs-ai/code/kurgan-rostok/`):
  the deployed copy is *missing* `SKILL.md` and carries an extra `_SKILL.md.deprecated` plus a
  `schemas/` subtree the source does not have. `diff -rq` confirms.

All of it entered in the v28 genesis import (`d6ee3bf`) and was never cleaned — it is the larger
cousin of the long-standing "flow-vs-ai temp/ cleanup" OPEN item. Beyond the mess, there is a
convention question: kurgan-rostok is a project experiment, not library-wide tooling, so it
arguably should not be deployed to `code/` root at all.

**Recommended fix (needs approval).** Remove the three orphaned dirs; decide whether kurgan-rostok
belongs in `code/` root and, if so, redeploy it cleanly from source (and update its MAP.md entry);
otherwise drop it too and remove the MAP.md line.

### C. MEDIUM — MAP.md broken link

Line 152, `[SKILL.md](code/kurgan-rostok/SKILL.md)`, points to a file that does not exist — the
deployed directory holds `_SKILL.md.deprecated`, not `SKILL.md`. `pre-commit.py`'s
`check_map_integrity()` would flag this, *if the hook were active* (see D). Resolved as part of B.

### D. MEDIUM — The pre-commit hook is inactive in this clone

`git config --get core.hooksPath` is empty and `.git/hooks/pre-commit` is absent, so structural
validation is currently **off**. The skill *does* bootstrap it (`SKILL.md` line 52:
`git config core.hooksPath code/githooks`), but only inside its CHECKPOINT/COMMIT/NOTE git step —
not at session start. Any `git commit` issued directly, outside the skill, before the first
skill-driven write op runs unvalidated. This is an inherent property of the portable per-clone
hook model, but it is live exposure worth surfacing.

**Recommended fix (needs approval).** Either run `git config core.hooksPath code/githooks` at the
start of each clone/session, or extend the skill's RESUME operation to perform the bootstrap (not
only the write ops).

### E. LOW — pre-commit.py prose contradicts its behaviour

`check_map_coverage()`'s docstring ("Block if a docs/ or inbox/ file has no entry in MAP.md") and
its inline comment ("docs/ and inbox/ files must always be indexed — block the commit") describe a
blocking `err()`, but the code calls `warn()`. The warn-only behaviour is correct per the v25
decision; the prose is stale and should be corrected (comment/docstring only).

### F. LOW — MAP.md skill entry is four versions stale

Line 119 describes ai-library-ops as **"skill v5 ... CHECKPOINT, NOTE, COMMIT, RESUME, NEW PROJECT,
and CONTEXT CHECK"**. The skill is **v9** (git_sync.py extraction). Index drift.

### G. LOW — MAP.md is missing two real deployed-file entries

The `## code/` section omits `code/githooks/pre-commit` (the portable hook itself) and
`.claude/skills/ai-library-ops/SKILL.md` (the cloud-autoload copy, a genuine third deploy location
added at v28). Both exist on disk and ship with the library; neither is indexed.

### H. TRIVIAL — Dead parameter in git_sync.py

`sync(operation_label, push_only, cwd)` never uses `operation_label`; the label is only consumed by
`log_result()`. Harmless, but it reads as if `sync` logs when it does not.

### I. INFO — Legacy manifest files linger in temp/

`temp/` holds 20 git-tracked `*-manifest.json` files (flow-vs-ai v02–v07, ai-library-system v16–v29)
for the mechanism removed at v30. They were deliberately retained as archived records per that
decision, but `.gitignore` no longer excepts them (`!temp/*-manifest.json` was dropped), so the
state is slightly inconsistent: tracked files that the ignore rule would now exclude. Not a bug;
noted as known dead weight.

---

## Still genuinely open (confirmed, not resolved by this audit)

These carry forward from the v34 context unchanged: `related:`-field bare-filename hook warning;
MAP.md machine-readable block; MASTER-PROMPT.md artifact-type schema; pre-commit MASTER-PROMPT.md
write protection (env-var bypass pattern agreed); DELTA design for checkpoint.py; the
`git-sync.log` vs `checkpoint-runs.log` fold question; iCloud/USB-C backup; Layer 4/5.

---

## Suggested remediation order

1. **A** (clean the kernel) and **F/G** (MAP.md accuracy) — low-risk, high-clarity, and A touches
   the most important file in the system.
2. **B + C** together (the flow-vs-ai `code/` cleanup) — resolves the orphan/divergence mess and
   the broken MAP.md link in one pass; this also retires a years-standing OPEN item.
3. **D** (hook bootstrap on RESUME) — closes the silent-validation-off window.
4. **E, H** — cosmetic code/doc hygiene, fold into whichever script touch happens next.

Each of the above is a separate, approval-gated change through its correct path. None was applied
in producing this audit.
