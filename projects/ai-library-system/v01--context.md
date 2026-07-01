CONTEXT v01
-----------
PROJECT: AI Document Library System

ORIGIN: This system was designed in a single extended conversation on
2026-04-11 starting from the user's stated requirements: a permanent
library of AI-generated documents, ability to resume work across
different AI vendors and models, full control from the prompt, and
generational durability.

CORE PHILOSOPHY ESTABLISHED:
- The file is the truth, not the application
- Plain text in open formats survives any tool change
- Metadata lives inside the file via YAML frontmatter, never in a database
- The checkpoint ritual externalises memory before context degrades
- The versioned triplet (artifact + context + instructions) captures
  three distinct types of knowledge at each save point
- THREAD.md provides the narrative arc of intellectual progression
- MAP.md provides Yahoo-style directory + Google-style snippets +
  Wikipedia-style thread linking

FIVE LAYERS DEFINED:
Layer 1 — Foundation: plain text files, naming conventions, master prompt,
  manual checkpoint ritual. No dependencies. Mandatory.
Layer 2 — Session: platform workspaces (Claude Projects). Reduces startup
  friction. Does not replace Layer 1 as permanent record.
Layer 3 — Automation: checkpoint.py script, update-map.py. Eliminates
  manual copy-paste. Requires API access and basic scripting.
Layer 4 — Retrieval: embedding model + vector store. Semantic search
  across library. Automatic context loading via RAG.
Layer 5 — Orchestration: MCP integration, scheduled sessions,
  cross-project synthesis, team infrastructure, pipeline automation.

DOCUMENTS PRODUCED IN THIS SESSION:
- MAP.md template
- README-folder-template.md
- orchestration-workflow.md
- layer-1-foundation.md
- MASTER-PROMPT.md (operative system prompt)
- MASTER-PROMPT.tex + PDF (9 pages, component reference + raw prompt)
- USER-GUIDE.tex + PDF (26 pages, complete Layer 1 reference)
- ARCHITECTURE.tex + PDF (25 pages, complete 5-layer reference)

KEY DECISIONS MADE:
- Plain Markdown (.md) as the universal file format
- YAML frontmatter as the metadata standard
- Two-digit version numbers (v01...v99) for correct lexicographic sort
- Three-file checkpoint triplet (artifact, context, instructions)
- THREAD.md as project spine, one per project folder
- MAP.md at library root as single traversal index
- Master prompt as the sole control mechanism — no app required
- Layer 1 is mandatory; all other layers are optional and additive
- The library folder is storage-agnostic (iCloud, Google Drive, local, etc.)
- LaTeX as the format for formal reference documents
- This conversation is itself the first project in the library

VENDOR COMPARISON CONDUCTED:
Responses from ChatGPT, Perplexity, Gemini, and Grok were reviewed.
All four independently converged on plain text / Markdown as the
vendor-agnostic foundation — validating the philosophy. None had:
versioned triplets, THREAD.md narrative logs, shareable project folders,
or an explicit checkpoint ritual. Gemini raised MCP as the key Layer 3/5
automation standard. This was incorporated into the architecture.

OPEN QUESTIONS:
- Layer 3 script has not yet been written (design only)
- Layer 4 embedding model and vector store not yet chosen
- Layer 5 MCP configuration not yet implemented
- MAP.md for this library not yet populated
- Existing user files in inbox not yet sorted

EXPLICITLY RULED OUT:
- Any proprietary format (Word, Notion, Evernote, etc.)
- Any app or platform as the source of truth
- Any approach that requires an account or subscription to read files
- Recommending a specific cloud storage provider
- Implementing any layer before Layer 1 is stable
