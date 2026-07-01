INSTRUCTIONS v28
----------------
PROJECT: AI Document Library System
GOAL: Design, document, and iteratively refine a five-layer vendor-agnostic generational system for managing AI-generated work using plain text files and a prompt-controlled workflow.
BACKGROUND: v28 forks the library to a private GitHub repo so it can be used from the Claude iOS app via cloud Claude Code sessions, and as an open-source on-ramp. The Cowork copy is frozen at v28 as a baseline and is not used in parallel. The move is pure-cloud: content is brought to GitHub by manual upload, with no local clone or sync on the Mac. This checkpoint was prepared in Cowork; the mobility files (CLAUDE.md, .gitignore exception, skill at .claude/skills/, code/githooks/pre-commit) are ready for upload, and v29 onward evolves on GitHub.
ARTIFACT STATE: MASTER-PROMPT.md v28 — structure diagram adds CLAUDE.md, .claude/skills/, code/githooks/; folder conventions document repo-local skills and portable hooks; the checkpoint ritual MASTER-PROMPT special case now describes CLAUDE.md Layer 2 instead of a manual paste.
KEY DECISIONS:
- v28 forks the library to a private GitHub repo; Cowork frozen at v28; copies not used in parallel
- Pure-cloud move: manual upload, no local clone or sync
- Audit trail lives in the files, not git commits — fresh-history upload preserves it
- Layer 2 via CLAUDE.md importing MASTER-PROMPT.md; manual paste only where no CLAUDE.md mechanism exists
- Skill deployed to .claude/skills/; portable git replaces Cowork-only discovery, lock-delete, hooks, and identity
OPEN QUESTIONS:
- Does a repo-local .claude/skills skill autoload and auto-trigger in a cloud session? (first cloud session is the spike)
- Cloud-session plan-tier eligibility for private repos?
- CLAUDE.md @-import behaviour across Claude Code versions?
- GitHub remote publication, ARCHITECTURE.tex / USER-GUIDE.tex updates, DELTA design, manifest->git cleanup all still pending
EXPLICITLY RULED OUT:
- Pushing from the live Cowork folder; local clone or sync for the fork; parallel live use of both copies
- (Plus all prior ruled-out items — see v28--context.md)
NEXT TASK: (1) Manually upload the library to the private GitHub repo, including the five prepared mobility files. (2) Open an iOS cloud Claude Code session and run the v28 checkpoint via code/checkpoint.py (dry-run then --write) — this doubles as the spike confirming the skill loads and the toolchain works in cloud. (3) Evolve v29 on GitHub.
PERSONA: See persona.md
STYLE AND CONSTRAINTS: Plain language. Precise. No lists where prose works better. No suggestions that contradict the established philosophy. When proposing changes to master prompt or documents, show the specific change not a full rewrite. State plan before executing any write, script, or git operation.
