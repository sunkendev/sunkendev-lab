CONTEXT v03
-----------
PROJECT: AI Document Library System — a five-layer vendor-agnostic plain-text library for managing AI-generated work.

DECISIONS:
- Plain Markdown as universal format
- YAML frontmatter as metadata standard
- Two-digit version numbers (v01...v99) for correct lexicographic sort
- Three-file checkpoint triplet: artifact, context, instructions
- THREAD.md as project spine, one per project folder
- MAP.md at library root as single traversal index
- Master prompt as sole control mechanism
- Layer 1 mandatory; all other layers optional and additive
- Library folder is storage-agnostic
- LaTeX for formal reference documents
- docs/ and code/ live inside each project folder, not at root
- inbox/ is the only non-project folder at root besides MAP.md and reference docs
- research/ and creative/ folders eliminated
- Frontmatter type field values: document | code | context
- Context file schema: PROJECT, DECISIONS, RULED OUT, OPEN, STATE — in that order
- Instructions file schema: PROJECT, GOAL, BACKGROUND, ARTIFACT STATE, KEY DECISIONS, OPEN QUESTIONS, EXPLICITLY RULED OUT, NEXT TASK, PERSONA, STYLE AND CONSTRAINTS
- DECISIONS and RULED OUT are append-only in both context and instructions files
- ORIGIN removed from context schema — episodic history belongs in THREAD.md
- Master prompt checkpoint ritual updated to enforce all three block schemas
- v01 files treated as pre-schema legacy
- Artifact wrapper schema: LABEL, VERSION MATCH, EXTENSION MATCH, NON-EMPTY BODY
- Artifact type schemas defined per type at time of first use
- THREAD.md schema: TITLE, STARTED, DESCRIPTION, PERSONA, CHECKPOINT LOG — ascending order
- THREAD.md status values: active | paused | complete | archived
- Latest checkpoint derived from last log entry, not stored in META
- MAP.md schema: TITLE, ROOT, PROJECTS — no META, no duplicate entries
- persona.md schema: ROLE, DOMAIN, BEHAVIOUR, EXAMPLES — all mandatory
- persona.md has no frontmatter — it is a project file not a standalone document
- VOICE and CONSTRAINTS merged into BEHAVIOUR in persona.md schema
- EXAMPLES mandatory in persona.md — specific detailed personas outperform generic ones
- Git as foundation for Layer 3 — local git first, remote later
- Pre-commit hook as primary validation mechanism
- vNN prefix retained for human readability alongside git history
- Checkpoint = major milestone commit; routine sessions = git commits without full triplet

RULED OUT:
- Any proprietary file format
- Any platform as source of truth
- Recommending specific cloud storage
- Implementing Layers 2-5 before Layer 1 is proven
- research/ and creative/ as top-level folders
- PHILOSOPHY section in context files
- Duplicating origin or file lists across multiple files
- META section in THREAD.md and MAP.md — derived from content or git
- Optional sections in schemas — either mandatory or absent
- VOICE and CONSTRAINTS as separate sections in persona.md
- Ascending-order changelog (newest first) — AI context loading requires oldest first

OPEN:
- Schema reference document not yet created in projects/ai-library-system/docs/
- layer-1-foundation.md needs full rewrite
- ARCHITECTURE.tex and USER-GUIDE.tex not yet updated
- Layer 3 validation script not yet written
- Layer 4 embedding model and vector store not yet chosen
- Artifact type schema for MASTER-PROMPT.md (.md prompt type) not yet formally written
- git not yet initialised

STATE:
- MASTER-PROMPT.md is at v03, current, saved, conformant
- All seven schemas defined and confirmed
- persona.md updated to four-section schema with EXAMPLES
- THREAD.md updated to correct status value and schema-conformant header
- MAP.md current and saved
- v01 and v02 files are pre-schema legacy — valid historical record
- Next immediate task: create schema reference document, then git init
