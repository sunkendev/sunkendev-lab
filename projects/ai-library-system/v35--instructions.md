INSTRUCTIONS v35
----------------
PROJECT: AI Document Library System
GOAL: Design, document, and iteratively refine a five-layer vendor-agnostic generational system for managing AI-generated work using plain text files and a prompt-controlled workflow.
BACKGROUND: This session diagnosed the MASTER-PROMPT.md label-leak regression (a dormant deploy-cp leak that went live at v28 when Layer 2 moved to CLAUDE.md @-import, then froze its version across NO-CHANGE checkpoints), and fixed it at the mechanism level: checkpoint.py now auto-deploys the label-stripped artifact body via a declarative .deploy marker, a regenerate-and-diff pre-commit guard enforces deploy/source parity, and SKILL.md's old manual cp was removed. A full v34 system audit, MAP.md staleness fixes, the pre-commit hook wiring, and a new pre-commit test suite also landed. The live MASTER-PROMPT.md is healed by this checkpoint's own auto-deploy.
ARTIFACT STATE: MASTER-PROMPT.md v35 — checkpoint-ritual save-step 3 rewritten to describe the automatic, label-stripping deploy; the deployed root copy is now unversioned (body only) and current.
KEY DECISIONS:
- Deployed MASTER-PROMPT.md is the label-stripped artifact body; the version lives in the triplet/THREAD/git
- checkpoint.py auto-deploys via a per-project .deploy marker on every checkpoint, NO CHANGE included
- pre-commit regenerate-and-diff guard enforces deployed == strip(latest artifact), scoped to staged prompt source/output
- ai-library-ops SKILL.md v10 removes the re-leaking manual cp; suite at 64 tests including new test_pre_commit.py
OPEN QUESTIONS:
- Disposition of the flow-vs-ai code/ orphans (inverted source-of-truth) — best handled in a flow-vs-ai session
- Whether to add an eval/quality gate before a new MASTER-PROMPT.md deploys
- The longer-standing v34-era items (related: warning, MAP machine-readable block, artifact-type schema, DELTA, backups, write protection, log fold, Layer 4/5)
EXPLICITLY RULED OUT:
- Manual cp deploy of MASTER-PROMPT.md (re-leaks the label; skipped on NO-CHANGE) — replaced by auto-deploy
- A versioned banner in the deployed file; the weaker prefix-only guard; inverting source to root MASTER-PROMPT.md
- Deleting the flow-vs-ai code/ orphans as cleanup (they are unsourced project deliverables)
- (Plus all prior ruled-out items — see v35--context.md)
NEXT TASK: Decide the flow-vs-ai code/ disposition (most likely by RESUMING flow-vs-ai and repairing its source-of-truth), or pick another v34-era OPEN item.
PERSONA: See persona.md
STYLE AND CONSTRAINTS: Plain language. Precise. No lists where prose works better. No suggestions that contradict the established philosophy. When proposing changes to master prompt or documents, show the specific change not a full rewrite. State plan before executing any write, script, or git operation.
