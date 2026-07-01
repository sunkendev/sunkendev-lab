INSTRUCTIONS v07
----------------
PROJECT: AI Document Library System
GOAL: Design, document, and iteratively refine a five-layer vendor-agnostic generational system for managing AI-generated work using plain text files and a prompt-controlled workflow.
BACKGROUND: Layer 1 is fully operational with pre-commit validation. Layer 2 is designed, documented, and ready for platform testing. The NOTE format has been added to THREAD.md schema and MASTER-PROMPT.md for inter-checkpoint working notes. A significant architectural decision was settled this session: projects/ai-library-system/ is the control panel for the library — scripts developed there, deployed to scripts/ at library root. The system was validated against cloud-native alternatives (Azure Foundry, AWS Bedrock, JetBrains) and found to be superior for personal use on privacy, IP ownership, cost, and generational durability grounds.
ARTIFACT STATE: MASTER-PROMPT.md v07 — complete, operational, NOTE format added. Approximately 75 lines. Reference documents: 2026-04-11--layer-1-foundation--claude.md and 2026-04-11--layer-2-session--claude.md both written and committed.
KEY DECISIONS:
- NOTE format added to THREAD.md schema: NOTE YYYY-MM-DD, Topic, prose — no triplet required
- scripts/ at library root for deployed operational scripts
- projects/ai-library-system/code/ is source; scripts/ is deployment target
- projects/ai-library-system/ is the control panel for the entire library
- Layer 2 is consumer app tier only — API cost prohibitive
- System prompt position gives standing instructions structural priority
- Layer 2 session start still requires all four RESUME files
- ARCHITECTURE.tex and USER-GUIDE.tex deferred until system is scripted live
- Cloud-native alternatives evaluated and ruled out for personal use
OPEN QUESTIONS:
- Layer 2 platform experiment not yet run
- scripts/ folder not yet created at library root
- pre-commit.py not yet deployed to scripts/
- NOTE format not yet added to layer-1-foundation document
- ARCHITECTURE.tex discrepancies not yet corrected
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
- Resuming from instructions file alone
- Blocking on MAP.md missing entry — warn only
- Blocking on section header checks — warn only
- Pre-commit hook checking itself
- Warn-only for triplet or version mismatch — hard blocks
- Remote git for now
- API tier for Layers 1 and 2
- Updating ARCHITECTURE.tex and USER-GUIDE.tex before scripted live
- Layer 2 session start simplification — deferred to library optimisations
- Cloud-native platforms (Azure Foundry, AWS Bedrock) for personal library use
NEXT TASK: Create scripts/ folder at library root. Deploy pre-commit.py from projects/ai-library-system/code/ to scripts/. Update MAP.md to add scripts/ section. Then run Layer 2 platform experiment — set up Claude Project with MASTER-PROMPT.md and persona.md in system prompt, run one full session with four-file RESUME, and note any behavioural differences.
PERSONA: See persona.md
STYLE AND CONSTRAINTS: Plain language. Precise. No lists where prose works better. No suggestions that contradict the established philosophy. When proposing changes to master prompt or documents, show the specific change not a full rewrite.
