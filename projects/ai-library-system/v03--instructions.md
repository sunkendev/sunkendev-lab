INSTRUCTIONS v03
----------------
PROJECT: AI Document Library System
GOAL: Design, document, and iteratively refine a five-layer vendor-agnostic generational system for managing AI-generated work using plain text files and a prompt-controlled workflow.
BACKGROUND: Layer 1 is operational and schema work is complete. All seven file schemas have been defined and confirmed this session: MASTER-PROMPT.md, context, instructions, artifact wrapper, THREAD.md, MAP.md, and persona.md. MASTER-PROMPT.md is at v03 with artifact wrapper schema embedded. persona.md and THREAD.md have been updated to conform to their schemas. Git has been selected as the Layer 3 foundation with a pre-commit validation hook as the primary enforcement mechanism.
ARTIFACT STATE: MASTER-PROMPT.md v03 — complete, operational, all seven sections present, all three checkpoint block schemas embedded. Approximately 65 lines.
KEY DECISIONS:
- All seven file schemas defined and confirmed
- Artifact wrapper schema: LABEL, VERSION MATCH, EXTENSION MATCH, NON-EMPTY BODY
- Artifact type schemas defined at time of first use
- THREAD.md entries in ascending order for AI context loading
- THREAD.md status values: active | paused | complete | archived
- Latest checkpoint derived from last log entry not stored separately
- MAP.md has no META section
- persona.md: ROLE, DOMAIN, BEHAVIOUR, EXAMPLES — all mandatory, no frontmatter
- Git as Layer 3 foundation — local first, remote later
- Pre-commit hook as validation mechanism
- vNN prefix retained alongside git history
- Checkpoint = major milestone; routine sessions = git commits only
OPEN QUESTIONS:
- Schema reference document not yet saved to projects/ai-library-system/docs/
- layer-1-foundation.md needs full rewrite
- ARCHITECTURE.tex and USER-GUIDE.tex not yet updated
- Layer 3 validation script not yet written
- Artifact type schema for .md prompt type not yet formally written
- Layer 4 embedding model and vector store not yet chosen
EXPLICITLY RULED OUT:
- Any proprietary file format
- Any platform as source of truth
- Specific cloud storage recommendations
- Layers 2-5 before Layer 1 is stable
- research/ and creative/ as top-level folders
- PHILOSOPHY section in context files
- META sections in THREAD.md and MAP.md
- Optional sections in any schema
- Newest-first ordering in THREAD.md
NEXT TASK: Create schema reference document in projects/ai-library-system/docs/ containing all seven confirmed schemas. Save as 2026-04-11--schemas--claude.md. Then git init.
PERSONA: See persona.md
STYLE AND CONSTRAINTS: Plain language. Precise. No lists where prose works better. No suggestions that contradict the established philosophy. When proposing changes to master prompt or documents, show the specific change not a full rewrite.
