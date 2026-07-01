CONTEXT v06
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
- v01 and v02 files treated as pre-schema legacy
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
- Git initialised — first commit 5a20741 on main branch
- Library stored in iCloud at ~/AI-Library (iCloud)
- RESUME procedure requires four files in order: persona.md, THREAD.md, context, instructions
- .git folder and .DS_Store excluded from MAP.md
- Post-checkpoint save instructions embedded in MASTER-PROMPT.md
- Manual verification via cat before every commit — superseded by pre-commit hook
- Pre-commit hook written, installed, and tested — operational at commit 515f792
- Triplet lockstep enforced: any vNN file staged requires all three at same version
- Version mismatch within same project folder blocks commit
- Block on structural violations; warn on advisory checks
- MAP.md integrity check: warns if referenced path does not exist on disk
- THREAD.md order check: warns if checkpoint headers are out of ascending order
- Exclusions centralised in EXCLUDED set in pre-commit script
- MASTER-PROMPT.md, ARCHITECTURE.tex, USER-GUIDE.tex, THREAD.md, persona.md excluded from MAP.md warning
- Pre-commit script self-check: not required — .py files correctly ignored by hook

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
- Newest-first ordering in THREAD.md
- Resuming from instructions file alone — insufficient context
- Blocking on MAP.md missing entry — warn only, legitimate during active sessions
- Blocking on context/instructions section headers — warn only
- Pre-commit hook checking itself — .py files have no frontmatter or vNN requirement
- Warn-only for triplet and version mismatch — both are blocking errors

OPEN:
- layer-1-foundation.md needs full rewrite
- ARCHITECTURE.tex and USER-GUIDE.tex not yet updated
- Artifact type schema for MASTER-PROMPT.md (.md prompt type) not yet formally written
- Layer 4 embedding model and vector store not yet chosen
- Remote git repository not yet set up
- Git identity (user.name and user.email) not yet configured

STATE:
- MASTER-PROMPT.md at v05, unchanged this session — no new version required
- Pre-commit hook written, tested, installed, and committed at 515f792
- Hook passes clean on MAP.md and pre-commit.py commits
- pre-commit.py added to MAP.md, committed
- Layer 1 fully operational with automated validation
- Next priority: layer-1-foundation.md rewrite or ARCHITECTURE.tex update
