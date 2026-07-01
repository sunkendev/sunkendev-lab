INSTRUCTIONS v36
----------------
PROJECT: AI Document Library System
GOAL: Design, document, and iteratively refine a five-layer vendor-agnostic generational system for managing AI-generated work using plain text files and a prompt-controlled workflow.
BACKGROUND: This short session reversed v35's label-strip: the deployed MASTER-PROMPT.md now carries its self-describing 'ARTIFACT vNN' label verbatim, because that label is load-bearing (it shows the live version and keeps the file consistent with the self-describing-artifact convention). The staleness that motivated stripping is already handled by auto-deploy plus the regenerate-and-diff guard, so keeping the label is both correct and simpler. checkpoint.py and pre-commit.py now copy/compare verbatim (strip helper removed), SKILL.md is at v11, and the live file was healed by this checkpoint's own verbatim deploy.
ARTIFACT STATE: MASTER-PROMPT.md v36 — ritual save-step 3 reworded to 'artifact verbatim'; the deployed root copy is byte-identical to v36--artifact.md and opens with 'ARTIFACT v36'.
KEY DECISIONS:
- Deploy is verbatim; the 'ARTIFACT vNN' label is load-bearing and kept (reverses v35)
- The regression was staleness, not the label; auto-deploy + guard fix staleness, so the label is safe to keep
- strip_artifact_label removed; deploy = literal copy, guard = literal compare; suite at 53
OPEN QUESTIONS:
- flow-vs-ai code/ disposition (inverted source-of-truth) — best handled in a flow-vs-ai session
- Whether to add an eval/quality gate before a MASTER-PROMPT.md deploy
- The longer-standing v34-era items (related: warning, MAP machine-readable block, artifact-type schema, DELTA, backups, write protection, log fold, Layer 4/5)
EXPLICITLY RULED OUT:
- Stripping the ARTIFACT label from the deployed MASTER-PROMPT.md (reverses v35); the manual cp; the weaker prefix-only guard; inverting source to root MASTER-PROMPT.md
- Deleting the flow-vs-ai code/ orphans as cleanup (unsourced project deliverables)
- (Plus all prior ruled-out items — see v36--context.md)
NEXT TASK: Decide the flow-vs-ai code/ disposition (likely by RESUMING flow-vs-ai), or pick another v34-era OPEN item.
PERSONA: See persona.md
STYLE AND CONSTRAINTS: Plain language. Precise. No lists where prose works better. No suggestions that contradict the established philosophy. When proposing changes to master prompt or documents, show the specific change not a full rewrite. State plan before executing any write, script, or git operation.
