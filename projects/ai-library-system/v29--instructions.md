INSTRUCTIONS v29
----------------
PROJECT: AI Document Library System
GOAL: Design, document, and iteratively refine a five-layer vendor-agnostic generational system for managing AI-generated work using plain text files and a prompt-controlled workflow.
BACKGROUND: v28 forked the library to a private GitHub repo (sunkendev/AI-Library) for iOS / cloud Claude Code access. This session was the first cloud session on that fork — it ran the v28 checkpoint as the planned toolchain spike, confirming that .claude/skills autoloads, that CLAUDE.md's @-import resolves MASTER-PROMPT.md automatically, and that a private repo works fine in a cloud session. The import surfaced two real pre-commit hook gaps (CLAUDE.md not excluded from the frontmatter check; a legacy docs file with a stray pre-frontmatter line), which were fixed and committed cleanly. The genesis commit itself needed a one-time --no-verify because the hook's version-mismatch check assumes one checkpoint per commit, not a 28-version bulk import. A cross-project blind spot in the SHA-256 tamper detection for shared files (MAP.md, THREAD.md) was also found and confirmed benign, but not yet fixed in code.
ARTIFACT STATE: MASTER-PROMPT.md unchanged — relabeled v29 via the NO CHANGE sentinel; no structural or ritual edits this session.
KEY DECISIONS:
- Toolchain spike successful end to end: skill autoload, CLAUDE.md import, and private-repo cloud access all confirmed working
- code/pre-commit.py EXCLUDED set fixed to include CLAUDE.md, in both the deployed and source copies
- 2026-04-11--schemas--claude.md fixed to start with its frontmatter block per convention
- v28 genesis import committed with one-time --no-verify after explicit user confirmation; hook unchanged, applies normally from here on
- checkpoint.py's MAP.md/THREAD.md tamper detection has a cross-project blind spot, confirmed via flow-vs-ai's v07 manifest; left unfixed pending a design decision
OPEN QUESTIONS:
- Should the MAP.md/THREAD.md tamper-detection blind spot be fixed (e.g. compare against the most recent manifest across all projects, not just the same slug), and if so, when?
- ARCHITECTURE.tex / USER-GUIDE.tex updates, related: bare-filename hook warning, MAP.md machine-readable block, DELTA design, and SHA-256 manifest → native git cleanup all still pending — see v29--context.md OPEN section for the full list
EXPLICITLY RULED OUT:
- Splitting the v28 genesis import into 28+ separate commits — unnecessary; --no-verify is the hook's own documented escape hatch for one-time bulk imports
- Fixing every pre-commit warning surfaced by the import before committing — only the two real gaps were fixed; version-mismatch behaviour is correct for steady-state and was left as-is
- (Plus all prior ruled-out items — see v29--context.md)
NEXT TASK: Decide whether and how to fix the MAP.md/THREAD.md cross-project tamper-detection blind spot in checkpoint.py, then continue evolving the library on GitHub — pick up ARCHITECTURE.tex/USER-GUIDE.tex updates or another OPEN item as priority allows.
PERSONA: See persona.md
STYLE AND CONSTRAINTS: Plain language. Precise. No lists where prose works better. No suggestions that contradict the established philosophy. When proposing changes to master prompt or documents, show the specific change not a full rewrite. State plan before executing any write, script, or git operation.
