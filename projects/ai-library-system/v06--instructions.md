INSTRUCTIONS v06
----------------
PROJECT: AI Document Library System
GOAL: Design, document, and iteratively refine a five-layer vendor-agnostic generational system for managing AI-generated work using plain text files and a prompt-controlled workflow.
BACKGROUND: Layer 1 is fully operational with automated validation. The pre-commit hook is written in Python, installed at .git/hooks/pre-commit, tested, and committed. It blocks on structural violations (triplet lockstep, version mismatch, malformed frontmatter, vNN naming) and warns on advisory checks (MAP.md coverage, MAP.md path integrity, THREAD.md order, section headers). MASTER-PROMPT.md is unchanged at v05 — no new artifact version was produced this session. The artifact at v06 is identical to v05 but the context and instructions reflect the completed hook work.
ARTIFACT STATE: MASTER-PROMPT.md v06 — identical to v05, complete and operational. All seven sections present, all schemas embedded. Approximately 70 lines. pre-commit.py at projects/ai-library-system/code/pre-commit.py — 337 lines, fully operational.
KEY DECISIONS:
- Pre-commit hook operational at commit 515f792
- Triplet lockstep: any vNN file staged requires all three at same version (block)
- Version mismatch within same project folder blocks commit
- Block on structural violations; warn on advisory checks
- MAP.md integrity check warns if referenced path missing on disk
- THREAD.md order check warns if headers out of ascending order
- Exclusions centralised in EXCLUDED set — one place to maintain
- Pre-commit script does not check itself — .py files correctly ignored
- Git identity not yet configured — cosmetic issue only
OPEN QUESTIONS:
- layer-1-foundation.md needs full rewrite
- ARCHITECTURE.tex and USER-GUIDE.tex not yet updated
- Artifact type schema for .md prompt type not yet formally written
- Layer 4 embedding model and vector store not yet chosen
- Remote git repository not yet set up
- Git identity (user.name and user.email) not yet configured
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
- Blocking on MAP.md missing entry — warn only
- Blocking on section header checks — warn only
- Pre-commit hook checking itself
- Warn-only for triplet or version mismatch — these are hard blocks
NEXT TASK: Rewrite layer-1-foundation.md. The current file is pre-schema legacy. The rewrite should conform to the standalone file frontmatter schema, cover the Layer 1 philosophy, folder structure, file naming rules, frontmatter schema, checkpoint triplet, and the role of the pre-commit hook. Save to projects/ai-library-system/docs/layer-1-foundation.md.
PERSONA: See persona.md
STYLE AND CONSTRAINTS: Plain language. Precise. No lists where prose works better. No suggestions that contradict the established philosophy. When proposing changes to master prompt or documents, show the specific change not a full rewrite.
