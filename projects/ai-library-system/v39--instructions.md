INSTRUCTIONS v39
----------------
PROJECT: AI Document Library System
GOAL: Design, document, and iteratively refine a five-layer vendor-agnostic generational system for managing AI-generated work using plain text files and a prompt-controlled workflow.
BACKGROUND: The post-v38 stretch of this session was a governance post-mortem. Three approval-prompt failures were traced to timed-out permission requests while the user was away; the proposed committed allowlist was rejected (human approval stays at the tool layer). v38's checkpoint input was found to have been assembled by an ad-hoc scratchpad script — verified harmless on disk, but ruled a process violation: checkpoints are now produced 100% natively, and this v39 checkpoint adds the enforcement to the kernel (letter-of-procedure rule, narrate-method rule, direct-output ritual clause) plus a matching persona.md line, itself produced natively as the demonstration. Also this stretch: context thresholds ruled stale against 1M windows (ratios, not absolutes; config table and compression-probe skill proposed), the stranded v37 bootstrap NOTE recovered via the front door, and the GitHub default branch flipped to main.
ARTIFACT STATE: MASTER-PROMPT.md v39 — two behaviour rules and one checkpoint-ritual clause added; structure diagram and all other content unchanged from v38.
KEY DECISIONS:
- No permission allowlist — every privileged command stays behind live human approval; verify git state before retrying any dropped git step
- Checkpoints 100% native: all four blocks are direct AI output; ad-hoc block-content scripts banned; kernel enforces by letter plus mandatory method-narration
- v38 verified uncorrupted (exact-prefix superset, three-line artifact diff, byte-identical deploy) and stands; ruling applies forward
- Context thresholds are ratios of a per-environment window, never absolutes; window config table and compression-probe skill proposed
- Layer 4 remains: external read-only synthesis repo (v38 decisions unchanged)
OPEN QUESTIONS:
- Which next: git_sync fresh-repo fix, window config table, compression-probe skill, orphaned-NOTE mitigation, BOOTSTRAP.md reconstruction, DELTA, or a v34-era item
- Layer 4 output location (observer vs contributor) and evaluation design — before any first synthesis run
EXPLICITLY RULED OUT:
- Permission allowlist; ad-hoc scripts on checkpoint block content; cherry-picking the stranded NOTE; redoing v38 (see v39--context.md for the full append-only list)
NEXT TASK: Pick one of the new OPEN items — the git_sync.py fresh-repo fix and the window config table are the most mechanical — or a v34-era backlog item; confirm the six post-v38 NOTEs reached main with this checkpoint's sync.
PERSONA: See persona.md
STYLE AND CONSTRAINTS: Plain language. Precise. No lists where prose works better. No suggestions that contradict the established philosophy. When proposing changes to master prompt or documents, show the specific change not a full rewrite. State plan before executing any write, script, or git operation. Follow documented procedures by the letter; propose improvements, never adopt them unilaterally; narrate method, not only outcome.
