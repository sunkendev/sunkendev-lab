INSTRUCTIONS v31
----------------
PROJECT: AI Document Library System
GOAL: Design, document, and iteratively refine a five-layer vendor-agnostic generational system for managing AI-generated work using plain text files and a prompt-controlled workflow.
BACKGROUND: This session rewrote ARCHITECTURE.tex (v2.0) and USER-GUIDE.tex (v1.0) from scratch, per explicit instruction to archive the old versions and rewrite Layers 1-3 with rigor while carrying Layers 4-5 forward unchanged (they describe unbuilt capability, so there is nothing to drift against). After the rewrite, the user asked whether the new documents' logic holds and can be used to derive a spec — triggering three successive critique re-reads. The first found four real mismatches between the docs and the actual scripts (post-write integrity checks misdescribed as pre-write, THREAD-order check misattributed to checkpoint.py instead of pre-commit.py, a fabricated related: field check, and an overstated MAP-coverage scope), plus a genuine bug in checkpoint.py itself (the artifact file extension was hardcoded to .md, which would silently mis-save any non-Markdown artifact). All four doc issues and the code bug were fixed, the fix was verified end to end with a synthetic .tex-artifact test project, and the deployed/source copies of checkpoint.py were kept in sync. The second and third critique passes, done at the user's request to re-check the just-committed fix, found that the first pass's own corrections had introduced a new inaccuracy (overstating which checks in checkpoint.py can block a run) and had missed five separate instances of a different overstatement (describing RESUME as reading "the latest triplet" when it never reads the artifact file). All were found and fixed.
ARTIFACT STATE: MASTER-PROMPT.md v31 — NO CHANGE, relabelled from v30. No edits to MASTER-PROMPT.md this session; all work was on ARCHITECTURE.tex, USER-GUIDE.tex, and checkpoint.py.
KEY DECISIONS:
- ARCHITECTURE.tex and USER-GUIDE.tex rewritten from scratch rather than amended in place; originals archived to docs/ as the historical record
- LaTeX files needing frontmatter-equivalent metadata use a %-commented block before \documentclass, since YAML --- breaks compilation
- checkpoint.py's artifact extension is now resolved by inheriting it from the previous version's artifact file on disk (resolve_artifact_extension() / find_artifact_path()), defaulting to .md only when there is no previous version
- Documentation claims about script behaviour must be checked directly against current source, every time, including re-checking one's own prior fix — this caught two further rounds of self-introduced errors in this session alone
KEY QUESTIONS:
OPEN QUESTIONS:
- Which OPEN item to pick up next: candidates include the flow-vs-ai temp/ cleanup, the related: bare-filename pre-commit warning, MAP.md machine-readable block, Artifact type schema for MASTER-PROMPT.md, or starting Layer 4 (embedding model / vector store selection)
- Whether checkpoint.py warrants an automated test suite now that it has accumulated several non-trivial behaviours (NO CHANGE sentinel, extension inheritance, integrity checks) that have so far only been verified manually per change
EXPLICITLY RULED OUT:
- Treating documentation claims as correct without verifying against current script source — every claim in this session's three critique passes was checked directly against checkpoint.py/pre-commit.py
- (Plus all prior ruled-out items — see v31--context.md)
NEXT TASK: Pick the next OPEN item to work, or continue ad hoc per user direction. No specific task assigned beyond this checkpoint.
PERSONA: See persona.md
STYLE AND CONSTRAINTS: Plain language. Precise. No lists where prose works better. No suggestions that contradict the established philosophy. When proposing changes to master prompt or documents, show the specific change not a full rewrite. State plan before executing any write, script, or git operation.
