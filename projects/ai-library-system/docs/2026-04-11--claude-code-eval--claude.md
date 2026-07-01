---
title: Claude Code Five-Layer Evaluation Prompt
date: 2026-04-11
updated: 2026-04-11
type: document
vendor: claude
model: claude-sonnet-4-6
tags: [evaluation, layer-1, layer-2, layer-3, layer-4, layer-5]
related: [ARCHITECTURE.tex, MASTER-PROMPT.md]
---
You are evaluating an AI document library system. The library is stored at:
~/AI-Library (iCloud)

Read the following files in this order before doing anything else:
1. MASTER-PROMPT.md
2. projects/ai-library-system/THREAD.md
3. projects/ai-library-system/v07--context.md
4. projects/ai-library-system/v07--instructions.md
5. ARCHITECTURE.tex
6. projects/ai-library-system/docs/2026-04-11--layer-1-foundation--claude.md
7. projects/ai-library-system/docs/2026-04-11--layer-2-session--claude.md
8. code/pre-commit.py

Then explore the full folder structure using tree or ls -R.

Evaluate the system across all five layers:

LAYER 1 — Foundation
- Is the folder structure consistent with the documented schema?
- Are naming conventions followed across all files?
- Is frontmatter present and valid on all standalone files?
- Is THREAD.md well-formed and ascending?
- Is MAP.md accurate and complete?
- Does the pre-commit hook match the documented validation rules?

LAYER 2 — Session
- Is the Layer 2 design sound and complete as documented?
- Any gaps between the design document and what Layer 1 provides?

LAYER 3 — Automation
- What is the highest-value script to build first given current pain points?
- What are the risks in the checkpoint.py design as described in ARCHITECTURE.tex?
- What input/output design would be most robust for this user's workflow?

LAYER 4 — Retrieval
- Is the library structure compatible with efficient embedding and retrieval?
- What design decisions at Layer 1 will most affect Layer 4 quality?

LAYER 5 — Orchestration
- No implementation yet — evaluate whether the Layer 1 foundation is solid
  enough to support the Layer 5 design described in ARCHITECTURE.tex.

For each layer: state what is working, what is incomplete, what is at risk,
and one concrete recommendation.

Do not suggest proprietary platforms or hosted services. The system is
deliberately vendor-agnostic and plain-text first.
