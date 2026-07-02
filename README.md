# AI-Library

A plain-text, vendor-agnostic system for storing, versioning, navigating, and
resuming AI-assisted work — in Claude Code, Claude Projects, Cowork, or any
platform that can read files and run a script.

No database, no proprietary format, no vendor lock-in. Everything is
Markdown, JSON, and stdlib Python, held together by one operative prompt and
a git repository.

## Why

Long-running AI work — a research thread, a codebase, a piece of fiction —
outlives any single chat session. This library gives that work a durable
home: every session's decisions, open questions, and next steps are written
to disk in a fixed schema, so a fresh AI session (or a different model
entirely) can pick up exactly where the last one left off, with nothing lost
to context-window limits or platform switches.

## How it works

- **`MASTER-PROMPT.md`** is the sole control mechanism. It defines the
  folder conventions, file schemas, and the `CHECKPOINT` / `NOTE` / `RESUME`
  / `NEW PROJECT` commands an AI follows inside this library. It is loaded
  automatically in Claude Code via `CLAUDE.md`'s `@MASTER-PROMPT.md` import.
- **Projects** live under `projects/<slug>/` as a `persona.md` +
  `THREAD.md` (checkpoint log) + a versioned triplet per checkpoint:
  `v[NN]--artifact.*`, `v[NN]--context.md`, `v[NN]--instructions.md`.
- **`RESUME`** loads a project's `persona.md`, `THREAD.md`, and latest
  `context.md` + `instructions.md` — never the artifact itself — which is
  enough for a memory-less session to continue the work faithfully.
- **`CHECKPOINT`** produces the next version's triplet plus a `THREAD.md`
  entry and a `MAP.md` index update, all validated by
  `code/checkpoint.py` and a pre-commit hook (`code/pre-commit.py`).
- **`code/git_sync.py`** pushes and fast-forwards `main` so a session never
  ends stranded on an orphaned branch.

Full mechanics are documented in `ARCHITECTURE.md` (design/reference) and
`USER-GUIDE.md` (practical walkthrough).

## Repository layout

```
AI-Library/
|-- MAP.md              # index of every file in the library
|-- MASTER-PROMPT.md     # the operative system prompt
|-- CLAUDE.md            # imports MASTER-PROMPT.md for Claude Code sessions
|-- ARCHITECTURE.md      # five-layer design reference
|-- USER-GUIDE.md        # end-to-end usage guide
|-- code/                # deployed scripts, skills, and their tests
|   `-- githooks/        # portable pre-commit hook (enable per clone, see below)
|-- .claude/skills/       # Claude Code cloud-autoload skill copy
|-- projects/
|   `-- ai-library-system/  # the system's own build history — a fully
|                            # worked example of the checkpoint ritual
|-- temp/                # checkpoint staging files (git-ignored)
|-- logs/                # operational logs (git-ignored)
`-- inbox/               # unsorted files awaiting a project home
```

This repository ships without example content projects — `projects/` holds
only `ai-library-system`, the project that designed and built the library
itself. Add your own project with `NEW PROJECT` (see below) to see the
workflow in action.

## Getting started

1. Clone the repo, then enable the portable pre-commit hook once per clone:
   ```
   git config core.hooksPath code/githooks
   ```
2. Open the repo in Claude Code. `CLAUDE.md` loads `MASTER-PROMPT.md`
   automatically as the system prompt.
3. Say `NEW PROJECT [name]` to start a project, or `RESUME` to continue an
   existing one.
4. Say `CHECKPOINT` at the end of a working session to save a versioned
   snapshot; use `NOTE` for lighter-weight inter-checkpoint updates.

## Requirements

Python 3 (stdlib only — no dependencies to install) and git.

## License

MIT — see `LICENSE`.
