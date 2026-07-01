INSTRUCTIONS v37
----------------
PROJECT: AI Document Library System
GOAL: Design, document, and iteratively refine a five-layer vendor-agnostic generational system for managing AI-generated work using plain text files and a prompt-controlled workflow.
BACKGROUND: This session bootstrapped the clean public template into the new sunkendev-lab repo per BOOTSTRAP.md: template zip extracted (LICENSE/README added, PII masked, example projects removed — only ai-library-system ships), hooks activated per-clone, test suite verified 53/53, PII greps clean, and the 150-file import committed as fresh-history root commit 23eb331 with a one-time --no-verify per the v28 bulk-import precedent. MASTER-PROMPT.md is unchanged.
ARTIFACT STATE: MASTER-PROMPT.md v37 — byte-identical body to v36 (NO CHANGE relabel); the deployed root copy opens with 'ARTIFACT v37' after auto-deploy.
KEY DECISIONS:
- Only ai-library-system ships in the public template; example projects and orphaned deploys removed
- Fresh git history for the new repo — audit trail lives in the files, not git history (v28 principle)
- One-time --no-verify for the bulk import, per the v28 precedent; hook active for all subsequent commits
- flow-vs-ai and kurgan-rostok OPEN items resolved by removal in this repo line
OPEN QUESTIONS:
- Verify main was established by this checkpoint's git_sync step (first sync in a repo with no main yet)
- MAP.md's logs/git-sync.log reference vs. the gitignored, initially-absent log file
- The longer-standing v34-era items (related: warning, MAP machine-readable block, artifact-type schema, DELTA, backups, write protection, log fold, Layer 4/5)
EXPLICITLY RULED OUT:
- Nothing new this session (see v37--context.md for the full append-only list)
NEXT TASK: Verify main exists and matches the checkpoint commit, then pick a v34-era OPEN item.
PERSONA: See persona.md
STYLE AND CONSTRAINTS: Plain language. Precise. No lists where prose works better. No suggestions that contradict the established philosophy. When proposing changes to master prompt or documents, show the specific change not a full rewrite. State plan before executing any write, script, or git operation.
