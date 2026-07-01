CONTEXT v02
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
- research/ and creative/ folders eliminated — not needed
- Frontmatter type field values: document | code | context
- Context file schema: PROJECT, DECISIONS, RULED OUT, OPEN, STATE — in that order
- Instructions file schema: PROJECT, GOAL, BACKGROUND, ARTIFACT STATE, KEY DECISIONS, OPEN QUESTIONS, EXPLICITLY RULED OUT, NEXT TASK, PERSONA, STYLE AND CONSTRAINTS
- DECISIONS and RULED OUT are append-only in both context and instructions files
- ORIGIN section removed from context schema — episodic history belongs in THREAD.md
- Master prompt checkpoint ritual updated to enforce context schema sections exactly
- v01 files treated as pre-schema legacy

RULED OUT:
- Any proprietary file format
- Any platform as source of truth
- Recommending specific cloud storage
- Implementing Layers 2-5 before Layer 1 is proven
- research/ and creative/ as top-level folders
- Duplicating file lists or project origin across multiple files
- PHILOSOPHY section in context files — belongs in master prompt and persona

OPEN:
- Instructions file schema not yet written into MASTER-PROMPT.md
- Artifact file schema not yet defined
- MASTER-PROMPT.md schema not yet written into a schema document
- layer-1-foundation.md needs full rewrite to match current system
- ARCHITECTURE.tex and USER-GUIDE.tex not yet updated
- Layer 3 script not yet written
- Layer 4 embedding model and vector store not yet chosen
- MAP.md machine-readable section (JSON frontmatter) not yet decided

STATE:
- MASTER-PROMPT.md is at v02, current, saved, conformant
- MAP.md is current and saved
- Context and instructions schemas are defined but only context schema is embedded in MASTER-PROMPT.md
- Instructions schema is confirmed but not yet written into MASTER-PROMPT.md checkpoint ritual
- Artifact schema not yet started
- layer-1-foundation.md is pre-schema legacy, flagged for full rewrite
- Session is at a natural checkpoint — ready to resume in fresh session
