---
name: ai-library-ops
description: >
  Automates Layer 3 operations for the AI document library. Use this skill whenever
  the user triggers CHECKPOINT, NOTE, COMMIT, RESUME, or NEW PROJECT. Handles:
  saving the checkpoint file, running checkpoint.py (dry-run then --write),
  git add/commit, the MASTER-PROMPT.md auto-deploy via checkpoint.py, add_note_thread.py for notes,
  git_sync.py for push/fast-forward-main, file-based RESUME (no copy-paste), and
  guided new project creation with persona.
  Triggers: CHECKPOINT, NOTE, COMMIT, RESUME, NEW PROJECT, CONTEXT CHECK,
  "start a new project", "resume a project", "load a project", "switch project".
  v6: NEW PROJECT writes all three v00 stubs and registers them in MAP.md.
  v7: portable for cloud / iOS sessions — git-root discovery, best-effort lock delete,
  core.hooksPath + git-identity bootstrap, CLAUDE.md Layer 2.
  v8: CHECKPOINT and COMMIT push the current branch and fast-forward main to match —
  closes the gap where cloud session branches never reached main.
  v9: push/fast-forward-main logic extracted from inlined bash into git_sync.py —
  CHECKPOINT, COMMIT, and NOTE all call the same script; outcome is logged to
  logs/git-sync.log automatically.
  v10: MASTER-PROMPT.md deploy is automatic — checkpoint.py writes the artifact to
  MASTER-PROMPT.md via the project's .deploy marker; the old manual cp (Step 5) is
  removed.
  v11: deploy is verbatim — the artifact is written as-is, keeping its self-describing
  ARTIFACT vNN label (load-bearing; shows the live version), reversing v10's strip.
---

# AI Library Operations

This skill automates the mechanical steps of managing the AI-Library.
It handles five operations: CHECKPOINT, NOTE, COMMIT, RESUME, and NEW PROJECT.

Do not call `checkpoint.py`, `add_note_thread.py`, or `git_sync.py` directly via
Bash outside this skill — direct calls skip the surrounding steps below and leave
commits stranded on the session branch.

The project slug for this library is: `ai-library-system`

---

## Finding the library root

Before running any command, locate the library root and `cd` into it.
Prefer the git toplevel (works in cloud / iOS sessions); fall back to a `find`
from `/sessions` for Cowork, where CWD is outside the repo:

```bash
LIBRARY=$(git rev-parse --show-toplevel 2>/dev/null || find /sessions -name "MAP.md" -maxdepth 7 2>/dev/null | grep -v "\.git" | head -1 | xargs dirname)
cd $LIBRARY
```

All scripts must run from inside the library root — the scripts themselves use
`Path.cwd()` to discover the library, so `cd` is required, not optional.

On the first operation in a fresh clone (cloud / iOS), bootstrap hooks and identity:
```bash
cd $LIBRARY
git config core.hooksPath code/githooks 2>/dev/null || true
chmod +x code/githooks/pre-commit 2>/dev/null || true
git config user.email >/dev/null 2>&1 || git config user.email "ai-library@local"
git config user.name  >/dev/null 2>&1 || git config user.name  "AI Library"
```

---

## Operation 1: CHECKPOINT

Triggered when the user says CHECKPOINT.

The MASTER-PROMPT.md checkpoint ritual governs block production (ARTIFACT, CONTEXT,
INSTRUCTIONS, THREAD ENTRY). Follow it exactly. This skill takes over after the blocks
are assembled — replacing the manual "tell the user to run these commands" instructions
with direct execution.

**Step 1 — Determine version.**
Read the last `### v[NN]` header in THREAD.md. Next version = NN + 1, zero-padded.

**Step 2 — Save the checkpoint file.**
Assemble all four tilde-fenced blocks and write to:
`$LIBRARY/temp/v[NN]-checkpoint.txt`

**Step 2b — MAP scan-and-fix.**
Before the dry-run, scan for any docs/ or inbox/ files not yet in MAP.md:
```bash
cd $LIBRARY && python3 -c "
import os
root = os.getcwd()
with open('MAP.md') as f:
    map_content = f.read()
found = []
for slug in sorted(os.listdir('projects')):
    docs = os.path.join('projects', slug, 'docs')
    if not os.path.isdir(docs):
        continue
    for fname in sorted(os.listdir(docs)):
        rel = 'projects/{}/docs/{}'.format(slug, fname)
        if fname not in map_content and rel not in map_content:
            found.append((slug, rel, fname))
inbox = 'inbox'
if os.path.isdir(inbox):
    for fname in sorted(os.listdir(inbox)):
        rel = 'inbox/{}'.format(fname)
        if fname not in map_content and rel not in map_content:
            found.append(('inbox', rel, fname))
if not found:
    print('MAP.md: all docs registered.')
else:
    for slug, rel, fname in found:
        print('UNREGISTERED: ' + rel)
"
```
For each UNREGISTERED file printed: read its frontmatter `title` field (or use the
filename if no frontmatter). Use the Edit tool to insert a bullet entry under its
project's `## projects/[slug]/` section in MAP.md, immediately before the next `##`
heading. Format:
`- [filename](relative/path) — [title or one-line description]`

Only proceed to Step 3 once MAP.md is clean (scan prints "all docs registered").

**Step 3 — Dry-run.**
```bash
cd $LIBRARY && python3 code/checkpoint.py ai-library-system [NN]
```
Show the full output to the user. It lists files that would be written and a suggested
commit message. Verify the sizes and paths look correct before proceeding.

**Step 4 — Execute.**
```bash
cd $LIBRARY && python3 code/checkpoint.py ai-library-system [NN] --write
```
Show the full output, including any integrity warnings. If integrity warnings appear,
show them clearly and let the user decide whether to proceed with the commit.

**Step 5 — MASTER-PROMPT.md deploy (automatic).**
No manual copy. When this checkpoint's artifact is MASTER-PROMPT.md, checkpoint.py
(Step 4) has already auto-deployed the artifact **verbatim** — the self-describing
`ARTIFACT v[NN]` label included — to MASTER-PROMPT.md via the
`projects/ai-library-system/.deploy` marker, so the deployed file is byte-identical to
the latest artifact and shows the current version. Don't `cp` it by hand; checkpoint.py
does it on every checkpoint. Just confirm `head -1 MASTER-PROMPT.md` shows the current
`ARTIFACT v[NN]`.
Layer 2 then loads automatically via CLAUDE.md (which imports MASTER-PROMPT.md) in
Claude Code / cloud / iOS sessions — no manual paste. Only on platforms with a separate
system-prompt box (e.g. Cowork project instructions) tell the user to paste it manually.

**Step 6 — Git commit and sync.**
Before every git operation:
1. If the `allow_cowork_file_delete` tool is available (Cowork only), call it on
   `$LIBRARY/.git/HEAD.lock`. It does not exist in cloud / iOS sessions — skip it there.
2. Then clear stale locks and commit (works in every environment):
```bash
cd $LIBRARY
rm -f .git/index.lock .git/HEAD.lock 2>/dev/null || true
git add . && git commit -m "[suggested commit message]"
```
3. Push the current branch, then fast-forward `main` to match if checkpointing happened on
   a different branch (cloud / Claude Code on the web sessions commonly run on an
   auto-created session branch, not `main`):
```bash
python3 code/git_sync.py [slug] CHECKPOINT
```
   No formal branching strategy is used for this library — session/feature branches are
   transient and always merged back to `main` before the session ends, keeping a single
   linear history. The script never forces a merge — if it reports `ff-main:diverged`,
   stop and tell the user rather than merging manually without checking first.
Show the commit hash and summary line to the user, and confirm whether `main` was updated
(check the script's printed `Fast-forward main:` status).

---

## Operation 2: NOTE

Triggered when the user wants to append an inter-checkpoint note to THREAD.md.

You need two things: a **topic** (one line) and a **body** (prose). Extract both from
the conversation context rather than asking again if the user has already provided them.

```bash
LIBRARY=$(git rev-parse --show-toplevel 2>/dev/null || find /sessions -name "MAP.md" -maxdepth 7 2>/dev/null | grep -v "\.git" | head -1 | xargs dirname)
cd $LIBRARY
python3 code/add_note_thread.py ai-library-system "[Topic]" --write << 'EOF'
[body text here]
EOF
```

The script appends the NOTE in the correct format and commits THREAD.md immediately.
Confirm the commit message to the user after it runs.

If the body contains newlines or special characters, write it to a temp file first
and redirect stdin:
```bash
python3 code/add_note_thread.py ai-library-system "[Topic]" --write << 'EOF'
[body text here, multiple lines OK]
EOF
```

Push the current branch so the commit isn't stranded only on local disk. NOTE is a
lightweight, anytime operation by design — unlike CHECKPOINT and COMMIT, it does not
merge into `main` here; that fast-forward happens at the next CHECKPOINT, COMMIT, or
session end, not after every individual note:
```bash
python3 code/git_sync.py [slug] NOTE --push-only
```
Confirm the push, in addition to the commit message.

---

## Operation 3: COMMIT

Triggered when the user wants to commit routine session work without a full checkpoint.

1. Run `cd $LIBRARY && git status` to show what has changed.
2. Confirm with the user which files to stage.
3. If `allow_cowork_file_delete` is available (Cowork only), call it on `$LIBRARY/.git/HEAD.lock`.
4. Clear stale locks, stage, and commit (works in every environment):
```bash
cd $LIBRARY
rm -f .git/index.lock .git/HEAD.lock 2>/dev/null || true
git add [file1] [file2] ...
git commit -m "[descriptive message]"
```
5. Push the current branch, then fast-forward `main` to match if not already on it —
   same sync logic as CHECKPOINT Step 6.3:
```bash
python3 code/git_sync.py [slug] COMMIT
```
6. Show the commit hash and summary to the user, and confirm whether `main` was updated.

---

## Operation 4: RESUME

Triggered when the user says RESUME, "resume a project", "load a project", or
"switch project".

This operation loads a project from disk — no copy-paste required.

**Step 1 — Find the library root.**
```bash
LIBRARY=$(git rev-parse --show-toplevel 2>/dev/null || find /sessions -name "MAP.md" -maxdepth 7 2>/dev/null | grep -v "\.git" | head -1 | xargs dirname)
```

**Step 2 — Discover projects.**
```bash
ls -d $LIBRARY/projects/*/
```
Collect the folder names (slugs) as the list of available projects.

**Step 3 — Ask which project.**
Use AskUserQuestion with the slug list as options. Example format:

> "Which project do you want to resume?"
> Options: [each slug as an option, with "Other" for manual entry]

**Step 4 — Find the latest files for the chosen project.**
```bash
SLUG=[chosen-slug]
CONTEXT=$(ls $LIBRARY/projects/$SLUG/v*--context.md 2>/dev/null | sort | tail -1)
INSTRUCTIONS=$(ls $LIBRARY/projects/$SLUG/v*--instructions.md 2>/dev/null | sort | tail -1)
PERSONA=$LIBRARY/projects/$SLUG/persona.md
THREAD=$LIBRARY/projects/$SLUG/THREAD.md
```

**Step 5 — Read all four files.**
Use the Read tool on each path in this order:
1. `$PERSONA`
2. `$THREAD`
3. `$CONTEXT`
4. `$INSTRUCTIONS`

Do not summarise. Read the full content of each file into your working context.

**Step 6 — Confirm orientation.**
Tell the user: "Loaded [slug] at v[NN]. [One sentence on current artifact state from
INSTRUCTIONS ARTIFACT STATE field.] Ready — what do you want to work on?"

Do not ask clarifying questions unless something in the files is genuinely ambiguous.

---

## Operation 5: NEW PROJECT

Triggered when the user says NEW PROJECT, "start a new project", or "create a project".

This operation creates a complete, committed project folder with a generated persona.md
and a blank-but-schema-conformant THREAD.md. It asks three questions one at a time,
each with an example and guidance, before writing anything.

---

### Step 1 — Project name

Ask:

> "What is the name of this project?"
> Options: provide 2-3 placeholder examples as option labels, plus Other.
> Example options: "Fiction Writing", "Legal Research", "Product Strategy"

Derive the slug automatically: lowercase the name, replace spaces with hyphens,
strip punctuation. Example: "Legal Research" → `legal-research`.
Show the derived slug and confirm it with the user before proceeding.

---

### Step 2 — Guided persona questions (one at a time)

Ask each question separately. Do not combine them. Each question uses AskUserQuestion
with example answers as options plus Other — the examples show the register and
depth of answer expected. The user will almost always select Other and type their
own answer; the options exist to model the format, not to be selected literally.

---

**Question 1 of 3 — Role and purpose**

Ask:

> "What is this project, and what do you need the AI to do in it?
>
> Focus on two things: what the project produces, and what job the AI has
> in that work."

Options (as format examples — user types their own via Other):
- "A fiction writing project. The AI acts as a developmental editor: pacing, character consistency, dialogue."
- "A legal research project. The AI summarises case law and identifies precedents, writing for a non-lawyer."
- "A product strategy project. The AI stress-tests assumptions and drafts structured briefs."

---

**Question 2 of 3 — Behaviour and constraints**

Ask:

> "How should the AI behave in this project?
>
> Cover three things: tone, level of directness, and at least one hard
> constraint — something it should always or never do."

Options (as format examples — user types their own via Other):
- "Direct and critical. Flag problems without softening them. Never suggest tools or platforms."
- "Patient and instructional. Break things down step by step. Never assume prior knowledge."
- "Precise and concise. Short answers unless asked to elaborate. Never pad with disclaimers."

---

**Question 3 of 3 — Example exchange**

Ask:

> "Give one example: a question you would typically ask in this project,
> and the kind of answer you would want.
>
> This is the most important question. A concrete example shapes AI behaviour
> more reliably than any description. Show the register and level of directness
> you expect."

Options (as format examples — user types their own via Other):
- "Q: Is this chapter's pacing working? A: No. The flashback in paragraph 3 kills momentum. Cut it or move it to chapter 2."
- "Q: What does consideration mean in contract law? A: It is the exchange of value that makes a promise enforceable. Without it, an agreement is a gift, not a contract."
- "Q: Is this positioning statement strong enough? A: No. It describes features, not outcomes. Rewrite starting from what the customer stops worrying about."

---

### Step 3 — Write and confirm persona.md

Using the three answers, generate a complete persona.md with all four mandatory
sections: ROLE, DOMAIN, BEHAVIOUR, EXAMPLES.

Rules for generation:
- ROLE: one sentence derived from Q1 answer — what the AI is in this project.
- DOMAIN: 2-4 sentences on the expertise implied by Q1 — what the AI needs to know.
- BEHAVIOUR: paragraph derived from Q2 — tone, directness, hard constraints.
  Include specific do/don't statements. Do not pad.
- EXAMPLES: two or three Q&A pairs. The first is the exact example from Q3.
  Generate one or two additional examples consistent with Q1 and Q2 answers,
  matching the same register and directness as the Q3 example.

Show the full generated persona.md to the user and ask:

> "Does this persona look right?"
> Options: "Yes, create the project" / "Revise it" / "Start questions over"

If "Revise it": ask what to change, regenerate, confirm again.
If "Start questions over": return to Step 2.
If "Yes, create the project": proceed to Step 4.

---

### Step 4 — Create the project structure

```bash
LIBRARY=$(git rev-parse --show-toplevel 2>/dev/null || find /sessions -name "MAP.md" -maxdepth 7 2>/dev/null | grep -v "\.git" | head -1 | xargs dirname)
SLUG=[derived-slug]
mkdir -p $LIBRARY/projects/$SLUG/docs
mkdir -p $LIBRARY/projects/$SLUG/code
```

Write `$LIBRARY/projects/$SLUG/persona.md` — the confirmed content from Step 3.

Write `$LIBRARY/projects/$SLUG/THREAD.md` with this exact schema:

```
# Thread: [Project Name]
> Started: [YYYY-MM-DD] | Status: active

## What this project is
[To be filled in after the first working session.]

## Persona
See persona.md

---

## Checkpoint log
(see v01 entry below after first checkpoint)
```

Write `$LIBRARY/projects/$SLUG/v00--context.md` with this exact content,
substituting [Project Name] and [one-line description from Q1]:

```
CONTEXT v00
-----------
PROJECT: [Project Name] — [one-line description from Q1 answer]
DECISIONS:
RULED OUT:
OPEN:
- Project goal not yet defined
- First working session not yet run
STATE:
- New project. Persona confirmed. No sessions completed yet. First checkpoint will be v01.
```

Write `$LIBRARY/projects/$SLUG/v00--instructions.md` with this exact content,
substituting [Project Name] and the persona summary from Q1/Q2:

```
INSTRUCTIONS v00
----------------
PROJECT: [Project Name]
GOAL: [to be defined in first session]
BACKGROUND: New project. Persona confirmed via guided setup. No working sessions yet.
ARTIFACT STATE: None — first session not yet run.
KEY DECISIONS:
OPEN QUESTIONS:
- What is the first artifact or deliverable for this project?
EXPLICITLY RULED OUT:
NEXT TASK: Define the project goal and run the first working session.
PERSONA: See persona.md
STYLE AND CONSTRAINTS: See persona.md
```

Write `$LIBRARY/projects/$SLUG/v00--artifact.md` with this exact content:

```
ARTIFACT v00
------------
[No artifact yet — first working session not run. See v00--instructions.md for next task.]
```

These v00 stubs exist solely so RESUME works and the pre-commit triplet rule is
satisfied on a fresh project. They are superseded after the first real CHECKPOINT
produces v01.

---

### Step 5 — Update MAP.md

Read `$LIBRARY/MAP.md`. Append a new section for the project immediately before the
`## inbox/` line. Use this format, matching the convention used by existing project
sections in the file:

```
## projects/[slug]/

- [persona.md](projects/[slug]/persona.md) — [one sentence on the persona from Q1/Q2 answers]
- [THREAD.md](projects/[slug]/THREAD.md) — Checkpoint log for the [Project Name] project
- [v00--artifact.md](projects/[slug]/v00--artifact.md) — Placeholder artifact; no working sessions yet
- [v00--context.md](projects/[slug]/v00--context.md) — Stub context v00: project created, no sessions run
- [v00--instructions.md](projects/[slug]/v00--instructions.md) — Stub instructions v00: define goal in first session
```

---

### Step 6 — Commit

If `allow_cowork_file_delete` is available (Cowork only), call it on `$LIBRARY/.git/HEAD.lock`, then:

```bash
cd $LIBRARY
rm -f .git/index.lock .git/HEAD.lock 2>/dev/null || true
git add projects/[slug]/ MAP.md
git commit -m "new project: [slug] — persona, THREAD.md, v00 stubs"
```

Show the commit hash. Then tell the user:

"Project [slug] created and committed. THREAD.md is blank — fill in the
'What this project is' section after the first session. First checkpoint
will be v01."

---

## Context Awareness

Every operation (CHECKPOINT, NOTE, COMMIT, RESUME, NEW PROJECT) must begin by
outputting a one-line context status before doing any other work.

**Estimate model:**

Fixed overhead every session:
- System prompt: ~38,500 tokens
- RESUME payload (4 project files): ~18,500 tokens
- Subtotal fixed: ~57,000 tokens

Variable — estimate from session memory:
- Each user exchange (message + response): ~300 tokens
- Each Bash command: ~200 tokens
- Each file read (Read tool): ~1,000 tokens average
- Each web search or fetch: ~1,500 tokens
- Each file write or edit: ~500 tokens

Sum fixed + variable to get the session estimate.

**Thresholds:**

- Below 130K: output `[context ~NNK — within budget]`
- 130K–154K (Tier 1): output `[context ~NNK — Tier 1 warning: checkpoint soon]`
- 155K+ (Tier 2): output `[context ~NNK — Tier 2 URGENT: checkpoint now]`

**Logging:**

When estimate reaches Tier 1 or Tier 2, append an entry to
`$LIBRARY/logs/context-pressure.log` in this format:

```
CONTEXT EVENT [YYYY-MM-DDTHH:MM]
Estimate: ~NNK tokens | Tier [1|2] ([threshold]K threshold exceeded)
Trigger: auto-check at [operation name] start
Session activity: [brief description, e.g. "RESUME + 8 operations + 5 file reads"]
Recommendation: [checkpoint soon | checkpoint immediately]
---
```

Use the Write tool to append — read the file first, then write the full content
including the new entry. Never overwrite previous entries.

**CONTEXT CHECK command:**

If the user says CONTEXT CHECK, run the estimate model explicitly, output the
full breakdown (fixed + variable itemised), and log if threshold is exceeded.
This is a fallback for manual checks — the per-operation status line is the
primary mechanism.

---

## Rules

- Always run from the library root — derive it fresh each session via git toplevel (find /sessions fallback).
- Never skip the dry-run before `checkpoint.py --write`.
- Never skip integrity warning output — show it even when clean ("INTEGRITY all checks passed").
- When the artifact is MASTER-PROMPT.md, Layer 2 updates automatically via CLAUDE.md; manual paste only where no CLAUDE.md mechanism exists.
- Do not edit THREAD.md manually for NOTE entries — always use add_note_thread.py.
- Do not commit MASTER-PROMPT.md separately from the checkpoint triplet — they go together.
- RESUME reads files from disk — never ask the user to paste them.
- NEW PROJECT does not create any files until the persona is confirmed in Step 3.
- Persona options in guided questions are format examples only — do not treat a selected
  option as the user's actual answer without reading the content carefully.
- `git_sync.py` never forces a merge — if it reports `ff-main:diverged`, stop and surface
  it to the user rather than merging manually. Check its printed output for the outcome.
