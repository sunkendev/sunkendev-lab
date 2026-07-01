INSTRUCTIONS v30
----------------
PROJECT: AI Document Library System
GOAL: Design, document, and iteratively refine a five-layer vendor-agnostic generational system for managing AI-generated work using plain text files and a prompt-controlled workflow.
BACKGROUND: Following the v28 GitHub fork and the v29 toolchain spike, this session asked whether the SHA-256 manifest/tamper-detection mechanism in checkpoint.py was still needed now that the library lives on a durable GitHub remote. Conclusion: no — git's commit history already provides full-diff, append-only change tracking with no cross-project blind spot, which is strictly more than the manifest ever gave. The mechanism was removed end to end from checkpoint.py (both the source and deployed copies), the .gitignore exception for manifest files was dropped, and the MASTER-PROMPT.md temp/ folder convention was updated to match. The code change was committed separately (ba0292c) ahead of this checkpoint, consistent with the rule that MASTER-PROMPT.md itself only changes through the checkpoint ritual. Historical manifest files were left untouched as archived audit records.
ARTIFACT STATE: MASTER-PROMPT.md v30 — one wording change from v28/v29: the temp/ folder convention entry no longer names v[NN]-[slug]-manifest.json. All other sections unchanged. The root MASTER-PROMPT.md file is also resynced to the current label (it had drifted to a stale "ARTIFACT v28" label after the v29 NO CHANGE relabel was applied only to the project copy).
KEY DECISIONS:
- SHA-256 manifest/tamper-detection removed entirely from checkpoint.py — GitHub's durable commit history makes it redundant for its original purpose
- write_checkpoint_log() and copy_and_relabel_artifact() kept — unrelated to the manifest mechanism
- Label/separator validation, DECISIONS/RULED OUT superset check, and size-ratio checks kept — they catch write-time bugs in checkpoint.py itself, which git diff cannot prevent
- .gitignore's !temp/*-manifest.json exception removed
- 19 historical manifest JSON files left in place as archived audit records — removal is forward-looking only
- MASTER-PROMPT.md temp/ convention updated to drop the manifest filename reference
OPEN QUESTIONS:
- ARCHITECTURE.tex / USER-GUIDE.tex updates, related: bare-filename hook warning, MAP.md machine-readable block, DELTA design, and the remaining OPEN items from v29 (see v30--context.md OPEN section) are all still pending and unprioritised
EXPLICITLY RULED OUT:
- Fixing the cross-project tamper-detection blind spot by comparing against the most recent manifest across all projects — would rebuild what git already does, worse
- Keeping the manifest as a redundant secondary layer alongside GitHub history — no offsetting benefit, only maintenance cost and false positives
- Deleting the historical manifest files — they are already-committed audit records, not live state
- (Plus all prior ruled-out items — see v30--context.md)
NEXT TASK: Pick the next OPEN item to work — likely candidates are the flow-vs-ai temp/ cleanup (small, well-scoped) or starting the ARCHITECTURE.tex/USER-GUIDE.tex reconciliation (larger, overdue since v15-era integrity-stack documentation drifted from current reality).
PERSONA: See persona.md
STYLE AND CONSTRAINTS: Plain language. Precise. No lists where prose works better. No suggestions that contradict the established philosophy. When proposing changes to master prompt or documents, show the specific change not a full rewrite. State plan before executing any write, script, or git operation.
