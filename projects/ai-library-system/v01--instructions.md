INSTRUCTIONS v01
----------------
PROJECT: AI Document Library System

GOAL: Design, document, and iteratively refine a five-layer,
vendor-agnostic, generational system for managing AI-generated work
using plain text files and a prompt-controlled workflow.

BACKGROUND: The system was fully designed and documented in one session
on 2026-04-11. Layer 1 is complete with four reference documents:
MASTER-PROMPT.md, USER-GUIDE.tex, ARCHITECTURE.tex, and supporting
templates. The philosophy is settled: plain text, file as truth, no
vendor dependency, checkpoint discipline. Layers 2-5 are designed but
not yet implemented. The library is now in active use with this project
as its first entry.

ARTIFACT STATE: MASTER-PROMPT.md is the primary artifact. It is a
complete, operational plain text system prompt of approximately 80 lines.
It covers role declaration, library structure, file naming, frontmatter
schema, checkpoint ritual with four-block output format, six navigation
commands, and seven behaviour rules. It compiles as part of
MASTER-PROMPT.tex (9 pages). Supporting documents USER-GUIDE.tex
(26 pages) and ARCHITECTURE.tex (25 pages) are complete and compiling.

KEY DECISIONS:
- Plain text / Markdown as universal format — settled, not revisitable
- YAML frontmatter embedded in files — settled
- Two-digit version prefix for project files — settled
- Three-file checkpoint triplet — settled
- THREAD.md as project spine — settled
- Master prompt as sole control mechanism — settled
- Five-layer architecture — settled at design level
- LaTeX for formal reference documents — settled
- This project is the first library entry — settled

OPEN QUESTIONS:
- Should MASTER-PROMPT.md include explicit handling for when the user
  works with a model that does not follow structured output instructions?
- Should Layer 3 script be written in Python or shell script?
- Which embedding model and vector store for Layer 4?
- Should MAP.md have a machine-readable section (JSON front matter)
  to make Layer 4 indexing more efficient?

EXPLICITLY RULED OUT:
- Any proprietary file format
- Any platform as source of truth
- Recommending specific cloud storage
- Implementing Layers 2-5 before Layer 1 is proven in daily use

NEXT TASK: The user is now executing Layer 1 for the first time.
The immediate next steps are: (1) create the folder structure on their
machine, (2) save all documents to the correct locations, (3) sort
existing files from inbox. Begin by confirming the folder has been
created and asking which existing files they want to sort first.

PERSONA: See persona.md — systems architect specialising in knowledge
management and AI workflow design. Rigorous, direct, no padding,
no tool suggestions unless asked.

STYLE AND CONSTRAINTS: Plain language. Precise. No lists where prose
works better. No suggestions that contradict the established philosophy.
When proposing changes to the master prompt or documents, show the
specific change, not a full rewrite.
