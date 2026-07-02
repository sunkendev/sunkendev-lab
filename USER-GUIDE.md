---
title: AI Document Library — User Guide
date: 2026-06-28
updated: 2026-07-02
type: document
vendor: claude
model:
tags: [user-guide, reference, operations]
related: [MASTER-PROMPT.md, ARCHITECTURE.md]
---

# AI Document Library — User Guide

**How to Operate the Library, End to End**

A task-oriented companion to ARCHITECTURE.md. This document explains what
to do, in what order, to RESUME a project, run a CHECKPOINT, leave a NOTE,
COMMIT routine work, or start a NEW PROJECT. It assumes nothing about which
AI vendor or platform you are using.

*Version 1.1 — 2026-07-02*

Companion to ARCHITECTURE.md. See MASTER-PROMPT.md for the authoritative
ritual definitions; this guide explains how to act on them.

---

## 1. Before You Start

This guide is practical, not philosophical. For the reasoning behind the
five-layer model, see ARCHITECTURE.md. For the authoritative, word-for-word
ritual definitions, see MASTER-PROMPT.md — this guide explains how to act
on those rituals, but MASTER-PROMPT.md is always the final word if the two
ever disagree.

### Document History

This is version 1.1 (2026-07-02): converted from LaTeX to Markdown, with
the CHECKPOINT walkthrough corrected to describe the automatic
MASTER-PROMPT.md deploy (the manual copy step it previously described was
replaced by checkpoint.py's auto-deploy and is now prohibited).

Version 1.0 was written 2026-06-28. There was no prior guide at this
scope: the original user guide (2026-04-11) documented a clipboard
copy-paste workflow — pasting MASTER-PROMPT.md and four RESUME files into
a chat box by hand, once per session. That workflow no longer exists.
RESUME, CHECKPOINT, NOTE, COMMIT, and NEW PROJECT are now file-based
operations carried out by the `ai-library-ops` skill, and `CLAUDE.md`
loads MASTER-PROMPT.md automatically in Claude Code, cloud, and iOS
sessions. The original document is archived at
`projects/ai-library-system/docs/2026-04-11--user-guide-v1-original--claude.tex`
as the historical record of that earlier design. Version 1.0 replaced it
entirely rather than amending it, because the underlying workflow changed,
not just the details.

### What You Need

- A clone of the AI-Library git repository.
- An AI session with file read/write access to that clone — Claude
  Code (CLI, cloud, or iOS), Cowork, or any platform that can read and
  write files in the repository.
- Git, configured with `core.hooksPath` pointed at
  `code/githooks` (see [One-Time Setup](#2-one-time-setup)).

> **Note:** If your platform cannot access files (a plain chat box with no
> file access), Layer 1 still works by hand: paste MASTER-PROMPT.md once,
> then paste the four RESUME files when resuming, and paste the checkpoint
> blocks back to yourself to save. Every instruction in this guide that
> refers to a script or skill running automatically has a manual equivalent
> in MASTER-PROMPT.md. Layer 1 never depends on Layer 3 being available.

---

## 2. One-Time Setup

Run once per fresh clone. A fresh clone never receives `.git/hooks/`
automatically, so the portable hooks in `code/githooks/` have to be
pointed to explicitly:

```
cd AI-Library
git config core.hooksPath code/githooks
chmod +x code/githooks/pre-commit
```

If git identity is not already configured in this environment (common on
a fresh cloud or iOS clone):

```
git config user.email "you@example.com"
git config user.name  "Your Name"
```

If you are using the `ai-library-ops` skill (the normal case in
Claude Code), it bootstraps both of the above automatically on its first
operation in a fresh clone. You do not need to do this by hand on every
machine — only verify it once if something seems to be silently failing.

---

## 3. Folder and File Conventions

### Where Things Live

```
AI-Library/
|-- MAP.md                  Index of everything in the library
|-- MASTER-PROMPT.md        The operative system prompt (Layer 2 control)
|-- CLAUDE.md               Imports MASTER-PROMPT.md for Claude Code
|-- ARCHITECTURE.md         Why the system is built this way
|-- USER-GUIDE.md           This document
|-- temp/                   Checkpoint staging only
|-- logs/                   Automation run logs
|-- code/                   Deployed scripts and skills
|   `-- githooks/           Portable git hooks
|-- .claude/skills/         Repo-local skills (load in cloud/iOS too)
|-- projects/
|   `-- [project-slug]/
|       |-- THREAD.md             Checkpoint log + inter-checkpoint notes
|       |-- persona.md            Read during RESUME, never preloaded
|       |-- docs/                 Standalone dated documents
|       |-- code/                 Project-local scripts/skills (source)
|       |-- v[NN]--artifact.[ext]
|       |-- v[NN]--context.md
|       `-- v[NN]--instructions.md
`-- inbox/                  Unsorted files awaiting a project
```

### Naming Rules

- **Project triplet files:** `v[NN]--artifact.[ext]`,
  `v[NN]--context.md`, `v[NN]--instructions.md`.
  Version numbers are always two digits: `v01`, `v02`,
  … `v09`, `v10`, `v11`.
- **Standalone files** (anything in a `docs/` folder or
  `inbox/`): `YYYY-MM-DD--short-slug--vendor.[ext]`.

### Frontmatter

Every standalone file (anything named with the dated convention above,
plus the root reference documents `ARCHITECTURE.md` and `USER-GUIDE.md`)
begins with:

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

The version-triplet files (`v[NN]--*`) do not use this frontmatter
block — their structure is already fixed by the checkpoint schema.
Core control files (`MAP.md`, `MASTER-PROMPT.md`, `CLAUDE.md`,
`README.md`, `THREAD.md`, `persona.md`) are exempt as well. LaTeX files cannot use
a YAML `---` block without breaking compilation, so archived `.tex`
files instead carry the same fields as a `%`-commented block before
`\documentclass`.

---

## 4. RESUME — Loading a Project

Use RESUME to pick up a project you have worked on before. It is the most
common operation in a normal session.

**What you say:** "Resume" (or "resume a project", "load
[project]", "switch project").

**What happens:**

1. The AI locates the library root and lists every folder under
   `projects/`.
2. It asks which project to resume (or proceeds directly if you named
   one).
3. It finds the highest-numbered `v[NN]--context.md` and
   `v[NN]--instructions.md` for that project.
4. It reads, in this exact order: `persona.md`, then
   `THREAD.md`, then the latest `context.md`, then the
   latest `instructions.md`.
5. It states the project, the current version, and a one-sentence
   summary of artifact state, then waits for direction.

> **Note:** RESUME reads files from disk. You never need to paste
> anything — if an AI asks you to paste persona.md or THREAD.md content,
> it does not have file access to this repository, and you are effectively
> back on the Layer 1 manual path.

### What persona.md Is — and Is Not

`persona.md` is read at RESUME time, as one of the four files
above. It is *not* preloaded into a system prompt and does not
persist automatically between sessions on its own. This was tried early
in the project and abandoned: a system prompt is not designed for
frequent updates, and persona content needs to sit in the same
RESUME-time audit trail as everything else, not in a separate channel
that can drift out of sync with it. If a platform offers a persistent
system-prompt or custom-instructions box, you may paste persona.md there
once as a convenience, but RESUME does not depend on it and will re-read
the file from disk regardless.

---

## 5. CHECKPOINT — Saving Progress

Use CHECKPOINT to save the current state of a project as a new version.
This is the core ritual of the library.

### The Four Blocks

Saying CHECKPOINT produces four blocks, each wrapped in tilde fences with
its label as the first line:

1. **ARTIFACT v[NN]** — the full artifact as raw text. If the
   artifact has not changed since the previous version, the body is
   the single line `NO CHANGE`; the automation copies and
   relabels the previous artifact file rather than asking you to
   retype it.
2. **CONTEXT v[NN]** — PROJECT / DECISIONS / RULED OUT / OPEN /
   STATE. DECISIONS and RULED OUT are append-only: every line from the
   previous context file is copied forward verbatim, then new lines
   are added at the end. Nothing already there is ever removed,
   shortened, or reworded.
3. **INSTRUCTIONS v[NN]** — a complete resume packet: GOAL,
   BACKGROUND, ARTIFACT STATE, KEY DECISIONS, OPEN QUESTIONS,
   EXPLICITLY RULED OUT, NEXT TASK, PERSONA, STYLE AND CONSTRAINTS.
4. **THREAD ENTRY v[NN]** — the dated log line appended to
   THREAD.md: trigger, artifact state, context state, instructions
   state, key decisions, still-open items.

The version number is always the last THREAD ENTRY number plus one. The
AI determines this by reading THREAD.md, not by asking you.

### From Blocks to Files

1. The four blocks are assembled into one file:
   `temp/v[NN]-checkpoint.txt`.
2. **Dry run:** `python3 code/checkpoint.py [slug] [NN]`.
   This parses the blocks, validates them, and shows exactly what it
   would write — but writes nothing yet.
3. Read the dry-run output. Confirm the file paths and sizes look
   right.
4. **Write:** `python3 code/checkpoint.py [slug] [NN] --write`.
   This writes the versioned triplet, appends the THREAD
   ENTRY to THREAD.md, and updates MAP.md.
5. **If the artifact is MASTER-PROMPT.md specifically:** nothing to do
   by hand. checkpoint.py auto-deploys the artifact verbatim — the
   self-describing `ARTIFACT v[NN]` label included — to
   `MASTER-PROMPT.md` at the library root, driven by the project's
   `.deploy` marker. Copying it by hand is prohibited; a pre-commit
   guard verifies the deployed file byte-equals the latest artifact.
   `CLAUDE.md` then loads it automatically on every future Claude Code,
   cloud, or iOS session — no manual paste. Only platforms with a
   separate system-prompt box outside this repository (for example, a
   Cowork project-instructions field) need it pasted by hand.
6. `git add .` and commit. The pre-commit hook validates the
   triplet before allowing the commit through (see
   [What Runs Automatically](#9-what-runs-automatically)).

If you are using the `ai-library-ops` skill, saying CHECKPOINT
walks all of the above automatically: it assembles the blocks, runs the
dry run, shows you the output, runs `--write` (which performs the
auto-deploy if relevant), commits, then pushes the branch and
fast-forwards `main`. You still see every step's output — it is
automated, not silent.

> **Warning:** Only the ai-library-system project may alter
> MASTER-PROMPT.md. A checkpoint from any other project that touches
> MASTER-PROMPT.md is an error — stop and fix the project assignment
> before writing.

---

## 6. NOTE — Logging Between Checkpoints

Use NOTE for something worth recording in THREAD.md that does not justify
a full checkpoint — a decision made mid-session, an observation, a
small correction.

```
echo "Note body." | python3 code/add_note_thread.py [slug] "Topic" --write
```

The script appends the note in the correct format and commits THREAD.md
immediately. THREAD.md is never edited by hand for notes — always
through this script, so the immediate-commit rule is enforced
automatically rather than relying on memory.

---

## 7. COMMIT — Routine Changes

Use COMMIT for ordinary work that is not part of a version triplet and
not a THREAD.md note — editing a script in `code/`, adding a
document to a project's `docs/` folder, fixing a typo in MAP.md.

1. Run `git status` and review what changed.
2. Confirm which files belong in this commit — COMMIT should not
   silently sweep in unrelated work.
3. Stage exactly those files and commit with a descriptive message.

```
git add [file1] [file2] ...
git commit -m "[descriptive message]"
```

---

## 8. NEW PROJECT — Starting Something New

Use NEW PROJECT to create a new project folder with a persona and a blank
THREAD.md, ready for its first CHECKPOINT.

1. **Name the project.** A slug is derived automatically
   (lowercase, hyphens, no punctuation) and confirmed with you.
2. **Three guided persona questions, asked one at a time:**
   1. What is this project, and what is the AI's job in it?
   2. How should the AI behave — tone, directness, at least one
      hard constraint?
   3. One concrete example exchange: a question you'd ask, and the
      answer you'd want. This shapes behavior more reliably than
      any description.
3. **persona.md is generated** from the three answers (ROLE,
   DOMAIN, BEHAVIOUR, EXAMPLES) and shown to you for confirmation
   before anything is written.
4. **Once confirmed,** the project folder, `THREAD.md`,
   and `v00` stub triplet are created and committed. The v00
   stubs exist only so RESUME and the pre-commit triplet check both
   work before the first real CHECKPOINT produces v01.
5. **MAP.md is updated** with a new section for the project.

THREAD.md starts blank apart from its schema. Fill in "What this project
is" after the first real working session — there is no need to
front-load it before any work has happened.

---

## 9. Other Navigation Commands

| Command | What it does |
|---|---|
| SHOW MAP | Summarizes the current state of the library from MAP.md. |
| SHOW THREAD | Summarizes a project's checkpoint log and describes its arc in plain language. |

---

## 10. What Runs Automatically

### The Pre-Commit Hook

`code/githooks/pre-commit` runs on every commit once
`core.hooksPath` is configured. It has two severities:

- **Blocks the commit:** a version triplet is incomplete, or
  triplet version numbers do not match each other (lockstep
  violation), or a deployed artifact target (e.g. MASTER-PROMPT.md)
  is out of sync with the latest artifact when either is staged.
- **Warns but does not block:** a staged file not yet listed
  in MAP.md, a MAP.md entry's path that does not match an actual
  file, THREAD.md entries out of numeric order.

> **Note:** There is no checksum or tamper-detection step. Git's commit
> history is the system of record for integrity — a separate manifest
> would only duplicate what git already verifies on every clone and pull.

### The ai-library-ops Skill

A repo-local skill at `.claude/skills/` (loads automatically in
Claude Code, including cloud and iOS sessions) that drives CHECKPOINT,
NOTE, COMMIT, RESUME, and NEW PROJECT end to end — the mechanical parts
of every section above. It does not change what any ritual produces; it
only removes the manual copy-paste-and-run steps.

---

## 11. Multi-Platform Notes

| Platform | How MASTER-PROMPT.md loads |
|---|---|
| Claude Code (CLI / cloud / iOS) | Automatically, via `CLAUDE.md`'s import on every session start. |
| Cowork | Paste once into the project's system-prompt field; it then persists for that project. |
| Other AI vendors | No automatic mechanism — paste MASTER-PROMPT.md at the start of each session. |

The rituals themselves (RESUME, CHECKPOINT, NOTE, COMMIT, NEW PROJECT) are
the same regardless of platform — only how the master prompt gets
loaded, and whether a skill automates the mechanical steps, differs.

---

## Colophon

`AI-Library / USER-GUIDE.md` — Version 1.1 — 2026-07-02

Plain text. Open format. No vendor. No application required. No expiry.

This guide explains how to act on the library.
MASTER-PROMPT.md is the authority on what the rituals mean.
ARCHITECTURE.md is the authority on why they exist.
