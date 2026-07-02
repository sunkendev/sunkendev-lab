---
title: AI Document Library — Complete Architecture
date: 2026-04-11
updated: 2026-07-02
type: document
vendor: claude
model:
tags: [architecture, reference, five-layer, design]
related: [MASTER-PROMPT.md, USER-GUIDE.md]
---

# AI Document Library — Complete Architecture

**Layers 1 through 5**

A permanent, vendor-agnostic, generational system for storing, versioning,
navigating, resuming, and automating AI-generated work. From plain text
files to full agentic orchestration. Every layer is optional. Layer 1 is
the only one that is mandatory.

*Version 2.1 — 2026-07-02*

---

## 1. Introduction and Design Philosophy

### What This Document Covers

This document describes the complete five-layer architecture of the AI Document
Library system. It serves as the single reference that integrates all components:
the foundational file system, the session workspace layer, the automation layer,
the synthesis layer, and the full orchestration layer.

Each layer builds on the one below it. No layer is required except Layer 1.
A practitioner who implements only Layer 1 has a fully functional, permanent,
and portable system. Each additional layer adds capability and reduces manual
effort, but at the cost of setup complexity and, in some cases, external
dependencies.

| Layer | Name | What it provides |
|---|---|---|
| 1 | Foundation | Plain text files, naming conventions, the master prompt, the checkpoint ritual. Full control from the prompt. No tooling dependencies beyond git. |
| 2 | Session | A live AI session operating under the master prompt. Currently run through Claude Code and Cowork, with the master prompt loaded automatically via `CLAUDE.md`. Vendor-agnostic by design; the present implementation is one instantiation of it. |
| 3 | Automation | A checkpoint script, a git pre-commit hook, and an orchestration skill that mechanise the parsing, saving, validating, and committing steps of the ritual. No vendor API calls; these tools operate on text already produced in a live session. |
| 4 | Synthesis | Cross-project reasoning-pattern synthesis: an external, read-only system that reads the whole library to learn how the user reasons, producing a versioned, evidence-derived meta-persona. Not yet implemented. |
| 5 | Orchestration | Multi-agent workflows, scheduled sessions, cross-project content synthesis, team sharing infrastructure, and pipeline automation for recurring work. Not yet implemented. |

### Document History

This is version 2.1 of this document. Version 2.0 (2026-06-28) superseded the
original written 2026-04-11 alongside the project's founding documents; the
original is archived at
`projects/ai-library-system/docs/2026-04-11--architecture-v1-original--claude.tex`.
Version 2.1 (2026-07-02) redefines Layer 4, and the document was converted
from LaTeX to Markdown the same day.

The 2.0 rewrite existed because Layers 1–3 had, by that point, been built,
used, and revised through 30 checkpoints of real operation — and had
drifted substantially from the one-shot design session that produced
the original text. At v07 (2026-04-11), updating this document was
explicitly deferred until the system was "scripted live." That
condition was met by roughly v10–v15, once the checkpoint script and
pre-commit hook were running reliably, but the deferral was never
revisited: it was copied forward, unexamined, through every checkpoint
from v08 to v30. Version 2.0 closed that gap for Layers 1–3.

Layer 5 is carried forward from the original text essentially
unchanged. It describes capability that has not been built yet, so
there is no implementation to drift against — it remains what it
always was: a forward-looking design, not a record of something built.
Layer 4 was redefined on 2026-07-02: the original semantic-retrieval
design was retired and the layer now specifies cross-project
reasoning-pattern synthesis, external to the library and read-only
(see the Layer 4 section for the rationale). Both remain unbuilt.

### The Governing Principle

Every design decision in this system follows from one principle:
**the file is the truth, not the application.**

All knowledge about a project — its content, its provenance, its history,
its current state, and its instructions for continuation — lives inside
plain text files that are owned by the user, stored wherever the user chooses,
and readable by any human or any AI without intermediary tooling.

The five layers add convenience, speed, and capability. They do not change
where the truth lives. A library built on Layer 1 and progressively extended
to Layer 5 is the same library throughout. The files do not change format.
The folder structure does not change in kind, only in detail. The master
prompt does not change in role, only in content. The layers are coats of
automation applied to an unchanging foundation.

### Portability and Vendor Independence

This system is designed to survive the discontinuation of any specific
AI vendor, platform, or tool. The following properties are maintained
at every layer:

- All permanent storage is in plain text files in open formats.
- No layer below Layer 4 requires a specific AI vendor.
- Context can be transferred to any AI model by reading (or pasting,
  where file access is unavailable) the master prompt and the
  relevant instructions file.
- The library folder can be moved to any storage location
  without any migration or conversion.
- A person who has never used this system can navigate a project
  folder by reading `THREAD.md` without instruction.

At Layer 4 and Layer 5, specific tooling choices are made
(agentic AI tooling, orchestration frameworks). These choices are
modular. Layer 4 in particular is external to the library and
read-only, so replacing or removing it leaves no trace; the underlying
file system remains intact if any Layer 4 or Layer 5 component is
replaced or removed.

### The Generational Property

A library built under this system is navigable by a human or an AI in
any decade in which plain text files remain readable on some computing
device. The YAML frontmatter, the THREAD.md narrative, the versioned
triplet structure, and the master prompt are all plain text. They require
no renderer, no application, no account, and no network connection.

This property is not incidental. It is the primary design constraint.
Every other design decision — the rejection of proprietary formats,
the embedding of metadata in files rather than databases, the separation
of convenience layers from the permanent record — follows from it.

---

## 2. Layer 1 — Foundation

> **Layer 1: Foundation** — No dependencies beyond git. No setup beyond creating folders and files.
> Full control from the prompt. Mandatory. All other layers build on this.

### What Layer 1 Provides

Layer 1 is the complete system in its minimal form. It provides:

- A folder hierarchy for organising all AI-generated content
- A file naming convention that makes chronological order and
  provenance visible without opening any file
- A YAML frontmatter schema that embeds metadata inside every
  standalone file
- A versioned triplet structure for multi-session projects
- `THREAD.md` as the narrative spine of each project
- `MAP.md` as the traversal index for the entire library
- The master prompt (`MASTER-PROMPT.md`) as the control
  mechanism for any AI session
- A checkpoint ritual that externalises session state on demand
- Git as the permanent, append-only, full-history record of every
  change to every file in the library

### The Folder Structure

```
AI-Library/
|-- MAP.md
|-- MASTER-PROMPT.md
|-- CLAUDE.md
|-- ARCHITECTURE.md
|-- USER-GUIDE.md
|-- temp/
|-- logs/
|-- code/
|   `-- githooks/
|-- .claude/
|   `-- skills/
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

**What each top-level item is for:**

- `CLAUDE.md` — imports `MASTER-PROMPT.md` so
  Claude Code (CLI, cloud, and iOS sessions) loads it automatically
  as project instructions, with no paste step.
- `temp/` — checkpoint files only
  (`v[NN]-checkpoint.txt`). Nothing else is stored here long-term.
- `logs/` — machine-written logs, e.g.
  `checkpoint-runs.log` and `context-pressure.log`.
- `code/` (library root) — deployed, library-wide scripts
  and git hooks. Source for each lives in the owning project's
  own `code/` folder; this is the deployment target.
- `.claude/skills/` — repo-local Claude Code skills,
  loaded automatically in every session type including cloud
  and iOS. Deployed copies live here; source stays in a project
  `code/` folder.
- `projects/[slug]/docs/` — standalone reference material
  produced during that project's sessions: research, reviews,
  working notes. Every file here carries frontmatter. Not for
  checkpoint triplets.
- `projects/[slug]/code/` — source for scripts and skills
  created within that project.
- `inbox/` — standalone files not yet sorted into a
  project's `docs/` folder.

### The Versioned Triplet

Every project checkpoint produces three files at the same version number.
These three files together capture the complete state of the work at a
point in time from three angles: what was built, what was established, and
how to continue.

| File | Contents |
|---|---|
| `v[NN]--artifact.[ext]` | The complete output in its current state. Raw LaTeX, Markdown, code, or plain text. Never summarised or truncated. If unchanged from the previous version, the body is the single line `NO CHANGE` and the previous file is copied and relabelled. |
| `v[NN]--context.md` | Complete state dump: PROJECT, DECISIONS, RULED OUT, OPEN, STATE. DECISIONS and RULED OUT are append-only — every line from the previous version is copied verbatim, then new lines are added. Sufficient for an AI to understand the full project state without reading the artifact. |
| `v[NN]--instructions.md` | Structured resume prompt. Goal, background, artifact state, key decisions, open questions, explicitly ruled-out items, next task, persona, style and constraints. Functional: a new AI session can begin from this file alone. |

### The Checkpoint Ritual

The command `CHECKPOINT` typed into a live session produces four
blocks in sequence, each wrapped in tilde fences (`~~~`)
so inner code samples can use ordinary backtick fences without collision:

1. **ARTIFACT v[NN]** — full current output, or `NO CHANGE`
2. **CONTEXT v[NN]** — complete state dump
3. **INSTRUCTIONS v[NN]** — structured resume prompt
4. **THREAD ENTRY v[NN]** — log entry for `THREAD.md`

The four blocks are assembled into `temp/v[NN]-checkpoint.txt`.
From there, Layer 3 automation takes over: parsing,
saving, validating, and committing. Layer 1 alone — with no
scripting — still works: the four blocks can be copied by hand into
the three triplet files and `THREAD.md`, exactly as the ritual
describes them. The script is a convenience, not a requirement.

### The Master Prompt

`MASTER-PROMPT.md` teaches the AI the complete Layer 1 system in
one shot: structure, conventions, checkpoint format, and all navigation
commands. In Claude Code (CLI, cloud, iOS) it loads automatically via
`CLAUDE.md`'s `@MASTER-PROMPT.md` import — no paste step.
On platforms with a separate system-prompt box and no file-import
mechanism (e.g. Cowork project instructions), it is pasted manually
once per workspace. The commands are:

| Command | Effect |
|---|---|
| `CHECKPOINT` | Produce all four checkpoint blocks |
| `RESUME` | Load persona, THREAD.md, and the latest context/instructions files for a chosen project |
| `NOTE` | Append an inter-checkpoint note to THREAD.md |
| `COMMIT` | Commit routine, non-triplet file changes |
| `NEW PROJECT` | Create a project folder, persona, and v00 stubs |
| `SHOW MAP` | Summarise library state from MAP.md |
| `SHOW THREAD` | Narrate a project's arc from its THREAD.md |

Only the `ai-library-system` project may alter
`MASTER-PROMPT.md`; any other project committing a change to it
is treated as an error. The library is a kernel: out-of-band fixes to
any library file require surfacing the problem, designing the fix, and
getting explicit approval before it is implemented through the correct
path — library Python, a skill, or `MASTER-PROMPT.md` itself.

### Naming Conventions

```
Project files:    v[NN]--[type].[ext]
                  v01--artifact.tex
                  v01--context.md
                  v01--instructions.md

Standalone files: YYYY-MM-DD--[slug]--[vendor].[ext]
                  2026-04-11--analysis-brief--claude.md
```

Two-digit version numbers are mandatory for correct lexicographic sort
order (`v01` through `v99`).

### Frontmatter

Every standalone file (anything in a `docs/` folder or `inbox/`,
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

Triplet files (`v[NN]--artifact/context/instructions`) and core
control files (`MASTER-PROMPT.md`, `CLAUDE.md`, `MAP.md`, `README.md`,
`THREAD.md`, `persona.md`) do not carry this frontmatter block; their identity is
encoded in their filename and position in the structure instead.
LaTeX files cannot carry a YAML `---` block without breaking
compilation, so archived or reference `.tex` files instead carry the
same fields as a `%`-commented block before `\documentclass`.

### What Layer 1 Does Not Provide

- Automatic mechanical execution of the ritual — that is Layer 3
- Synthesis of reasoning patterns across projects — that is
  Layer 4 (search by meaning needs no dedicated layer: any
  session with file access does it with native file tools)
- Scheduling or pipeline automation — that is Layer 5
- The judgment of when to checkpoint, what belongs in a project,
  or how to resolve a conflict — this always remains with the user

---

## 3. Layer 2 — Session

> **Layer 2: Session** — Requires an AI session with file access for full automation;
> works with manual paste on any vendor as a fallback.
> Reduces session startup friction. Does not replace Layer 1 as the permanent record.

### What Layer 2 Provides

Layer 2 is the live AI session in which work actually happens, operating
under the rules in `MASTER-PROMPT.md`. It provides:

- Automatic loading of the master prompt as project instructions,
  where the platform supports a file-import mechanism
- File-based `RESUME` — the AI reads
  `persona.md`, `THREAD.md`, the latest
  `context.md`, and the latest `instructions.md`
  directly from disk, with no copy-paste
- A consistent set of navigation commands that behave identically
  regardless of which AI vendor is running the session
- A fallback to manual paste, in the original four-file order,
  on any platform without file access — the mechanism is
  vendor-agnostic even where today's implementation is not

### Where the Master Prompt Loads

| Platform | How `MASTER-PROMPT.md` reaches the session |
|---|---|
| Claude Code (CLI, cloud, iOS) | Automatic. `CLAUDE.md` at the library root contains `@MASTER-PROMPT.md`, which Claude Code imports as project instructions on every session start. No manual step. |
| Cowork | Manual, once per workspace. Cowork's project-instructions box has no file-import mechanism, so `MASTER-PROMPT.md` is pasted directly into it. |
| Any other vendor (GPT, Gemini, etc.) | Manual, every session. `MASTER-PROMPT.md` is pasted at the start of the chat, exactly as the document instructs. This is the universal fallback that keeps the system vendor-agnostic. |

### What persona.md Is — and Is Not

`persona.md` is read as one of the four `RESUME` files,
not preloaded into the system prompt. Putting it in the system prompt
was tried early in this project and abandoned: a system prompt is not
designed for frequent updates, and persona content needs to be visible
in the same audit trail as everything else `RESUME` loads. It is
read fresh, from disk, every time a project is resumed.

### Session Start with Layer 2

**Where file access is available** (Claude Code, Cowork with repo
access):

1. Type `RESUME`.
2. Confirm which project, if more than one exists.
3. The AI reads `persona.md`, `THREAD.md`, the
   latest `v[NN]--context.md`, and the latest
   `v[NN]--instructions.md` from disk, in that order.
4. The AI asks one clarifying question only if something is
   genuinely ambiguous, then waits to be directed.

**Where no file access exists:** paste the same four files, in
the same order, into the chat after `MASTER-PROMPT.md`. The
ritual is identical; only the transport differs.

> **Important:** Generic platform memory features (a model's
> built-in cross-session recall of user preferences) are not a substitute
> for the Layer 1 checkpoint ritual. They are platform-locked, do not
> transfer between vendors, do not capture structured project state, and
> may be reset by account or policy changes outside the user's control.
> The instructions file — read or pasted at session start — is the
> only reliable, cross-vendor context carrier.

### Multi-Vendor Strategy at Layer 2

If you work across multiple AI vendors, the file-based ritual is what
makes that practical: the triplet files and `THREAD.md` are
plain text with no vendor-specific structure. The current automation
(the skill, `CLAUDE.md`) happens to be built for Claude Code,
but switching vendors for a session never requires migrating data —
only pasting the same files a different tool would otherwise read
automatically.

### Relationship Between Layer 1 and Layer 2

| Function | Layer 1 | Layer 2 |
|---|---|---|
| Permanent context storage | ✓ | — |
| Version history | ✓ | — |
| Cross-vendor portability | ✓ | — |
| Generational durability | ✓ | — |
| Automatic master prompt loading | — | ✓ |
| File-based RESUME (no paste) | — | ✓ |
| Reduced session startup effort | — | ✓ |

---

## 4. Layer 3 — Automation

> **Layer 3: Automation** — Requires Python and git. No AI vendor API calls.
> Eliminates manual copy-paste from the checkpoint ritual and enforces
> structure before anything is committed.

### What Layer 3 Provides

Layer 3 is three things working together: a checkpoint script, a git
pre-commit hook, and a skill that orchestrates both along with the
other ritual operations. None of them call an AI API — they operate
purely on text that a live session has already produced.

- `code/checkpoint.py` — parses the four tilde-fenced
  blocks out of `temp/v[NN]-checkpoint.txt`, confirms all
  four are present and version-matched, writes the triplet files,
  appends the THREAD ENTRY to `THREAD.md`, updates
  `MAP.md`, then runs a post-write integrity check that
  reports (but does not undo) drift from the previous version
- `code/githooks/pre-commit` — blocks a commit that
  breaks triplet lockstep or version consistency; warns (but does
  not block) on advisory issues like MAP.md path drift
- The `ai-library-ops` skill — the actual entry point a
  user invokes for `CHECKPOINT`, `NOTE`,
  `COMMIT`, `RESUME`, and `NEW PROJECT`;
  it calls the scripts below in the right order and handles the
  git operations around them
- `code/add_note_thread.py` — appends a `NOTE`
  to a project's `THREAD.md` and commits immediately

After Layer 3, the checkpoint ritual is:

1. Produce the four blocks in the live session (Layer 1/2, unchanged).
2. Save them to `temp/v[NN]-checkpoint.txt`.
3. Run `checkpoint.py [slug] [NN]` as a dry run; review the
   proposed files, sizes, and commit message.
4. Run it again with `--write`. If the project declares
   deploy targets (via its `.deploy` marker —
   `ai-library-system` declares `MASTER-PROMPT.md`),
   the script auto-deploys the artifact verbatim as part of the
   write. Copying it by hand is prohibited; a pre-commit guard
   verifies the deployed file byte-equals the latest artifact.
5. Commit. The pre-commit hook validates structure before the
   commit is allowed to complete.

The human judgment of when to checkpoint, and what belongs in each
block, remains entirely with the user. The mechanical work of parsing,
naming, saving, and validating is what is automated.

### checkpoint.py

```
checkpoint.py [project-slug] [version-number] [--write]

Operations:
1. Locate the project folder from the slug --- error if missing
2. Error if THREAD.md is not found inside that project folder
3. Read temp/v[NN]-checkpoint.txt --- error if missing
4. Resolve the artifact's file extension by inheriting it from the
   previous version's artifact file on disk (default .md if there
   is no previous version, e.g. v01)
5. Error if any target file (v[NN]--artifact.[ext], v[NN]--context.md,
   v[NN]--instructions.md) already exists --- checkpoint.py never
   overwrites
6. Parse the four labelled, tilde-fenced blocks:
   - ARTIFACT v[NN]      (or the NO CHANGE sentinel)
   - CONTEXT v[NN]
   - INSTRUCTIONS v[NN]
   - THREAD ENTRY v[NN]
   error if any block is missing, or if its version number does not
   match the version passed on the command line
7. Without --write: print the plan and exit (dry run)
8. With --write:
   - save ARTIFACT to v[NN]--artifact.[ext] (or copy-and-relabel
     the previous artifact, if NO CHANGE)
   - save CONTEXT to v[NN]--context.md
   - save INSTRUCTIONS to v[NN]--instructions.md
   - append THREAD ENTRY to THREAD.md
   - update MAP.md
   - auto-deploy the artifact verbatim to any targets declared in
     the project's .deploy marker
   - run a post-write integrity check against the files just
     written and the previous version on disk:
       - DECISIONS / RULED OUT are a superset of the previous
         context file
       - artifact / context size ratios are not wildly inconsistent
     this check is advisory only --- it runs after the triplet is
     already on disk, and reports warnings rather than rolling
     anything back
   - log the run, and the integrity warnings if any, to
     logs/checkpoint-runs.log
```

The THREAD.md ascending-version-order check is a separate concern,
owned by the pre-commit hook (see "The Pre-Commit Hook" below), not
by this script — it runs at commit time across every
`THREAD.md` in the library, not just the one being
checkpointed.

There is deliberately no tamper-detection or hashing layer in this
script. An earlier version computed and stored a SHA-256 manifest per
checkpoint to detect post-hoc edits to triplet files. That mechanism
was removed once the library moved to git as its system of record:
every commit already gives a full, durable, content-addressed diff of
every file, with no per-project blind spot. Tamper detection is git's
job now, not the script's.

### The Pre-Commit Hook

`code/githooks/pre-commit` runs on every commit (after
`git config core.hooksPath code/githooks` is set once per
clone). It distinguishes two severities:

- **Blocks the commit:** a staged `v[NN]` file without
  its matching triplet members at the same version; a version
  number that does not match across a triplet; a deployed artifact
  target (e.g. `MASTER-PROMPT.md`) out of sync with the latest
  artifact when either is staged.
- **Warns, does not block:** any staged file (not just
  `docs/` — the check applies to every non-exempt staged
  path) not yet listed in `MAP.md`; a `MAP.md` entry
  whose path does not resolve to a file on disk; THREAD.md entries
  out of ascending order.

The hook does not check itself, and excludes files that are exempt from
the frontmatter/triplet rules (`MASTER-PROMPT.md`, `CLAUDE.md`,
`MAP.md`, `README.md`, `THREAD.md`, `persona.md`, `SKILL.md`) via a
single centralised exclusion set.

### The ai-library-ops Skill

The skill is what a user actually invokes. It is the thing that turns
"type CHECKPOINT" into a finished, committed triplet, and it is the
only Layer 3 component end users interact with directly:

| Operation | What the skill does |
|---|---|
| CHECKPOINT | Saves the four blocks to `temp/`, runs `checkpoint.py` dry-run then `--write` (which auto-deploys `MASTER-PROMPT.md` verbatim when it is the artifact), commits, then pushes and fast-forwards `main`. |
| NOTE | Calls `add_note_thread.py` with the topic and body; commits immediately. |
| COMMIT | Stages and commits routine, non-triplet file changes (e.g. `ARCHITECTURE.md`, `USER-GUIDE.md`). |
| RESUME | Discovers the library root, lists projects, reads `persona.md`, `THREAD.md`, and the latest `context.md`/`instructions.md` from disk — not the artifact file itself. No paste. |
| NEW PROJECT | Runs three guided persona questions, then writes the project folder, `persona.md`, `THREAD.md`, and v00 stub triplet. |

The skill is repo-local (`.claude/skills/`), so it loads
automatically in Claude Code cloud and iOS sessions as well as the
CLI — installed plugins do not run in cloud sessions, but repo-local
skills do.

### What Layer 3 Does Not Provide

- Cross-project reasoning-pattern synthesis — that is Layer 4
- Scheduling — that is Layer 5
- The checkpoint trigger judgment — that always remains with the user
- Any AI vendor API call — the scripts are pure text processors

---

## 5. Layer 4 — Synthesis

> **Layer 4: Synthesis** — Requires a separate repository and an AI with native file-reading tools.
> Reads the library — never writes it — to learn how the user reasons in collaboration with AI.
> Produces a versioned, evidence-derived model of the user's thinking patterns.

### What Layer 4 Provides

Layer 4 is cross-project reasoning-pattern synthesis. It reads the
library as a corpus — every project's `THREAD.md` arc, the
append-only DECISIONS and RULED OUT registers, and the recorded
reversals — and distils from them how the user actually reasons:
which trade-offs they weigh and how, what they reliably reject and
why, what kinds of arguments change their mind, and what rigor they
demand before accepting a fix.

The output is a thinking-patterns document — a meta-persona —
derived from evidence rather than self-description, versioned like any
other artifact so the user can audit what the system claims to have
learned about them and correct it. Where `persona.md` is the
user's self-declared behaviour specification, the Layer 4 synthesis is
the measured counterpart; disagreement between the two is itself
signal.

A possible later use of the same corpus is AI training —
conditioning or tuning a model to mimic the user's judgment patterns.
That use is explicitly deferred and unscoped; nothing in this layer's
design depends on it.

### Why the Original Retrieval Design Was Retired

In versions 1.0 and 2.0 of this document, Layer 4 was specified as
semantic retrieval: an embedding model, a vector store, and index
maintenance scripts living inside the library. That design was retired
on 2026-07-02, for two reasons.

First, dedicated retrieval infrastructure became unnecessary. Agentic
file search — an AI session using its native file tools (read, grep,
glob) in an iterative loop — displaced embedding-based retrieval for
corpora of exactly this kind, industry-wide, during 2025–2026. The
library's own conventions (consistent naming, frontmatter,
`MAP.md`, one schema everywhere) make it maximally legible to
that kind of search, with no index to build, sync, or back up.
Searching the library by meaning is now understood as a native
capability of any Layer 2 session with file access, not a layer of its
own.

Second, retrieval was never the layer's real intent. Finding relevant
prior work is a convenience; the standing purpose of reading across
projects is to learn from the accumulated record of human–AI
collaboration itself. The layer number is retained; its contents are
redefined.

### Architecture: External and Read-Only

Layer 4 lives in its own repository, external to the library. It reads
a clone of the library and never writes to it. Three consequences
follow, each deliberate:

- **The library stays a pure corpus.** A synthesis engine
  is a software project; housing it inside the library would
  break the constraint that keeps the library free of CI,
  dependency manifests, and non-stdlib code. Externalising it
  means the library requires nothing new.
- **The record cannot be contaminated.** Read-only access
  preserves the single-active-writer model and the kernel rule.
  This matters doubly here: the library is Layer 4's training
  signal, and a consumer that could write into its own source
  data would poison the well.
- **The vendor boundary lands cleanly.** The library-facing
  interface is just the filesystem. The Layer 4 repository may
  be as vendor-specific as it likes — native AI tools, one
  vendor's agent runtime — without compromising the library's
  vendor independence, because removing Layer 4 leaves no trace
  in the library.

Read-only is currently a discipline, not an enforcement — nothing
mechanical prevents an external agent from writing into a clone. The
practical write barriers are git: the library remote's branch
protection, and the fact that a Layer 4 clone's changes are never
pulled. A filesystem-level read-only mount is the stronger option if
discipline proves insufficient.

### The Corpus and Its Limits

What the library offers as signal, in roughly descending order of
value:

- **RULED OUT registers** — rejected options with recorded
  rationale: preference pairs, the strongest available signal of
  where the user's boundaries lie
- **Reversals** — decisions overturned later, with both
  states preserved by the append-only rule: direct evidence of
  what kinds of arguments change the user's mind
- **DECISIONS registers** — the settled positions themselves
- **THREAD.md arcs** — the temporal order in which positions
  were reached, held, and revised
- **persona.md** — the self-declared baseline the synthesis
  can be tested against

Three limits are known in advance and must be designed against rather
than discovered:

- **The corpus is AI-mediated.** Checkpoint blocks are
  drafted by an AI and approved by the user; they record
  conclusions and rationales in the AI's phrasing, not the
  deliberation itself. A naive synthesis will partly learn the
  checkpoint genre rather than the user. Reversals and explicit
  user overrides are the least contaminated signal.
- **The synthesis needs a falsification path.** Without an
  evaluation — for example, predicting the user's actual call
  on held-out decisions and scoring against what they really
  chose — the meta-persona is unfalsifiable prose. No such
  evaluation is designed yet.
- **It is a decision-policy model, not a mind.** The corpus
  supports learning judgment patterns. It does not support
  recreating cognition. Richer capture of in-the-moment
  deliberation at checkpoint time is the only way to deepen what
  can be learned.

### Open Design Questions

- **Where the output lives.** Either the synthesis stays in
  the Layer 4 repository (observer model: the library never
  knows Layer 4 exists), or it returns to the library through
  the front door as a normal versioned project artifact
  reachable by RESUME (contributor model: same ceremony as any
  approved change). The contributor model creates a feedback
  loop — sessions load the meta-persona, which shapes future
  decisions, which feed future synthesis — and that loop must
  be reasoned about before the first synthesis run, not after.
- **Coupling to the library's growth mitigation.** Any
  future archiving or compression of `THREAD.md` decides
  what Layer 4 can ever learn. If this layer is the long-term
  purpose of the corpus, growth mitigation must preserve the
  reasoning record verbatim — archive, never summarise.

### What Layer 4 Does Not Provide

- Writes to the library — never, under any design
- Retrieval infrastructure — native agentic file search
  already covers finding relevant prior work
- Content-level cross-project synthesis (connections and
  contradictions between project subject matter) — that is
  Layer 5's synthesis agent; Layer 4 synthesises the reasoning,
  not the content
- Automatic or scheduled synthesis runs — scheduling is Layer 5
- Recreation of the user's cognition — the corpus supports a
  decision-policy model, nothing deeper

---

## 6. Layer 5 — Orchestration

> **Layer 5: Orchestration** — Requires MCP client, agent framework, and scheduling infrastructure.
> Transforms the library from a managed archive into an active, partially autonomous system.
> Implement only when Layers 1 through 3 are stable and well-understood.
> Layer 4 is external and independent — not a prerequisite.

### What Layer 5 Provides

Layer 5 extends the library with capabilities that run with minimal
human intervention per session. These capabilities are:

- **MCP integration:** An AI client (Claude Code, Cursor, or
  a custom wrapper) that reads the library folder directly and
  navigates it without the user pasting any files
- **Scheduled sessions:** Recurring AI tasks that run on a
  schedule and produce new files in the library automatically
- **Cross-project content synthesis:** An agent that reads
  across multiple project THREAD.md files and produces synthesis
  documents that identify connections, contradictions, and
  patterns between project subject matter (distinct from Layer 4,
  which synthesises the user's reasoning patterns, not content)
- **Team infrastructure:** Shared library folders, role-based
  access to project folders, and merge protocols for collaborative
  work on shared projects
- **Pipeline automation:** Multi-step workflows where one
  AI agent's output becomes another agent's input, orchestrated
  across the library file system

### MCP Integration

The Model Context Protocol (MCP) is an open standard that allows an AI
client to read and write files in a local folder as part of its context.
When the library folder is connected to an MCP-compatible client, the AI
can navigate `MAP.md`, open `THREAD.md` files, read version
files, and update them — all without the user pasting anything.

#### How MCP Changes the Session Start

Without MCP (Layers 1–3):

1. Open a session under the master prompt (automatic or pasted)
2. Type RESUME
3. The AI reads persona.md, THREAD.md, and the latest
   context/instructions files from disk, or they are pasted

With MCP (Layer 5):

1. Open MCP client pointed at `AI-Library/`
2. Type: "Resume the [project name] project."
3. The AI reads `MAP.md`, locates the project, opens
   `THREAD.md`, reads the latest instructions file,
   and confirms its understanding

The checkpoint ritual is triggered by voice or a single word. Saved
files are written by the agent directly.

#### MCP Configuration

```
# .mcp-config.json in AI-Library root
{
  "library_root": "./",
  "system_prompt_file": "MASTER-PROMPT.md",
  "map_file": "MAP.md",
  "projects_dir": "projects/",
  "allowed_write_paths": ["projects/", "inbox/", "temp/", "logs/"],
  "protected_files": ["MASTER-PROMPT.md", "ARCHITECTURE.md",
                       "USER-GUIDE.md", "CLAUDE.md"]
}
```

Protected files cannot be modified by the agent. All writes are logged.

### Scheduled Sessions

Certain AI tasks are well-suited to scheduled execution. Examples:

- **Weekly synthesis:** Every Sunday, an agent reads all
  `THREAD.md` files updated in the past week and produces
  a weekly synthesis document summarising progress, decisions
  made, and open questions across all active projects.
- **Research monitoring:** A daily agent runs a set of
  standing queries against a web search tool, compares results
  to existing research files, and produces a "new developments"
  note in a project's `docs/` folder when significant new
  material is found.
- **Inbox processing:** A nightly agent reads all files in
  `inbox/`, proposes frontmatter and filenames for each,
  and produces a triage report. The user reviews and approves
  the proposed classifications.

Scheduled sessions are implemented using the operating system's
scheduler (`cron` on macOS/Linux, Task Scheduler on Windows)
combined with a script that invokes an AI vendor API and writes the
output to the library.

```
# crontab entry for weekly synthesis
0 8 * * 0 /path/to/AI-Library/code/weekly-synthesis.py
```

### Cross-Project Content Synthesis

As the library grows, connections between projects become valuable and
difficult to see manually. A synthesis agent reads across the entire
library and produces documents of the form:

- "Projects X and Y are working on related problems.
  Here are the relevant decisions from each and where they conflict."
- "The argument developed in project A in February was
  contradicted by findings in project C in April.
  Here is a summary of the conflict."
- "These five research files collectively cover the topic of Z.
  Here is a synthesis of their conclusions."

Synthesis documents are stored in the relevant project's `docs/`
folder with a `synthesis` tag and references to all source files
in their `related:` frontmatter field.

### Team Infrastructure

For users who want to share a library with collaborators or extend it
across a family or team over time, Layer 5 includes a shared folder
protocol.

#### Shared Folder Structure

```
AI-Library-Shared/           (shared cloud folder or shared git remote)
|-- MAP.md                   (maintained by designated librarian)
|-- MASTER-PROMPT.md
|-- projects/
|   |-- [shared-project]/    (all contributors read and write)
|   `-- [personal-project]/  (one owner, others read-only)
|-- team/
|   |-- [person-a]/          (personal subfolders, read-only to others)
|   `-- [person-b]/
`-- synthesis/               (cross-contributor synthesis documents)
```

#### Merge Protocol

When two contributors work on the same project in the same time period,
a merge protocol resolves version conflicts:

1. Both contributors checkpoint before merging.
2. The merge agent reads both sets of version files and
   `THREAD.md` entries.
3. It produces a merged `THREAD.md` entry that records
   what each contributor added and where their work diverges.
4. It proposes a merged instructions file for the next session.
5. The designated project owner reviews and approves the merge.

### Pipeline Automation

A pipeline is a sequence of AI tasks where the output of one becomes
the input of the next. Example pipeline for a research brief:

```
Pipeline: research-brief
Steps:
  1. search-agent:     Run web searches on [topic], produce research notes
                       -> save to projects/[topic]/docs/[date]--raw--claude.md
  2. synthesis-agent:  Read research notes, synthesise key findings
                       -> save to projects/[topic]/docs/[date]--synthesis--claude.md
  3. brief-agent:      Read synthesis, produce structured brief
                       -> create project [topic]-brief, v01 checkpoint
  4. review-agent:     Read brief, produce critique and open questions
                       -> append to THREAD.md as a NOTE
  5. (human reviews v01, directs revisions, session continues manually)
```

Steps 1–4 run automatically. Step 5 requires human judgment.
The pipeline stops and waits at the human review step.

Pipelines are defined as YAML files in `code/pipelines/`
and invoked by name:

```
run-pipeline.py research-brief --topic "interest rates small business"
```

### Layer 5 File Structure

```
AI-Library/
|-- .mcp-config.json
|-- code/
|   |-- checkpoint.py
|   |-- weekly-synthesis.py
|   |-- run-pipeline.py
|   |-- merge.py
|   `-- pipelines/
|       |-- research-brief.yaml
|       `-- [other pipelines]
|-- (all Layer 1-3 files unchanged; Layer 4 adds nothing here)
```

### What Layer 5 Requires Before Implementation

> **Warning:** Layer 5 should not be implemented until Layers 1 through 3
> are stable and well-understood. The failure modes of automated agents
> writing to your library are more severe than the failure modes of manual
> workflows. An agent that misclassifies files, overwrites `THREAD.md`
> entries incorrectly, or produces low-quality synthesis documents creates
> a mess that is time-consuming to correct. The manual discipline of
> Layers 1 through 3 is the correct starting point.

Before implementing Layer 5, the following should be true:

- Layer 1 is in active daily use with at least 10 projects
- Layer 3 (scripted checkpoints) is running reliably
- The user can navigate the library from `MAP.md` without
  confusion and has a clear mental model of its structure
- Git version control is active on the library folder so that
  any agent-caused damage can be reverted

---

## 7. The Complete Stack

### Layer Dependency Diagram

```
+------------------------------------------+
|        Layer 5 --- Orchestration         |
+------------------------------------------+
                    ^
                    |      +-----------------------------------+
                    |      |  Layer 4 --- Synthesis            |
                    |      |  (external repo, reads the        |
                    |      |   library; never writes it)       |
                    |      +-----------------------------------+
                    |                   |
                    |                   | reads (read-only)
                    |                   v
+------------------------------------------+
|         Layer 3 --- Automation           |
+------------------------------------------+
                    ^
                    |
+------------------------------------------+
|          Layer 2 --- Session             |
+------------------------------------------+
                    ^
                    |
+------------------------------------------+
|   Layer 1 --- Foundation (mandatory)     |
+------------------------------------------+
```

Layers 1–3 and 5 stack: each builds on the one below. Layer 4 sits
outside the stack — it consumes the library that Layers 1–3 produce,
and nothing depends on it.

### What Each Layer Owns

| Responsibility | Layer | Mechanism |
|---|---|---|
| Permanent storage | 1 | Plain text files in folder hierarchy |
| Metadata | 1 | YAML frontmatter on standalone files |
| Version history | 1 | Versioned triplet files (v01, v02…) and git |
| Project narrative | 1 | THREAD.md checkpoint log |
| Library navigation | 1 | MAP.md traversal index |
| Session control | 1 | Master prompt + commands |
| Master prompt auto-loading | 2 | CLAUDE.md import (Claude Code) |
| File-based RESUME | 2 | Skill reads persona + THREAD + latest context/instructions from disk |
| Reduced startup friction | 2 | No copy-paste required where file access exists |
| Checkpoint parsing and saving | 3 | checkpoint.py |
| Structural validation | 3 | pre-commit hook |
| Ritual orchestration | 3 | ai-library-ops skill |
| Note logging | 3 | add_note_thread.py |
| Reasoning-pattern synthesis | 4 | External read-only repo, agentic reading of all projects |
| Meta-persona output | 4 | Versioned synthesis document (location undecided) |
| Folder navigation by AI | 5 | MCP client reads library directly |
| Scheduled tasks | 5 | cron + API scripts |
| Cross-project content synthesis | 5 | Synthesis agent reads all THREAD.md |
| Pipeline automation | 5 | run-pipeline.py orchestrates agents |
| Team collaboration | 5 | Shared folder + merge protocol |

### Implementation Sequence

The recommended implementation sequence is strictly bottom-up.
Do not skip layers.

1. **Layer 1:** Create the folder structure. Move existing
   files into `inbox/`. Sort one project. Create its
   `THREAD.md` and `persona.md`. Save
   `MASTER-PROMPT.md` to the library root. Run one
   complete session and call one checkpoint by hand. This is the
   proof of concept.

2. **Layer 2:** Run several sessions from the project's
   natural environment (Claude Code, Cowork, or manual paste).
   Verify `RESUME` consistently reconstructs the right
   state from persona.md, THREAD.md, and the latest
   context/instructions files alone, with no missing context.

3. **Layer 3:** Write or deploy the checkpoint script and
   pre-commit hook. Test on a real checkpoint output. Verify all
   four files save correctly and `THREAD.md`/`MAP.md`
   update accurately. Use it for ten real checkpoints before
   adding Layer 4.

4. **Layer 4:** Create the external synthesis repository and
   give it read-only access to a library clone. Decide where the
   output lives (observer vs. contributor) and design the
   evaluation before the first synthesis run. Run a first
   synthesis across all projects and validate it against
   `persona.md` and held-out decisions before trusting it.
   Independent of Layer 5 — may be built before or after.

5. **Layer 5:** Implement MCP connection first, before any
   scheduling or pipelines. Run ten sessions via the MCP client.
   Then implement one scheduled task (the weekly synthesis is
   recommended as the first). Verify it produces useful output
   for one month before implementing pipelines.

### Status of This Library

| Layer | Status | Note |
|---|---|---|
| 1 | Implemented | In daily use since project start; 30+ checkpoints |
| 2 | Implemented | Multi-platform: Claude Code (CLI/cloud/iOS), Cowork |
| 3 | Implemented | checkpoint.py, pre-commit hook, ai-library-ops skill |
| 4 | Not implemented | Redefined 2026-07-02: external read-only synthesis repo; unscoped |
| 5 | Not implemented | Estimated 8–20 hours setup once undertaken |

---

## 8. Document Index

| File | Contents |
|---|---|
| `MASTER-PROMPT.md` | The control mechanism for every AI session. Contains the complete Layer 1 operating instructions for any AI model. |
| `CLAUDE.md` | Imports `MASTER-PROMPT.md` so Claude Code sessions load it automatically; the Layer 2 loading mechanism for this implementation. |
| `USER-GUIDE.md` | Practical, task-oriented guide: how to RESUME, CHECKPOINT, NOTE, COMMIT, and start a NEW PROJECT, end to end. |
| `ARCHITECTURE.md` | This document. Complete five-layer architecture reference. |

---

## Colophon

`AI-Library / ARCHITECTURE.md` — Version 2.1 — 2026-07-02

Plain text. Open format. No vendor. No application required. No expiry.

Layer 1 is the only mandatory layer.
Every additional layer adds convenience.
None of them changes where the truth lives.
