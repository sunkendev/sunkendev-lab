---
title: THREAD.md Growth Wall Analysis
date: 2026-04-13
updated: 2026-04-13
type: document
vendor: claude
model: claude-sonnet-4-6
tags: [context-window, thread-growth, architecture, layer-3]
related: [2026-04-13--v18-compression-forensics--claude.md, THREAD.md, MASTER-PROMPT.md]
---

# THREAD.md Growth Wall Analysis

## Background

The RESUME operation loads four files into the context window at the start of
every session: persona.md, THREAD.md, the latest context file, and the latest
instructions file. Both THREAD.md and context.md are append-only by design —
they never shrink. This document analyses at what point that growth makes the
system impractical or impossible to use.

---

## Current payload (v20)

System prompt overhead is fixed and was measured directly from the v18 forensic
analysis. RESUME file sizes are derived from bytes on disk at v20.

| File | Size on disk | Estimated tokens |
|---|---|---|
| System prompt (fixed) | ~154,084 chars | ~38,521 |
| THREAD.md | ~44,000 chars | ~11,000 |
| v20--context.md | 19,375 bytes | ~4,844 |
| v20--instructions.md | 4,601 bytes | ~1,150 |
| v20--artifact.md | 5,700 bytes | ~1,425 |
| persona.md | ~500 bytes | ~125 |
| **RESUME total** | | **~18,544** |
| **Session start total** | | **~57,065** |

Remaining working budget at session start: **~142,935 tokens** out of 200K.
This is comfortable at v20.

---

## Growth rate

Both append-only files grow with every checkpoint cycle.

THREAD.md accumulates one checkpoint entry (~400–600 tokens) plus any NOTEs
(~100–200 tokens each) between checkpoints. NOTEs are prose-heavy and
accumulate faster than entries when sessions are active.

context.md accumulates new DECISIONS and RULED OUT lines (~150–300 tokens per
checkpoint). It grows more slowly than THREAD.md but never compresses.

Combined growth per checkpoint cycle: approximately **500–800 tokens**.
Using 650 tokens as a working average.

---

## Wall projections

Two thresholds matter. The practical wall is when RESUME load consumes so much
context that sessions become too short to accomplish meaningful work. The hard
wall is when RESUME load alone exceeds the available working budget.

**Practical wall — Tier 1 threshold (130K input tokens):**

At 130K tokens, the context detection skill issues a Tier 1 warning. If this
fires immediately on RESUME load — before any work begins — the session is
effectively broken.

```
130,000 − 38,521 (system prompt) = 91,479 tokens for RESUME
91,479 − 18,544 (current RESUME load) = 72,935 tokens of headroom
72,935 / 650 (tokens per checkpoint) ≈ 112 more checkpoints
```

**Practical wall reached at approximately v132.**

**Hard wall — context window exhausted at load:**

```
161,479 (working budget) − 18,544 (current RESUME load) = 142,935 tokens of headroom
142,935 / 650 ≈ 220 more checkpoints
```

**Hard wall reached at approximately v240.**

The system becomes unusable well before v240. By v132, sessions start at
Tier 1 and the AI is forced to checkpoint before any substantive work. The
practical ceiling is v132, not v240.

THREAD.md is the primary driver. It grows faster than context.md because
NOTEs are unconstrained prose. A project with frequent NOTEs will hit the
wall earlier than these projections suggest.

---

## Mitigations

Three options in order of implementation complexity.

**Option 1 — THREAD.md archiving (recommended)**

When THREAD.md exceeds a defined size threshold, move all checkpoint entries
older than the last five into `THREAD-archive.md`. RESUME loads only the
active tail. The archive remains on disk and in git for reference and audit
but is not loaded into the context window by default.

This requires no schema changes and no new file types. The pre-commit hook
or checkpoint.py could enforce the threshold automatically. The RESUME
operation in the ai-library-ops skill needs one additional step: check
THREAD.md size and warn if archiving is overdue.

Suggested threshold: 8,000 tokens / ~32,000 characters.

**Option 2 — Context.md summarisation at milestones**

Every ten checkpoints, produce a `v[NN]--context-summary.md` that condenses
DECISIONS into categorical blocks rather than a flat append-only list. RESUME
loads the summary instead of the full context file. The full append-only
context stays on disk for integrity and audit.

This requires a new file type in the schema, a new naming convention, and a
revised RESUME procedure. It is more powerful than archiving but significantly
more complex to implement and maintain.

**Option 3 — Project forking**

When a project reaches a defined complexity ceiling, close it and start a
new project slug that references the old one. The new project begins with a
compact seed context derived from the old one. THREAD.md starts fresh.

This is architecturally clean and consistent with the library's existing
philosophy — the iCloud-to-local fork at v15 is a precedent. It requires no
tooling changes. The cost is that historical THREAD.md entries from the old
project are only accessible by loading the old project, not the current one.

---

## Recommendation

Design and implement THREAD.md archiving before v132. The threshold trigger
(32,000 characters in THREAD.md) should be added to checkpoint.py as a
warning, similar to the integrity checks. The archiving step itself can be
a manual operation or automated in ai-library-ops.

At the current growth rate, archiving will be needed around v60–v70 to keep
THREAD.md within a healthy size for the long term. Designing it at v20 gives
forty checkpoints of runway before it becomes urgent.

Project forking remains the fallback if a project evolves so significantly
that a clean break is more appropriate than archiving old entries.
