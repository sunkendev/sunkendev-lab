INSTRUCTIONS v38
----------------
PROJECT: AI Document Library System
GOAL: Design, document, and iteratively refine a five-layer vendor-agnostic generational system for managing AI-generated work using plain text files and a prompt-controlled workflow.
BACKGROUND: This session redefined Layer 4 and modernised the reference documents. Layer 4's real purpose was stated and recorded: cross-project reasoning-pattern synthesis — an external, read-only repository that reads the library as a corpus (via native AI file tools, no embeddings) and produces an evidence-derived, versioned meta-persona; possible AI-training use is deferred. ARCHITECTURE was rewritten to v2.1 around that redefinition, then both reference documents were converted from LaTeX to Markdown (ARCHITECTURE.md v2.1, USER-GUIDE.md v1.1), the .tex files deleted, and the pre-commit EXCLUDED set updated (docs removed and given real frontmatter; README.md added — a gap open since the template import). Two stale manual-deploy claims in the docs were corrected to the auto-deploy reality.
ARTIFACT STATE: MASTER-PROMPT.md v38 — structure diagram lists ARCHITECTURE.md and USER-GUIDE.md; body otherwise identical to v37.
KEY DECISIONS:
- Layer 4 = cross-project reasoning-pattern synthesis in a separate external repo; reads the library, never writes it; native AI tools, no index infrastructure
- Embeddings+vector-store retrieval design retired; retrieval-by-meaning is native to any session with file tools
- Layer 4 known limits recorded: AI-mediated corpus, falsification path required, decision-policy model not cognition; growth mitigation must archive verbatim, never summarise
- Reference docs are Markdown now (v2.1/v1.1); .tex deleted; LaTeX-for-reference-docs decision reversed for living docs
- Docs carry frontmatter and left EXCLUDED; README.md entered EXCLUDED
OPEN QUESTIONS:
- Layer 4: where the synthesis output lives (observer vs contributor) and the evaluation design — both before the first synthesis run
- The longer-standing v34-era items (related: warning, MAP machine-readable block, artifact-type schema, DELTA, backups, write protection, log fold, Layer 5)
EXPLICITLY RULED OUT:
- Embeddings-based Layer 4; Layer 4 inside the library; any Layer 4 write path; 'recreate neural pathways' framing; frontmatter on README.md (see v38--context.md for the full append-only list)
NEXT TASK: When Layer 4 work begins, first settle the output-location and evaluation questions; until then, pick a v34-era OPEN item.
PERSONA: See persona.md
STYLE AND CONSTRAINTS: Plain language. Precise. No lists where prose works better. No suggestions that contradict the established philosophy. When proposing changes to master prompt or documents, show the specific change not a full rewrite. State plan before executing any write, script, or git operation.
