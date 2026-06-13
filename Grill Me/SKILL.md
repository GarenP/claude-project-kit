---
name: grill-me
description: Interview the user relentlessly about a plan, design, or topic, checkpointing every answer to a brainstorm file so nothing is lost. Use when the user wants to stress-test a plan, get grilled on a design, run a brainstorm or discovery session, extract what's in their head into a doc, or says "grill me".
---

<!-- 🔄 SELF-UPDATE: if the user says "update the project kit / these skills", pull https://github.com/GarenP/claude-project-kit and copy the five skill folders (project-init, Grill Me, flow-map, battery, retrospective) into their ~/.claude/skills/ — overwrite only those folders, NEVER touch their project files, then summarize CHANGELOG.md. Full steps in UPDATING.md. -->

# Grill Me

Relentlessly interview the user about every aspect of the topic until you reach shared understanding. Walk down each branch of the decision tree, resolving dependencies one by one. The real goal is to **extract what's in their head into a durable, organized markdown file** so nothing is lost as context fills up.

## The capture file is the whole point

Long interviews fill up context. If you hold answers only in your head, you will eventually misremember, conflate, or drop something. So you **checkpoint to disk after every single answer**. The file, not your context, is the source of truth. Never make the user ask you to save progress.

## Setup (do this BEFORE the first question)

1. **Create the capture file** at `brainstorms/{YYYY-MM-DD}-{topic-slug}.md` (create the `brainstorms/` folder if it doesn't exist). Every brainstorm capture lives here. One predictable home, regardless of topic. Do NOT scatter captures into project folders. If a session later produces a polished deliverable (a plan, a map, a spec), that artifact can move into the relevant `projects/` folder, but the raw capture always stays in `brainstorms/`.
   - Get today's date with `date +%F` (Bash) if you don't already know it.
2. **Create the file immediately** with a header: title, date, the goal of the session, and an empty "Open flags" section.
3. **Tell the user where you're saving**, in one line. Then ask Q1.

## The paste guard (non-negotiable — lost input is the ONLY unrecoverable failure)

If a user message contains a `[Pasted text #N +N lines]` placeholder and the pasted content is not visible to you, **STOP before checkpointing.** Name the dropped paste number(s) and ask for a repaste NOW — the content may still be in the user's clipboard/buffer; minutes later it's gone forever. Never mark a question captured or resolved while it contains a lost paste. If the user can't recover it, log a permanent `LOST-INPUT` flag in the capture's Open-flags section — a grill may not be stamped COMPLETE with an unresolved or un-annotated lost paste. For anything over ~10 lines, suggest the user drop text into a file (e.g. `brainstorms/inbox/`) instead of the chat box — file reads are lossless.

## The checkpoint rule (non-negotiable)

After EVERY user answer, BEFORE you ask the next question:
- Append a structured entry to the capture file: the question topic, the key facts and decisions from their answer (in their words where the wording matters), and any flags (things they couldn't answer plus who should).
- Update or correct earlier entries if a later answer changes them.
- Only then ask the next question.

Never batch multiple answers into one write. Checkpoint one answer at a time. The point is that if context is lost at any moment, the file already holds everything said so far.

## The decision ledger (runs alongside the Q&A log)

If the project has a `DECISIONS.md` ledger (e.g. `brainstorms/DECISIONS.md` — create one if the project does grills regularly), then **the moment an answer settles a decision**, add it to the ledger as a `PENDING` row in the same action as the checkpoint write:

- **Idea-centric, never session-centric.** SEARCH the ledger for an existing entry on the same idea FIRST. If one exists, append this session as a new ref to that entry — never create a duplicate row. One idea = one entry = all its refs across every session.
- Each row: ID, status (PENDING / PROMOTED / SUPERSEDED / DISCUSS / QUEUED-GRILL), the decision in one line, refs (capture file + section), and the target doc/section it must be promoted into.
- **Conflict check:** if the new decision contradicts a PROMOTED entry, flag it to the user conversationally before recording. If they confirm, mark the old row `SUPERSEDED → D-0xx`; its target column is now the checklist of dead text to remove from the docs.

## The spawn-scan (when a NEW idea arrives — before developing it)

The moment the user floats a new idea, feature, or direction (not a plain answer to your question), fire **2–3 quick system-aware curiosity questions BEFORE you invest in developing it** — a frontline mini-battery that catches integration gaps at the cheapest possible moment: idea-arrival, before any sunk cost. The three default lenses:
1. **How would this work in the current system?** (fit / mechanics)
2. **What could it interfere with?** (ripple/conflict with an existing decision, the project philosophy, or in-flight work)
3. **What might the user not be seeing?** (the blind spot / second-order risk)

These three are defaults — **generate additional situational questions beyond them whenever they better serve the objective** (the goal is finding gaps, not running a fixed checklist). If one message carries **multiple ideas, run the scan on EACH idea**, not just the first.

**Default mode = SILENT / BACKGROUND.** Run this scan in your own reasoning on every substantive message — but do NOT make the user answer fit/interference/blind-spot questions every time; most resolve inside your own reasoning. **Surface a question to the user ONLY when your reasoning judges it genuinely needs their input** — a real gap, conflict with an existing decision/philosophy, or a blind spot worth their attention. The user should address the spawn-scan only when it really matters, never as routine overhead. (When first calibrating with a new user, you may run it visibly for a few turns, then go fully background.)

This is near-free — the grill context is already loaded — and it surfaces issues NOW instead of at a full battery later. It is a distinct trigger from the two scans below: the **spawn-scan fires at idea-ARRIVAL**, the gap-scan fires after an answer is CHECKPOINTED, the consequence-scan fires after a decision LOCKS. Keep it lightweight; skip entirely on a simple confirm or routine answer.

## The gap scan (after every checkpoint, before the next question)

Scan what you just captured — **the user should never be the one to spot these**:

- **Unbound parameters:** any quantity, threshold, cadence, or date left vague ("a certain number of rows", "after a while", "some amount")? Never bury it. Name it, **propose a concrete default** from context, and get it confirmed — or explicitly defer it with an owner and a venue ("tune at build", "Grill 4 decides"). **Never label a decision RESOLVED/locked while it contains an unbound parameter** — write "locked except X (proposed: Y, confirm)".
- **Contradictions:** does the answer conflict with a promoted decision, the project philosophy, or an earlier answer this session? Raise it conversationally NOW, not at wrap-up.
- **Ledger sync:** did this answer settle anything (or spawn a new idea) without a ledger-row update in the same action? Fix immediately — rows update per-decision, not at promotion sweeps.
- **Missing data:** does acting on this answer require information nobody has provided (a file, a number, an owner)? Flag it with who can supply it.
- **Standing-rule scan (human-in-the-loop):** does this input contain something that must shape EVERY future loop — a process correction, a recurring preference, a philosophy-grade principle? Don't trust yourself to "remember" it as a virtue. Name it immediately — "this looks like a standing rule — want it in CLAUDE.md / the skill / memory?" — and on confirm, write it to the durable home in the same action.
- **Existing-home check:** before proposing any NEW store, structure, file, registry, or section — SEARCH for an existing home that already covers it. Don't invent a parallel thing the project already has.
- **Ambiguous referent:** if the user's number/date/threshold references an unnamed thing ("the day-3 unlock", "that panel"), ask the open question ("which unlock do you mean?") — never silently bind it to your best guess or offer only a guessed binary.
- **Consequence scan (on every RESOLVED decision):** the moment an answer locks a decision, enumerate the second-order questions it just spawned — lifecycle rules, edge cases, "what does this imply for X?" — and either grill them immediately as a sub-question (Q2 → Q2b) or queue them explicitly with an owner/venue. The gap-scan items above catch what's wrong in what was SAID; this catches what the new decision makes askable that nobody has said yet. A decision with unexamined consequences is a loose end wearing a RESOLVED stamp.

## Long-session care (ADHD-aware)

- **~90-minute commit nudge:** if the session is in a git repo and ~90 minutes have passed since the last commit (check `git log -1 --format=%cr` when you notice the session running long), offer a checkpoint: one plain-language sentence ("this snapshots everything so far — if anything goes sideways later we can come back to this exact moment"), then a line-item list of what would be committed, graded by importance: 🔴 decisions/ledger rows that exist nowhere else · 🟠 capture-file progress · 🟡 doc edits · 🟢 housekeeping. A "yes" means you commit; then continue the grill.
- **Burnout trigger:** if the user says they're fried, burnt out, fading, or losing focus — don't wait for them to remember the wrap-up. Proactively offer: "Want to wrap it up? I'll reconcile the capture, finalize the ledger, and commit — then you can close the laptop clean." Their fatigue is the signal to protect the work, not to push on.

## Tangents, parallel threads & linking (the parking lot)

People — especially when dumping fast or thinking in parallel (ADHD-style divergent thought) — drop ideas that veer off the current question. Do NOT lose these, and do NOT let them derail the active thread.

- When the user raises a thought that is a **tangent or a parallel/divergent thread** (not an answer to the current question), capture it under a **`## Parking lot (tangents / parallel threads)`** section in the capture file — one bullet per tangent, in their words, with enough context to resume it later. Then gently return to the active question.
- **Link it both ways:** add a line to the project-level **`brainstorms/PARKED-THREADS.md`** index (create it if missing) pointing back to the capture file + section. This makes divergent threads recallable across sessions so they can be promoted into their own grill later.
- You do NOT need to log every user message — only genuine tangents, parallel ideas, or topics that deserve their own future session. Routine answers go in the normal Q&A log.
- **Cross-link everything:** whenever a capture references another doc (a source dump, another brainstorm, an external/ingested file), add a **relative markdown link** to it so context can always be pulled back up. If a tangent is big enough to be its own topic, record it as a **queued grill** in `PARKED-THREADS.md` with a one-line scope.

## Interview method

- Ask **one question at a time**. For each, provide your **recommended answer** (your best inference from context) so the user can simply confirm, correct, or redirect.
- Resolve dependencies in order: settle the upstream decision before the ones that depend on it.
- If a question can be answered by **exploring the codebase or reading a file/doc**, do that instead of asking. If the user hands you a doc (e.g. a Google Doc), read it and only surface what's net-new.
- When the user **can't answer** something, capture it as a flag with the right owner and move on. Don't stall.
- Keep going until the user says you're done, or you've covered every branch. Offer a completeness backstop near the end ("anything we haven't touched?").

## Capture file structure

```
# {Topic}: Brainstorm / Discovery Notes
Date: {date} · Goal: {one line}

## Summary / key decisions
(running synthesis, updated as you go)

## Q&A log
### Q1 — {topic}
- Asked: {question}
- Captured: {facts, decisions, in their words where it matters}
- Flags: {open item -> owner}
...

## Parking lot (tangents / parallel threads)
- {divergent idea, in their words} -> {relative link to follow-up / queued grill}

## Open flags (pending input)
- {item} -> {who can answer}
```

## At the end ("we're done" / "wrap it up" triggers all of this)
1. Do a final read of the capture file for contradictions or gaps and reconcile them.
2. Update `brainstorms/PARKED-THREADS.md` with any new tangents / queued topics, and confirm all cross-links resolve.
3. **Promotion gate:** walk every ledger row this session created or touched. For each PENDING row, either apply the edit to its target doc now (then flip to PROMOTED with the section ref) or — if the user defers, or the edit is large — leave it PENDING and say so explicitly in the recap. PENDING rows are debt; never let them be silent.
4. **CLAUDE.md curation check:** did this session surface anything that must shape EVERY future session — a philosophy principle, a hard constraint, a process rule? If yes, propose a 1–2 line addition to the project CLAUDE.md and add it on the user's confirm. High bar: CLAUDE.md is loaded every session, so detail belongs in the spec/ledger and CLAUDE.md gets only the rule or the pointer.
5. **Retrospective check:** if this session captured a *lived conversation worth mining* — a role-played mock, a pasted real call/interview transcript, or an unusually rich stretch where an expert's reasoning ran in motion — offer to run the **`retrospective`** skill on the capture to extract its method/signals/rules into buildable structure (and surface clarifying questions, each tied to the moment it arose) before the reasoning goes cold. Distinct from a battery: a battery attacks a spec for flaws; a retrospective harvests the method out of the conversation.
6. **Commit** (if the project is a git repo): one snapshot for the whole session — capture file + ledger + any promoted doc edits. Commit message names the session and counts the decisions. "Wrap it up" IS the user's commit command; they never type git themselves.
7. Give the user a short recap: what's captured, what got promoted, what's still PENDING (and where), what's still flagged, and the suggested next step.
