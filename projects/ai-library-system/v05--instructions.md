INSTRUCTIONS v05
----------------
PROJECT: AI Document Library System
GOAL: Design, document, and iteratively refine a five-layer vendor-agnostic generational system for managing AI-generated work using plain text files and a prompt-controlled workflow.
BACKGROUND: Layer 1 is fully operational. All seven schemas are defined and saved. Git is initialised on main branch. RESUME procedure corrected this session — a full resume now requires four files pasted in order: persona.md, THREAD.md, context, instructions. Post-checkpoint save instructions and manual verification step are embedded in MASTER-PROMPT.md. Pre-commit validation script is the next major deliverable.
ARTIFACT STATE: MASTER-PROMPT.md v05 — complete, operational, all seven sections present, all checkpoint schemas embedded, corrected RESUME procedure. Approximately 70 lines.
KEY DECISIONS:
- All seven file schemas defined and confirmed
- Artifact wrapper schema: LABEL, VERSION MATCH, EXTENSION MATCH, NON-EMPTY BODY
- Artifact type schemas defined at time of first use
- THREAD.md entries in ascending order for AI context loading
- THREAD.md status values: active | paused | complete | archived
- Latest checkpoint derived from last log entry not stored separately
- MAP.md has no META section, excludes .git and .DS_Store
- persona.md: ROLE, DOMAIN, BEHAVIOUR, EXAMPLES — all mandatory, no frontmatter
- Git as Layer 3 foundation — local first, remote later
- Pre-commit hook as validation mechanism
- vNN prefix retained alongside git history
- Checkpoint = major milestone; routine sessions = git commits only
- Git initialised — commit 5a20741 on main branch
- Library path: ~/AI-Library (iCloud)
- RESUME requires four files in order: persona.md, THREAD.md, context, instructions
- Manual cat verification before every commit until pre-commit hook exists
OPEN QUESTIONS:
- Pre-commit validation script not yet written
- layer-1-foundation.md needs full rewrite
- ARCHITECTURE.tex and USER-GUIDE.tex not yet updated
- Artifact type schema for .md prompt type not yet formally written
- Layer 4 embedding model and vector store not yet chosen
- Remote git repository not yet set up
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
- Resuming from instructions file alone
NEXT TASK: Write the pre-commit validation script in Python. It checks: vNN naming on project files, valid YAML frontmatter on standalone files, complete checkpoint triplets, conformant context and instructions section headers, every file in the folder has a MAP.md entry, .git and .DS_Store excluded. Save to projects/ai-library-system/code/pre-commit.py. Then wire as .git/hooks/pre-commit.
PERSONA: See persona.md
STYLE AND CONSTRAINTS: Plain language. Precise. No lists where prose works better. No suggestions that contradict the established philosophy. When proposing changes to master prompt or documents, show the specific change not a full rewrite.
