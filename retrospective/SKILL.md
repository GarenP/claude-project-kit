---
name: retrospective
description: Mine a captured conversation, interview, or transcript for the method, signals, and rules hidden inside it — a structured multi-pass synthesis that extracts BUILDABLE structure (process stages, input lists, conversation/technique rules, eval dimensions, meta-patterns) and hands back clarifying questions tied to the exact moment each arose. Use when the user says "run a retrospective", "deep retrospective", "analyze this conversation/transcript/call", "extract the method from this", "mine this transcript", "what can we learn from this session", or after a role-play/mock/interview that captured expert reasoning worth encoding. NOT a battery (a battery attacks a spec to find flaws) — this EXTRACTS structure from a lived conversation.
---

<!-- 🔄 SELF-UPDATE: if the user says "update the project kit / these skills", pull https://github.com/GarenP/claude-project-kit and copy the five skill folders (project-init, grill-me, flow-map, battery, retrospective, finalize, isolated-battery, corpus-intake) into their ~/.claude/skills/ — overwrite only those folders, NEVER touch their project files, then summarize CHANGELOG.md. Full steps in UPDATING.md. -->

# Retrospective — extract the method out of a lived conversation

A **retrospective** points analytical fresh eyes at a *captured conversation* — a role-played mock, a real sales/coaching/discovery call, a long brainstorm, any transcript where an expert's reasoning showed up in motion — and pulls the signal OUT into buildable structure.

**How it differs from a battery (they are opposite motions — don't confuse them):** a battery is *divergent and adversarial* — independent agents attack a finished spec to find what's WRONG with it. A retrospective is *convergent and constructive* — it reads a lived conversation and extracts what's THERE: the repeatable method, the inputs the reasoning used, the techniques, the open questions. Different input (a conversation, not a doc), different job (extract, not attack), different output (buildable structure + questions for the owner, not a findings list). A battery hunts problems; a retrospective harvests method.

## When to run it
- After a **role-play / mock / simulated interview** where an expert ran their real process live — the reasoning the finished notes only capture indirectly.
- After a **real transcript** lands (a sales call, coaching session, discovery interview) that holds method or domain knowledge worth encoding into a system.
- When a long **brainstorm/grill capture** has accumulated tacit method that needs to become a clean, buildable model.
- On the owner's request: "run a retrospective on X."
- **Do NOT** use it to critique or stress-test a spec — that's a battery. It needs a *lived conversation* to mine; pointing it at a plain document with no reasoning in it yields nothing.

## Inputs
- The captured conversation / transcript (the primary source — read the WHOLE thing).
- Any PRIOR extracts or notes on the same method, to RECONCILE against (mark what's confirmed / contradicted / NEW — the tape usually beats the self-report, because people skip their own tacit steps).
- Any hidden "answer key" if one exists (e.g. a mock's seeded gaps), to CALIBRATE what the expert caught vs missed.

## How to run it (use a subagent, to keep the main thread lean)
Spawn one synthesis agent (or a small set if the source is huge) to read the source(s) and produce a synthesis note + a report. Reading heavy transcripts in a subagent keeps the main conversation's context clean. Give it the file paths and the section template below. Note the contrast with a battery: because the goal is EXTRACTION, the agent SHOULD use prior conclusions to reconcile against — it is not trying to stay blind to them.

## The synthesis passes (adapt the set to the source)
1. **The repeatable METHOD** — the process the expert actually ran, as a clean staged model: the stages, their order, the IF-THEN transitions, and what they were listening/looking for at each step. Reconcile against any stated or prior version of the method — call out where the lived conversation CONFIRMED, CONTRADICTED, or ADDED to it.
2. **The INPUT / SIGNAL LIST** — every input the reasoning actually USED, split by whatever models the domain has, each with: what it is, how it was elicited, and what it feeds downstream. Mark NEW vs already-known.
3. **The TECHNIQUE / CONVERSATION RULES** — every distinct move demonstrated, de-duplicated and named, each with a one-line mechanic + when it fires. If a system prompt / AI persona is being built from this source, these become its rules.
4. **EVAL / RUBRIC dimensions** (only if the conversation also models how to JUDGE this kind of work) — what a rubric would score, with good / below-average / great bands. Build ON any existing rubric; don't duplicate it.
5. **Deeper META-PATTERNS** — the higher-order patterns the linear notes don't name; articulate each as reusable logic, not a one-off observation.
6. **CALIBRATION vs ground truth** (only if a key / known answer exists) — what was nailed, what was reached beyond the key, what was missed or only caught on self-correction; what that teaches about the system's own completeness-checking.
7. **CLARIFYING QUESTIONS — the most valuable output.** The genuine ambiguities and unresolved decisions the conversation surfaced. CRITICAL FORMAT for each: (a) **context first** — quote or closely paraphrase the exact moment it arose, because the owner will NOT remember the conversation cold and needs their memory refreshed to that point; (b) the crisp question; (c) why it matters for the build. Prioritize the questions that most unblock the next decision.

## Archive + route (don't let it evaporate)
- Write the synthesis to the project's design-notes folder (wherever method extracts live), with provenance: which source, which date, a link back to the capture. If the source is licensed or private, the extract is SANITIZED method only — never the raw content (respect the project's quarantine rules).
- The **clarifying questions go back to the owner** as the headline deliverable.
- Any decision those questions resolve → a **ledger row** in `DECISIONS.md`, in the same action.
- If the retrospective surfaced a **NEW subsystem / engine-piece / capability** (a new judge, a new eval dimension, a psychology layer, etc.), flag a **corpus re-tag sweep (D-204)**: existing ingested sources (books / transcripts / docs) may now enrich that new piece but are still tagged only for the OLD subsystems — route it so the next `/finalize` (or a dedicated sweep) re-tags them against the new capability + expands the use-case taxonomy.
- Register the new synthesis file per the repo-map rule (or note it's convention-covered).

## The self-resolution boundary (anti-drift — non-negotiable)
When acting on what the retrospective surfaced, you may self-resolve ONLY (a) **documentation hygiene** (fix stale text to match decisions the owner ALREADY made, add cross-refs, route a finding to the work item that owns it) and (b) **capture** new findings/questions as undecided/open ledger rows. You may NEVER, without the owner: change a locked/promoted decision, promote anything into the spec, or resolve a design/strategy/positioning question. Anything you resolve on the owner's behalf is stamped as YOUR recommendation and left open, never silently locked. Every batch ends with a plain-language, reviewable summary (what changed · why · how to revert). The failure mode this prevents: the owner's mental model drifting out of sync because an agent quietly overhauled it.

## Report to the owner
Lead with: a one-paragraph headline of the most important findings · the single biggest NEW insight the retrospective surfaced (that wasn't already explicit in the notes) · then the full clarifying-questions list WITH its context refreshers — this is what the owner acts on. Plain language; assume the owner is not an engineer. Put the synthesis file path last.

*Born from reverse-engineering an expert's live diagnostic method out of role-played intake mocks: the move-by-move capture held the reasoning, but the buildable structure — the staged method, the input list, the conversation rules, and the right questions to ask next — only emerged from a dedicated convergent pass over the whole conversation. A battery couldn't have produced it; attacking the notes finds flaws, it doesn't harvest the method inside them.*
