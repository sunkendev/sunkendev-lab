---
title: v18 Context Compression Forensics
date: 2026-04-13
updated: 2026-04-13
type: document
vendor: claude
model: claude-sonnet-4-6
tags: [context-compression, forensics, layer-3, skill-design]
related: [THREAD.md, MASTER-PROMPT.md]
---

# v18 Context Compression Forensics

## Background

During the v18 checkpoint session, context compression occurred mid-execution.
The checkpoint blocks had been fully assembled and written to disk before
compression hit. The session continued from a summary rather than live context.
This document analyses that event using the 5 Whys method and records the
forensic findings that will inform threshold calibration for the proposed
context-detection skill.

---

## 5 Whys

**Why did the session end in a compressed state?**
The model's context window was exhausted. At turn 225, input tokens collapsed
from 165,028 to 54,023 — a drop of 111,005 tokens — as the runtime injected
a session summary in place of the full live context.

**Why did the token count reach 165,028?**
The session ran 224 turns with sustained, deep tool use — skill code authoring,
multiple file writes, git operations, code edits across several files, and
intermediate reads and verifications. Each tool call and result added to the
accumulated context.

**Why did the session run 224 turns without a checkpoint?**
No mechanism existed to detect rising context pressure or warn the user before
compression hit. Checkpoints were triggered by milestone judgment only. The
session felt productive until the moment compression occurred — there was no
visible degradation signal to prompt an early stop.

**Why was there no detection mechanism?**
The library system was designed around project milestones as checkpoint
triggers. Context window limits were not considered as a trigger condition.
The assumption was that sessions would naturally end before pressure became
critical.

**Why were context limits not considered as a trigger?**
The system was built from the outside in — file formats, schemas, version
control, scripting — with context health as an implicit concern rather than
an explicit design constraint. No prior compression event had occurred to
surface it as a real failure mode. The v18 event is the first instance.

---

## Forensic Findings

### 1. Compression point

Last coherent output: Turn 224 (18:23:41) — a Write tool call saving
`temp/v18-checkpoint.txt` containing all four checkpoint blocks.
Input context at that turn: 165,028 tokens, 6,913 output tokens.

First degraded output: Turn 225 (18:25:32) — a thinking-only turn with no
text output. Input context collapsed to 54,023 tokens (a drop of 111,005
tokens). The model was operating from an injected session summary, not
live context.

### 2. Character count at compression

The JSONL transcript up to and including turn 224 totalled 1,293,079
characters. Applying the `len(text) // 4` heuristic gives 323,269 estimated
tokens — 161.6% of a 200K window. This figure is inflated: JSONL format
includes metadata, timestamps, and thinking blocks not present in the live
context. The authoritative figure, read from the `usage` field directly,
was 165,028 input tokens = **82.5% of the 200K window**.

The `// 4` heuristic on raw transcript characters is not reliable for
threshold calibration. The `usage` field is the correct source.

### 3. System prompt overhead

Directly measurable from turn 1's `cache_creation_input_tokens`:
**38,521 tokens ≈ 154,084 characters**. This is the system prompt cached
before any user content — Cowork system prompt, MASTER-PROMPT.md, persona.md,
and project instructions. It represents **19.3% of the 200K window** consumed
before the session begins. Any threshold model must account for this fixed cost.

### 4. Signals before compression

No structural degradation in reasoning quality was visible at any point.
Observable signals were present but individually ambiguous:

From turn ~155 (~138K tokens): text outputs between tool calls collapsed to
1–3 tokens — single connector phrases. This is consistent with normal
deep-tool-chain behaviour and does not reliably indicate compression risk.

From turn ~166 (~141K tokens): a persistent pattern of alternating `stop=none`
turns emitting exactly 8 output tokens (thinking-only, no visible text). Silent
decision steps. This pattern became dense at turns 169–195 and 218–222.

Turn 188 (~149K tokens): a status summary response that would normally be a
paragraph was suppressed to 8 output tokens — content appeared only in the
thinking block, never rendered as text. This is the most legible signal in
retrospect: a response whose expected length was far above its actual output.

Turn 220 (~159K tokens): a decision text of 1 output token.

None of these signals individually indicate context pressure. There is no
single pre-compression warning moment observable from output quality alone.
Detection based on output behaviour is not reliable. Detection must use
the `usage` token count directly.

### 5. What was mid-flight

Turn 223: TodoWrite initialised + ARTIFACT v18 block produced and written.
Turn 224: CONTEXT v18, INSTRUCTIONS v18, and THREAD ENTRY v18 blocks produced
and written as a single Write call to `temp/v18-checkpoint.txt`.

Compression hit between the file write and the dry-run step. All four blocks
were complete and on disk at the moment of compression. The checkpoint was not
mid-block. Recovery was clean precisely because the file existed on disk and
the injected session summary correctly identified the next step. The
file-first design of the checkpoint workflow saved the session.

### 6. Threshold recommendation

Compression hit at 165,028 tokens. At 20% headroom:

`165,028 × 0.80 = 132,022 tokens`

**Practical threshold: warn when input tokens exceed 130,000.**

At that point in the v18 session (approximately turns 183–185, 18:05–18:06),
the session had just completed the lock-handling fixes and was packaging the
skill — a natural pause point where a checkpoint could have been triggered
before the write_snapshot and self-containment work that consumed the
remaining 35K tokens.

With system prompt overhead fixed at ~38,521 tokens, the available session
budget is approximately 161,479 tokens. A 130,000-token warning fires at
80.6% of actual available budget, giving roughly 31,000 tokens of runway
after the warning — enough to finish most in-progress operations and run
a checkpoint cleanly.

---

## Conclusions for Skill Design

The `usage` field is the only reliable detection source. Character count
heuristics on transcript text overcount by ~2x due to JSONL overhead.
Output behaviour signals are present but not reliably distinguishable from
normal deep-tool-chain patterns.

System prompt overhead of ~38K tokens is a fixed cost that must be
subtracted from the nominal 200K window when reasoning about available budget.
Effective session budget is approximately 160K tokens, not 200K.

Tier 1 warning threshold: **130,000 input tokens**.
Tier 2 urgent threshold: **155,000 input tokens** (leaving ~10K for a checkpoint).

The file-first design of the checkpoint workflow proved its value: because
all four blocks were written to disk before the dry-run step, the compression
event caused no data loss. This is an argument for keeping the write step
early in the checkpoint sequence, not at the end.
