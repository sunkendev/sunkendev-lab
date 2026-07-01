---
title: Layer 2 Session Reference
date: 2026-04-11
updated: 2026-04-11
type: document
vendor: claude
model: claude-sonnet-4-6
tags: [layer-2, session, reference]
related: [MASTER-PROMPT.md, ARCHITECTURE.tex, 2026-04-11--layer-1-foundation--claude.md]
---

# Layer 2 — Session Reference

Layer 2 reduces the manual work of starting each AI session by pre-loading
standing context into a platform workspace. It does not replace Layer 1 as
the permanent record. It adds convenience on top of an unchanged foundation.

---

## What Layer 2 Provides

Without Layer 2, every session begins by pasting MASTER-PROMPT.md into a
fresh chat. With Layer 2, the full MASTER-PROMPT.md content and the project
persona are pre-loaded in the platform workspace system prompt. They are
present from the first token of every session without any user action.

The four-file RESUME procedure is still required every session for
version-specific content — the current artifact, context, and instructions
change at every checkpoint and cannot be pre-loaded. Layer 2 eliminates
the static setup cost, not the dynamic context cost.

Layer 2 provides:

- MASTER-PROMPT.md content active in every session without pasting
- Persona loaded automatically for every session in the workspace
- Project-specific constraints visible to every new chat
- Platform-managed session memory for lightweight preferences and patterns
- A faster session start: open workspace, paste four RESUME files, begin work

The permanent record — versioned triplet files, THREAD.md, MAP.md, git
history — is unchanged. Platform workspaces are convenience only.

---

## What Goes in the Workspace System Prompt

The workspace system prompt contains exactly two things:

**1. The full contents of MASTER-PROMPT.md**

Paste the complete current MASTER-PROMPT.md verbatim. This gives the AI
the full Layer 1 operating instructions — folder structure, naming rules,
frontmatter schema, checkpoint ritual, all schemas, all navigation commands,
and all behaviour rules — without the user pasting anything.

When MASTER-PROMPT.md is updated (at a new checkpoint version), update
the workspace system prompt to match. The system prompt must always reflect
the current operative version of MASTER-PROMPT.md.

**2. The contents of persona.md for this project**

Paste the complete persona.md below the MASTER-PROMPT.md content. The AI
will operate with this persona from the first message of every session.

Nothing else belongs in the system prompt. Version-specific content —
current artifact state, current instructions, open questions — changes
at every checkpoint and is pasted per session via RESUME.

Putting MASTER-PROMPT.md in the system prompt is not only convenient —
it is structurally advantageous. The system prompt sits at the beginning
of every context window and carries inherent priority over pasted content.
Instructions placed there are followed more reliably and consistently than
the same instructions pasted into the user turn. This is the correct
position for standing operating instructions that must never be overridden.

---

## Session Start with Layer 2

```
1. Open the workspace for the relevant project
2. Type: RESUME
3. Paste persona.md
4. Paste THREAD.md
5. Paste v[NN]--context.md (latest version)
6. Paste v[NN]--instructions.md (latest version)
7. The session is live
```

The AI already has MASTER-PROMPT.md and persona.md from the system prompt.
Steps 3 and 4 — persona.md and THREAD.md — are still pasted because the
RESUME procedure requires all four files and the system prompt content
is not guaranteed to be visible to the AI as pasted context. Pasting
them explicitly ensures the AI treats them as active working context
rather than background instructions.

The checkpoint ritual, navigation commands, and behaviour rules operate
exactly as in Layer 1. Nothing changes about how the AI works. Only the
startup sequence is shorter.

---

## Platform Memory

Platform memory builds a profile of user preferences and patterns across
sessions. It is supplementary to Layer 1 and captures style preferences,
communication patterns, and incidental context.

Platform memory does not capture project-specific state, version history,
or structured decisions. It is not a substitute for the Layer 1 checkpoint
ritual. The instructions file is the only reliable cross-vendor context
carrier.

Platform memory is platform-locked. It does not transfer between vendors,
cannot be pasted into a session on a different platform, and may be reset
due to account changes, plan changes, or platform policy updates. Never
treat it as permanent.

---

## Multi-Vendor Use at Layer 2

If you work across multiple AI vendors, maintain one workspace per project
on your primary platform as the Layer 2 environment. When switching to a
different vendor for a session, fall back to Layer 1: paste MASTER-PROMPT.md
manually, then follow the four-file RESUME procedure.

The instructions file is vendor-agnostic. The platform workspace is
vendor-specific. The permanent record is unaffected by which vendor
you use for any given session.

---

## One Workspace Per Project

Each active project has its own workspace. The workspace system prompt
contains the MASTER-PROMPT.md content and that project's persona.md.
Do not share a workspace across projects — the persona is project-specific
and mixing projects in one workspace degrades AI behaviour.

---

## Relationship Between Layer 1 and Layer 2

| Function                        | Layer 1    | Layer 2    |
|---------------------------------|------------|------------|
| Permanent context storage       | yes        | no         |
| Version history                 | yes        | no         |
| Cross-vendor portability        | yes        | no         |
| Generational durability         | yes        | no         |
| Automatic persona loading       | no         | yes        |
| Reduced session startup effort  | no         | yes        |
| Platform preference memory      | no         | yes        |

Layer 2 adds convenience in the second column. It does not touch the
first column. If the platform changes, the vendor is abandoned, or
the account is lost, Layer 1 is entirely unaffected.

---

## What Layer 2 Does Not Provide

- Automatic file saving — the user still copies and saves checkpoint output
- Automatic MAP.md or THREAD.md updates — manual after each checkpoint
- Search across the library — that is Layer 4
- Semantic retrieval — that is Layer 4
- Any form of scheduling or pipeline automation — that is Layer 5
- A substitute for the checkpoint ritual — checkpoints still required

---

## When to Implement Layer 2

Implement Layer 2 when the manual paste of MASTER-PROMPT.md at session
start has become friction you notice. For a user running one or two
sessions a week across one active project, Layer 1 alone is sufficient.
For a user running daily sessions across multiple projects, Layer 2
eliminates meaningful repetition.

Layer 2 requires a paid platform account. Confirm that platform workspaces
with a configurable system prompt are available on your current plan before
proceeding.
