---
title: AI Library System — File Schemas
date: 2026-04-11
updated: 2026-04-11
type: document
vendor: claude
model: claude-sonnet-4-6
tags: [schemas, layer-1, validation]
related: [MASTER-PROMPT.md, layer-1-foundation.md]
---

# AI Library System — File Schemas

All schemas confirmed 2026-04-11. These are the authoritative definitions
for all file types in the library. The Layer 3 validation script checks
against these schemas at commit time.

---

## 1. MASTER-PROMPT.md

Sections (in order, all mandatory):
1. ROLE          — one paragraph, declares AI identity and constraints
2. STRUCTURE     — folder tree, exact format
3. NAMING        — file naming rules, version format, standalone format
4. FRONTMATTER   — YAML block, all fields, valid values per field
5. CHECKPOINT    — ritual definition, block count, block formats in order
6. COMMANDS      — navigation commands, one per line, exact syntax
7. BEHAVIOUR     — rules list, negative constraints only

Rules:
- Sections must appear in this order
- No section may be omitted
- No section may be merged with another
- Each command in COMMANDS must have a one-line description
- BEHAVIOUR rules are stated as prohibitions

---

## 2. Context File (v[NN]--context.md)

Sections (in order, all mandatory):
1. PROJECT       — name and one-line description
2. DECISIONS     — every settled decision, stated as facts, append-only
3. RULED OUT     — everything explicitly rejected and why, append-only
4. OPEN          — unresolved questions, one per line
5. STATE         — current snapshot of where the project stands right now

Rules:
- Sections must appear in this order
- No section may be omitted
- DECISIONS and RULED OUT are append-only — nothing is deleted
- STATE is rewritten fresh at each checkpoint
- No prose padding — dense, factual entries only
- For project origin see THREAD.md

---

## 3. Instructions File (v[NN]--instructions.md)

Sections (in order, all mandatory):
1. PROJECT              — name, one line
2. GOAL                 — one sentence, what the project produces
3. BACKGROUND           — 2-4 sentences, full intellectual state
4. ARTIFACT STATE       — what exists, structure, length, completeness
5. KEY DECISIONS        — bulleted, append-only, stated as facts
6. OPEN QUESTIONS       — bulleted, rewritten fresh each checkpoint
7. EXPLICITLY RULED OUT — bulleted, append-only, with reason
8. NEXT TASK            — exactly what the next AI does first
9. PERSONA              — paste or describe
10. STYLE AND CONSTRAINTS — tone, voice, formatting rules

Rules:
- Sections must appear in this order
- No section may be omitted
- KEY DECISIONS and EXPLICITLY RULED OUT are append-only
- OPEN QUESTIONS and NEXT TASK are rewritten fresh each checkpoint
- NEXT TASK is one specific action, not a list

---

## 4. Artifact File (v[NN]--artifact.[ext])

### Wrapper schema (all artifact types)

Required elements:
1. LABEL         — first line must be: ARTIFACT v[NN]
2. VERSION       — version number must match context and instructions files
3. EXTENSION     — file extension must match content type:
                   .md  for Markdown and prompts
                   .tex for LaTeX
                   .py  for Python
                   .txt for plain text
4. BODY          — file must contain non-empty content below the label

Rules:
- Wrapper checked before any type schema
- Extension mismatch is a hard error
- Version mismatch between triplet files is a hard error

### Type schemas

Defined at time of first use. No type schema exists speculatively.
Current defined types: none formally written yet.
MASTER-PROMPT.md (.md prompt type) — to be formalised in next session.

---

## 5. THREAD.md

Sections (in order, all mandatory):
1. TITLE         — # Thread: [project name]
2. STARTED       — start date, status (active | paused | complete | archived)
3. DESCRIPTION   — what the project is and what it produces, 2-4 sentences
4. PERSONA       — See persona.md or inline if no persona file
5. CHECKPOINT LOG — append-only, one entry per version, ascending order

Checkpoint log entry (mandatory fields):
### v[NN] — YYYY-MM-DD
**Triggered by:**
**Artifact:**
**Context:**
**Instructions:**
**Key decisions made this session:**
**Still open:**

Rules:
- Sections must appear in this order
- No section may be omitted
- CHECKPOINT LOG is append-only
- Entries in ascending order — oldest first, newest at bottom
- Latest version derived from last log entry
- Status must be one of: active | paused | complete | archived
- Dates in YYYY-MM-DD format

---

## 6. MAP.md

Sections (in order):
1. TITLE    — # Map: AI-Library (mandatory)
2. ROOT     — ## Root, one entry per root-level file (mandatory)
3. PROJECTS — one ## section per project folder, one sub-section per subfolder

Entry format:
- [filename](path/filename) — one-line summary

Rules:
- ROOT section mandatory even if empty
- Each project gets its own ## section: ## projects/[slug]/
- Subfolders get their own ## section: ## projects/[slug]/docs/
- Empty folders listed as section headers with no entries
- One-line summary mandatory on every entry
- All paths relative to AI-Library root
- System files (.DS_Store etc.) never listed
- No file appears twice
- MAP.md is the single index — no file listed anywhere else

---

## 7. persona.md

Sections (in order, all mandatory):
1. ROLE        — one sentence, who this AI is in this project
2. DOMAIN      — areas of expertise, 2-4 sentences
3. BEHAVIOUR   — communication style, hard limits, and goals combined
4. EXAMPLES    — 1-2 samples of correct response style

Rules:
- Sections must appear in this order
- No section may be omitted
- BEHAVIOUR mixes positive directives and prohibitions as needed
- EXAMPLES must be representative of the actual project voice
- No frontmatter — persona.md is a project file
- No prose padding — every line is operative
