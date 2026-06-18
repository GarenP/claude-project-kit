---
name: finalize
description: Run the end-of-session FINALIZE wrap — the deliberate, resumable procedure that closes out a brainstorm/work session: verification checkers → retrospective → battery (+ optional isolated-battery) → a human-in-the-loop gate for any conflicts → then promote settled decisions into ALL canonical docs (the whole docs/ folder) + the PRD + the system-flow-map, and commit/push. Use when the user says "finalize", "wrap up the session", "push the updates", "promote everything", "close out", or at a session-end / promotion-sweep gate. Heavy + token-intensive by design, so it CHECKPOINTS and COMMITS after every phase and is fully resumable after a crash, shutdown, or rate-limit. Replaces the old session-end procedure that lived inline in CLAUDE.md.
---

<!-- 🔄 SELF-UPDATE: if the user says "update the project kit / these skills", pull https://github.com/GarenP/claude-project-kit and copy the skill folders (project-init, grill-me, flow-map, battery, retrospective, finalize, isolated-battery, corpus-intake) into their ~/.claude/skills/ — overwrite only those folders, NEVER touch their project files, then summarize CHANGELOG.md. Full steps in UPDATING.md. -->

# Finalize — the resumable session-end wrap + promotion sweep

This is the one deliberate procedure that takes a session's loose, captured work and makes it durable and congruent: it verifies, stress-tests, gets human sign-off on anything contentious, then promotes settled decisions UP into the canonical docs + PRD + flow-map and pushes. It is intentionally heavy — so it is built to **never lose work midway**.

## ⚠ Token / crash / shutdown safety — read first
`finalize` burns a lot of context (a retrospective + a battery are each multi-agent). Two honest constraints shape the design:
1. **The AI cannot reliably read the user's remaining context-window/token budget** — there is no tool for it. So we do NOT try to "predict how much fits." Instead we make every phase independently durable.
2. **A crash, shutdown, or rate-limit can hit mid-run.** So after EACH phase we (a) write a checkpoint to `brainstorms/.finalize-progress.md` and (b) **git-commit the phase's output**. Completed phases are then on disk AND in git history — a re-run resumes from the first unfinished phase and redoes at most one phase, never the whole thing.

**Resume protocol (do this at the very start of every `finalize` run):**
- Read `brainstorms/.finalize-progress.md` if it exists. It lists each phase as `[ ]` (todo), `[~]` (in progress), or `[x]` (done) with a timestamp/commit.
- **Skip every `[x]` phase.** Resume at the first non-done phase. If the file is absent or all phases are done, start fresh (and create/clear the file).
- This file is gitignored working-state (like `last-response.md`); add `brainstorms/.finalize-progress.md` to `.gitignore` if not already there.

Announce to the user at the start: *"Finalize is heavy. I'll checkpoint + commit after each phase, so if anything interrupts us, re-running `/finalize` picks up where it stopped."*

## The phases (each ends with: update the progress file → commit)

### Phase 0 — Pre-flight
- Establish/resume the progress file with the phase checklist below.
- Confirm the session has a capture file (`brainstorms/{date}-{topic}.md`) and pending ledger rows worth promoting; if there's nothing to finalize, say so and stop.

### Phase 1 — Verification battery (cheap, fast)
- Run every checker the project has: `check_promotions.py`, `check_orphans.py`, `check_open_questions.py`, `check_doc_sync.py`, `check_repo_map.py`, `check_grill_complete.py <capture>` (and any project-specific ones).
- Record PASS/FAIL per checker into the progress file. **Hard failures (open questions, doc drift, repo-map mismatch) are CONFLICTS** → they feed the Phase 4 human gate; do not silently push past them.
- Commit: `finalize: phase 1 — checkers`.

### Phase 2 — Retrospective
- If the session captured a *lived conversation worth mining* (a grill, a mock, a rich brainstorm), run the `retrospective` skill on the capture → write its output under `audit/`.
- (If the session was pure mechanical work with no method to extract, note "retrospective n/a" and skip.)
- **Mistake post-mortem:** surface any MEANINGFUL mistakes made this session (ones that affected a decision/output/understanding — not trivial mechanics) → for each, name the root cause + propose a SYSTEMIC prevention (a rule/checker/guardrail/kit change). These feed the Phase 4 human gate, which decides which become permanent. (Mistake → root-cause → never-repeat; D-119.)
- Commit: `finalize: phase 2 — retrospective`.

### Phase 3 — Battery (+ optional isolated-battery)
- Run the `battery` skill to stress-test the session's design changes / spec / new decisions; archive transcripts under `audit/`.
- **Optionally** (AI's judgment, or on request) run `isolated-battery` for a zero-risk isolated drift/consistency probe of the doc↔ledger system.
- Collect findings; **any confirmed issue is a CONFLICT** for the Phase 4 gate.
- Commit: `finalize: phase 3 — battery`.

### Phase 4 — 🧑 Human-in-the-loop gate (STOP before promoting)
- **Do not push to the PRD/docs yet.** Gather everything from Phases 1–3 that needs a human decision: checker failures, battery findings, contradictions between a new decision and a PROMOTED one, ambiguous numbers, anything the self-resolution boundary forbids resolving alone.
- Present them to the user as a short, plain-language decision list and **WAIT for their calls.** If there are zero conflicts, say so and proceed.
- ★ **Never present bare ledger codes (D-0XX).** The user does NOT track codes by number and is out-of-context on a long index — a list of "promote D-208, D-210, D-195" is meaningless to them. Each promotion candidate / conflict = **its ESSENCE in one plain sentence** (what the decision actually says), grouped by theme, code in a trailing parenthesis at most. (Recurring real-user complaint — the index line items alone carry no context.) Same rule applies to the Phase-5 recap.
- Record the user's resolutions into the ledger (new/adjusted rows) before promoting.
- Commit: `finalize: phase 4 — conflicts resolved` (only after the human responds).

### Phase 5 — Promote + push (update EVERYTHING, then ship)
- Walk every PENDING/DISCUSS row the session settled and **promote it into its target(s)**, updating **ALL** of these as needed so they stay congruent:
  - **The whole `docs/` folder** — `icp.md`, `offer.md`, `mechanism-and-value.md`, **`facts-registry.md`** (any changed numbers), and **`validation-summary.md`** (re-distill so the human check-page is current). Update each doc's provenance header (`Built from` + `Last reconciled` date) and stamp the ledger row `→ PROMOTED → docs/X.md (date)`.
  - **The PRD** — promote spec-level decisions into the right section; bump the version + changelog note.
  - **The system-flow-map** (`schema/system-flow-map.*`) — regenerate via `/flow-map` if the change touched the architecture.
  - **Corpus re-tag sweep (D-204)** — if this session ADDED a new subsystem / engine-piece (a new judge, a psychology layer, a knowledge graph, a new card mechanic, etc.), sweep the corpus registries (`_NEVER-SHIP/**/_CORPUS-REGISTRY.md`) and **re-tag existing sources** (books / transcripts / docs that could now enrich the new piece) + expand the use-case tag taxonomy to include it. Stops the "source tagged only for the OLD subsystems" drift as the system grows — sources don't auto-surface for capabilities that didn't exist when they were ingested.
- Re-run `check_doc_sync.py` + `check_promotions.py` — they must pass (no doc citing a superseded decision, no number drift). Fix anything they flag.
- Final commit: `finalize: phase 5 — promoted + pushed`, then **`git push`** (and push the gitignored vault repo too if `_NEVER-SHIP/raw/` changed).
- Clear/mark the progress file fully `[x]` done.

## After finalize
Give the user a short recap: what got promoted + where, what's still open, what the human resolved, and the next suggested step. The session's decisions are now durable and congruent across the ledger, the docs, the PRD, and the map.

### Phase 6 — The reductive refocus (the closing question)
After the recap, pose the single most important question: **"What is the ONE thing most blocking us right now?"** — the biggest roadblock to the project's progress. Answer it honestly as an advisor (name the real constraint, not a comfortable one), then propose the smallest next move that de-risks it. This is the same reductive loop the product runs on the user's business, turned on the project itself — it pulls a creative, idea-rich owner back to the single highest-leverage point instead of widening scope. End on THAT, not on a stop-offer.

## Boundaries (inherited)
- The **self-resolution boundary** still holds: never resolve a design/strategy/positioning question or change a PROMOTED decision on the user's behalf — those are exactly what Phase 4 surfaces for them.
- Promotion only happens AFTER the human gate. A clean checker run is NOT permission to promote unresolved conflicts.
