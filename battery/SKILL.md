---
name: battery
description: Run a stress-test battery on a project's spec/design — independent fresh-eyes agents attack it through multiple lenses, findings get adversarially grounded, full transcripts archived with parent/child links, and an experiment registry tracks which lenses have run. Use when the user says "run a battery", "stress test the spec/design", "mini battery", "audit the design with agents", or at milestone/pre-build/pre-ship gates.
---

<!-- 🔄 SELF-UPDATE: if the user says "update the project kit / these skills", pull https://github.com/GarenP/claude-project-kit and copy the four skill folders (project-init, Grill Me, flow-map, battery) into their ~/.claude/skills/ — overwrite only those folders, NEVER touch their project files, then summarize CHANGELOG.md. Full steps in UPDATING.md. -->

# Battery — multi-agent stress-testing with a paper trail

A **battery** is a set of independent fresh-eyes agents attacking a project's spec/design through lenses the editors haven't used. Editors can't see their own drift — the value comes from agents that read the docs **cold**, with no access to your conclusions. Two sizes:

- **Full battery** (milestones, pre-build gate, pre-ship gate): 4–6 agents, each a different lens, plus a synthesis.
- **Mini battery** (validating one specific scenario or fix): ~3 agents on that single question — cheap, fast, no new lenses required.

## The self-improving loop (batteries get better every run — propose-and-confirm)

Batteries are not static — they learn. The fuel is the **scoreboard**: in the experiment registry, every run records a performance row per lens — **raw found · confirmed-real (survived adversarial verification — the number that matters) · false-alarm rate · top severity · one-line verdict.** A lens that finds nothing on a clean spec is NOT bad (clean bill of health); "good" = *when real problems exist, it catches them with low noise*, judged over many runs.

That data drives four moves, **all governed by the COMMANDER'S INTENT** (the project's / kit's stated end-state) — every proposed change is judged "does this serve the intent?"; if not, drop it:
1. **SELECT (exploit):** weight lens choice by track record — run the proven high-yield lenses.
2. **EVOLVE (mutate):** sharpen a high-yield lens into a variant (e.g. split "security" into injection/exfil/supply-chain); variants compete on yield, keep the winner. May include a **token-bounded, cached deep-research step** to enrich a lens with current failure modes/attack patterns — capped so it never burns budget.
3. **GENERATE:** when findings cluster on a theme across runs, spin up a specialized lens for it.
4. **★ EXPLORE (non-negotiable):** ALWAYS reserve a slot for a brand-new lens never tried. Without it the system overfits to yesterday's problems and goes blind to new failure modes — the one thing a battery exists to catch. Exploit the best, but always explore.

**Propose-and-confirm, never self-rewriting:** the AI proposes the selection/variant/new-lens and its rationale; the human approves; then it's recorded. (Cross-project communal "master index" of batteries = deliberately HELD — privacy + malicious-contribution security; its own design pass.)

## The lessons log (the reactive half — learn from problems that got through)

Batteries hunt for problems proactively; the **lessons log** learns from problems that surface in REAL USE (a user drifts, a generated artifact is wrong, an update could break work). Keep `LESSONS.md` (or a section): each entry = what missed · the real context · the fix. On confirm, the fix is written into the relevant skill/spec + a "born from real X" changelog note. **The intelligence is in the clusters:** when several lessons share a root cause, abstract a PRINCIPLE that kills the whole FAMILY — don't just patch instances. Every lesson and fix is judged against the commander's intent. (One project's miss → fix the SHARED method → every future project inherits it.)

## Step 1 — Consult the experiment registry

Open (or create) `audit/experiment-registry.md` — a table of every test type ever run: lens · what it checks · last run date · report file. Rules:
- **Novelty rule:** every full battery includes **at least one lens never tried before** on this project. Invent freely — the proven lenses below are a menu, not a ceiling.
- **No pointless re-invention:** don't re-run a lens that just ran on an unchanged area; DO re-run the most useful lenses at the **pre-build polish pass** (the registry's value: you know which ones earned their keep).

**Proven lens menu:** doc consistency / cross-doc agreement · **persona simulation** (agents live as target users inside the spec for simulated weeks — finds sequencing/rendering gaps) · adversarial security/abuse/legal · seller-side business operations (support, updates, refunds, scaling) · resource/capacity arithmetic (tokens, cost, rate limits — checked with real math) · instruction-coherence/promptability (are the AI-behavior rules actually followable? do any collide?) · failure-state walking (what does day 0 look like with nothing connected?).

## Step 2 — Run the agents

- Each agent reads the project docs **cold** — give it file paths and its lens, never your hypotheses or prior findings.
- Agents run in parallel, independent of one another.
- Require structured output: findings with severity, the evidence (file + section), and a proposed fix.
- For big/surprising claims, add a cheap adversarial check (a second agent told to refute the claim) before they reach the synthesis.
- **Routing-lane rule:** before logging a buyer/user-side risk as a product fix, ask whether marketing qualification/disqualification is the cheaper correct lane ("good friction" — keeping the wrong users out beats engineering around them).

## Step 3 — Archive EVERYTHING (the part everyone skips)

Synthesis without transcripts is untraceable. In the project's `audit/` folder:
1. **Full transcripts:** each agent's complete report → `audit/transcripts/YYYY-MM-DD-<battery-name>/<lens>.md`. Never let the raw reports die with the session.
2. **Synthesis file:** `audit/YYYY-MM-DD-<battery-name>.md` — scorecard (one verdict line per lens), converged findings, and a judgment queue of decisions the owner must make.
3. **Parent/child linking, both directions:** the synthesis cites the transcript file for every conclusion ("→ transcripts/.../persona.md §W6"); each transcript header links back to the synthesis. Any conclusion must be traceable to its source so logic and errors can be audited later.
4. **Update the registry** (lens rows + dates) in the same action.
5. **Route findings:** every judgment-queue item becomes a row in the project's decision ledger (`DECISIONS.md`) in the same action — a finding without a ledger row is a finding that will be forgotten.

## The self-resolution boundary (anti-drift — non-negotiable)
When acting on findings, you may self-resolve ONLY (a) **documentation hygiene** (fix stale text to match decisions the owner ALREADY made, add cross-refs, fill a flagged missing default, route a finding to the work item that owns it) and (b) **capture** new findings as undecided/open ledger rows. You may NEVER, without the owner: change a locked/promoted decision, promote anything into the spec, or resolve a design/strategy/positioning question. Anything you resolve on the owner's behalf is stamped as YOUR recommendation and left open, never silently locked. Every batch of self-resolutions ends with a plain-language, reviewable summary (what changed · why · how to revert). The failure mode this prevents: the owner's mental model drifting out of sync with the system because an agent quietly overhauled it.

## Step 4 — Report to the owner

Lead with the verdict scorecard and what's genuinely strong (agreement across lenses matters in both directions). Then the judgment queue: each item = the problem in plain words + the proposed solution + what it costs to ignore. Plain language — assume the owner is not an engineer.

## Mini battery (single-scenario validation)

When one specific fix/scenario needs validation: ~3 parallel agents, same scenario, different angles (e.g. does-it-work / how-does-it-fail / what-does-the-user-feel). Same archiving rules, lighter synthesis (one file, no new registry lenses required). Skip the mini battery entirely when the open question is a *taste/judgment call* — agents can't make taste decisions for the owner; that's a conversation.
