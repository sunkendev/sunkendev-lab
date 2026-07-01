---
title: Layer 1 Foundation Reference
date: 2026-04-11
updated: 2026-04-11
type: document
vendor: claude
model: claude-sonnet-4-6
tags: [layer-1, foundation, reference]
related: [MASTER-PROMPT.md, ARCHITECTURE.tex, USER-GUIDE.tex]
---

# Layer 1 — Foundation Reference

Layer 1 is the mandatory base of the AI Document Library System. It requires
no tools, no automation, and no platform dependency beyond a text editor and
a git client. Every other layer is optional and builds on this one.

---

## Philosophy

The file is the truth, not the application. A document stored in a proprietary
format or inside a platform is at risk the moment that platform changes its
pricing, API, or existence. Plain text files in open formats remain readable
by any tool — including any AI — across decades.

Vendor independence is a hard requirement at every layer. The system must work
equally with Claude, GPT, Gemini, or any successor. Nothing in Layer 1 depends
on a specific AI's capabilities or memory model.

The master prompt is the sole control mechanism. Every AI session begins with
MASTER-PROMPT.md pasted into the chat. The AI reads it and operates within
the system. No app, plugin, or integration is required.

---

## Folder structure

```
AI-Library/
|-- MAP.md
|-- MASTER-PROMPT.md
|-- ARCHITECTURE.tex
|-- USER-GUIDE.tex
|-- projects/
|   `-- [project-slug]/
|       |-- THREAD.md
|       |-- persona.md
|       |-- docs/
|       |-- code/
|       |-- v01--artifact.[ext]
|       |-- v01--context.md
|       `-- v01--instructions.md
`-- inbox/
```

`projects/` contains one subfolder per project. Each project folder is
self-contained: its versioned files, THREAD.md, persona.md, and any supporting
documents in `docs/` or code in `code/` all live inside it.

`inbox/` is for unsorted items. Drop anything unclassified here first.
Sort it into a project folder when you know where it belongs.

`MAP.md` is the single traversal index for the entire library. Every file in
the library has an entry in MAP.md. It has no META section — structure is
derived from content and git history.

The root contains only MAP.md, MASTER-PROMPT.md, and formal reference documents.
No other folders exist at the root level.

---

## File naming

Project files use a two-digit version prefix:

```
v[NN]--artifact.[ext]
v[NN]--context.md
v[NN]--instructions.md
```

Version numbers are always two digits — v01 through v99 — so files sort
correctly in any file system without tool assistance.

Standalone files use a date-slug-vendor pattern:

```
YYYY-MM-DD--short-slug--vendor.[ext]
```

Example: `2026-04-11--schemas--claude.md`

The vendor field identifies which AI produced the file. This matters for
provenance and for understanding the context in which the file was created.

---

## Frontmatter

Every standalone file begins with a YAML frontmatter block:

```
---
title:
date:
updated:
type: document | code | context
vendor: claude | gpt | gemini | other
model:
tags: []
related: []
---
```

All eight fields are mandatory. The `type` field accepts exactly three values:
`document`, `code`, or `context`. No other values are valid.

Project files — versioned triplet files, THREAD.md, and persona.md — do not
carry frontmatter. They are project files, not standalone documents. Their
metadata is carried by the versioning system and git history.

---

## Checkpoint triplet

Every project checkpoint produces exactly three files at the same version number:

- `v[NN]--artifact.[ext]` — the output itself: a document, prompt, script, or other deliverable
- `v[NN]--context.md` — full state dump: every settled decision, everything ruled out, open questions, current state
- `v[NN]--instructions.md` — resume instructions: everything a new AI needs to pick up the project from scratch

The triplet is the unit of trust. All three files must exist at the same version
number. Staging any one of the three without the others is a structural violation
and the pre-commit hook will block the commit.

Checkpoints are reserved for major milestones. Routine working sessions are
committed to git without producing a new triplet.

---

## Context file schema

Context files use exactly these sections in this order:

```
PROJECT: name and one-line description
DECISIONS: every settled decision, stated as facts, append-only
RULED OUT: everything explicitly rejected and why, append-only
OPEN: unresolved questions, one per line
STATE: current snapshot of where the project stands right now
```

DECISIONS and RULED OUT are append-only. Nothing is ever removed from them.
They are a permanent record of why the project is in its current state.

---

## Instructions file schema

Instructions files use exactly these sections in this order:

```
PROJECT:
GOAL:
BACKGROUND:
ARTIFACT STATE:
KEY DECISIONS:
OPEN QUESTIONS:
EXPLICITLY RULED OUT:
NEXT TASK:
PERSONA:
STYLE AND CONSTRAINTS:
```

NEXT TASK is the most critical field. It tells the resuming AI exactly what
to do first, in enough detail that no clarification is required.

---

## THREAD.md

Every project has one THREAD.md at its folder root. It contains:

- Title, start date, and status (`active | paused | complete | archived`)
- A description of what the project is
- A reference to persona.md
- A checkpoint log in ascending version order

Entries in the checkpoint log are append-only and always ascending. The log
is the episodic history of the project. An AI resuming a project reads
THREAD.md to understand how the project arrived at its current state.

Inter-checkpoint working notes can be appended to THREAD.md at any time
without triggering a checkpoint. Use this format:

NOTE YYYY-MM-DD
---------------
**Topic:** [one line]
[prose — as long or short as needed]

Notes are append-only. No triplet is required. No version number. Notes
record decisions, observations, or corrections made between checkpoints
that should not be lost but do not warrant a full milestone commit.

---

## persona.md

Every project has one persona.md. It defines the role, domain, behaviour,
and examples the AI should follow for that project. All four sections are
mandatory. persona.md carries no frontmatter.

The EXAMPLES section is not optional. Specific, detailed personas with
worked examples produce significantly better AI behaviour than generic
role descriptions.

---

## Pre-commit validation hook

The library uses a Python pre-commit hook at `.git/hooks/pre-commit` to
enforce structural integrity at commit time. The hook source lives at
`projects/ai-library-system/code/pre-commit.py`.

The hook blocks commits on structural violations:

- vNN prefix must be exactly two digits
- Standalone `.md` and `.txt` files must have complete, valid frontmatter
- Any versioned file staged requires all three triplet files at the same version
- Staging files at two different version numbers in the same project folder is blocked

The hook warns but allows commits for advisory checks:

- Staged file not referenced in MAP.md
- MAP.md references a path that does not exist on disk
- THREAD.md checkpoint entries out of ascending version order
- Context or instructions files missing required section headers

All warnings are actionable. A clean commit with no warnings is the target state.
Use `git commit --no-verify` only in genuine emergencies.

---

## Resuming a project

To resume a project in a new AI session, paste MASTER-PROMPT.md into the chat,
then type RESUME and paste the following four files in this exact order:

1. `persona.md`
2. `THREAD.md`
3. `v[NN]--context.md` (latest version)
4. `v[NN]--instructions.md` (latest version)

All four files are required. Resuming from the instructions file alone is
insufficient — the AI needs the full context and project history to operate
correctly.

---

## What Layer 1 does not include

Layer 1 is the foundation only. It does not include automation, scripting
beyond the pre-commit hook, API integration, embedding or search, or any
platform dependency. All of that belongs in Layers 2 through 5, all of which
are optional.