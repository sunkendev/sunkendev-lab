INSTRUCTIONS v02
----------------
PROJECT: AI Document Library System
GOAL: Design, document, and iteratively refine a five-layer vendor-agnostic generational system for managing AI-generated work using plain text files and a prompt-controlled workflow.
BACKGROUND: Layer 1 is operational. MASTER-PROMPT.md is at v02 with updated folder structure, refined checkpoint ritual enforcing schema-conformant context output, updated frontmatter type values, and expanded instructions format. The context file schema and instructions file schema have been defined and confirmed this session. The folder structure was redesigned — docs/ and code/ now live inside each project folder; research/ and creative/ eliminated entirely. All changes are saved and MAP.md is current.
ARTIFACT STATE: MASTER-PROMPT.md v02 — complete, operational, approximately 60 lines. All six sections present: role, structure, naming, frontmatter, checkpoint ritual, navigation commands, behaviour rules. Context schema embedded in checkpoint ritual. Instructions schema embedded in checkpoint ritual.
KEY DECISIONS:
- docs/ and code/ live inside project folders, not at root
- research/ and creative/ eliminated
- Frontmatter type values trimmed to: document | code | context
- Context schema: PROJECT, DECISIONS, RULED OUT, OPEN, STATE
- Instructions schema: PROJECT, GOAL, BACKGROUND, ARTIFACT STATE, KEY DECISIONS, OPEN QUESTIONS, EXPLICITLY RULED OUT, NEXT TASK, PERSONA, STYLE AND CONSTRAINTS
- DECISIONS and RULED OUT are append-only
- ORIGIN removed from context schema — belongs in THREAD.md
- v01 files are pre-schema legacy
OPEN QUESTIONS:
- Should instructions schema be explicitly embedded in MASTER-PROMPT.md checkpoint ritual (it is implied but not shown as labelled sections)?
- Artifact schema not yet defined — what sections does an artifact file require?
- Should MAP.md have a JSON frontmatter block for Layer 4 indexing?
- Layer 3 script: Python or shell?
- Layer 4: which embedding model and vector store?
EXPLICITLY RULED OUT:
- Any proprietary file format
- Any platform as source of truth
- Specific cloud storage recommendations
- Layers 2-5 before Layer 1 is stable
- research/ and creative/ as top-level folders
- PHILOSOPHY section in context files
- Duplicating origin or file lists across multiple files
NEXT TASK: Define the artifact file schema. Then embed the instructions schema explicitly into MASTER-PROMPT.md checkpoint ritual block 3. Then scope the layer-1-foundation.md rewrite.
PERSONA: Systems architect specialising in knowledge management and AI workflow design. Rigorous, direct, no padding, no tool suggestions unless asked.
STYLE AND CONSTRAINTS: Plain language. Precise. No lists where prose works better. No suggestions that contradict the established philosophy. When proposing changes to the master prompt or documents, show the specific change, not a full rewrite.
