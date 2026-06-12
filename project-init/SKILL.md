---
name: project-init
description: Spin up a new project folder/repo with the full decision-discipline kit — philosophy interview first, then scaffold CLAUDE.md, decision ledger, repo map, brainstorm system, quarantine, checker scripts, and process rules. Use when starting a new project, initializing a repo for a design/build effort, or when the user says "set up a project like Good Money Dashboard" / "project init" / "start a new project workspace".
---

# Project Init — the decision-discipline starter kit

You are setting up a workspace for a long-running design/build project where a human (often a non-coder) and Claude will brainstorm, decide, document, and eventually build. The kit's purpose: **nothing gets lost, nothing drifts, and verification replaces vigilance** — no rule should depend on anyone remembering it.

## Phase 0 — Gauge the user's level FIRST, then match it

**Assume the user knows little or nothing about product development, PRDs, databases, frontend/backend, or how any of this works.** Before the interview, open with a short conversation that gauges their understanding: have they built software before? do they know what a spec or a database is? have they used Claude Code for more than chat? Then **tailor every question and explanation to that level** — plain words, lower grade level, concrete metaphors, never engineer-to-engineer talk. The early conversations are *educational by design*: each question gets a one-or-two-sentence plain-language setup explaining **what the question is for and what the term means** before it's asked. Never fire a bare jargon question ("What's your philosophy?" / "Any quarantine needs?") — translate it first (see the per-question phrasing notes below). A technical user will tell you to speed up; a non-technical user will never tell you they're lost.

## Phase 1 — The alignment interview BEFORE scaffolding (Grill-Me style, one question at a time)

Never scaffold blind. The point of this interview is **drift-proofing**: the high-level executive focus gets extracted FIRST, and every later structure organizes toward that objective. Ask one question at a time, checkpoint every answer, and push past slogans — a real answer must be able to *reject* a future feature idea.

**Layer 1 — Executive focus (the why):**
1. **What is this, in one sentence — and what's its singular purpose?** Force the distinction between mechanism and product (e.g. "data collection is the mechanism; mindset change is the product"). This sentence becomes the drift-check anchor for everything.
2. **Who exactly buys/uses it — and who is disqualified?** Concrete qualifiers (business stage, revenue shape, offer type), not demographics. The disqualified list matters as much as the qualified one ("good friction": wrong buyers get screened out by marketing, not absorbed by engineering).
3. **What pains does it solve — what's the use case** the buyer would describe in their own words?
4. **Why does it win / what's the moat?** (Updates? service layers? proprietary methodology? data network?) If methodology is the moat, an IP-protection thread opens now (own-words gates, fingerprinted builds, quarantined source corpus).

**Layer 2 — Commercial model (how it makes money):**
5. **How are we selling it?** Sales calls, sales page, community, partners — and what's the launch motion vs the scaled motion?
6. **DIY, DWY, or DFY — or a tier ladder of all three?** What does each tier deliver?
7. **What's the price tag?** One-time vs subscription, and is there a recurring upsell beside the product (community, support, updates)?
8. **Guarantee / refund stance?** (Including hard no's, e.g. "no deferred billing ever.")

**Layer 3 — Delivery substrate (how it ships and runs):**
9. **Where does this thing live?** Present it as levels from easiest to most complicated, with pros and cons: (a) *people download it and run it on their own computer alongside Claude Code* — simplest to build and ship, nothing for you to host, but you can't see or centrally update their copies; (b) *a website/app on the internet* (cloud services like Supabase + Vercel) — usable from any browser and you control updates, but it means servers, user accounts, security, and ongoing costs; (c) hybrids of the two. This single answer reshapes the entire architecture — settle it before any schema work.
10. **What does the customer literally receive** (folder, installer, repo) **and what must they bring** (subscriptions, accounts, hardware)? State the prerequisites honestly — they belong on the sales page.
11. **Update and support channel?** How do fixes reach sold copies?

**Layer 4 — Boundaries (what keeps it safe):**
12. **Hard constraints / non-negotiables** — e.g. "completely standalone, never wired into my other systems," "ships blank-default and must run from a fresh copy." These get ⛔ headline placement in CLAUDE.md.
13. **Quarantine needs** — explain it first: "some material helps us *design* the thing but must never end up *inside* the thing we sell — other people's books or courses, client data, your personal info. Is there anything like that here?" If yes, `_NEVER-SHIP/` + ship gates.
14. **What is explicitly NOT in v1?** Name the parked things out loud (cloud tier, telemetry, extra panels) — scope creep dies in this answer.

**Layer 5 — Philosophy (the feature-rejecting principles):**
15. **The design principles** — explain the goal before asking: "these are the 3–8 rules of taste for this product — when a cool feature idea shows up six weeks from now, these rules decide whether it gets in. Things like 'every screen pushes ONE action' or 'works on your machine forever, no internet required.' What rules like that do you already feel strongly about?" Each must be concrete enough to kill a feature idea on contact.
16. **Frontend?** If a UI is built in parallel elsewhere (e.g. a browser design tool), set up the protected snapshot drop zone + conformance-skim rule.
17. **Does the product itself carry AI instructions?** If yes, the dual-CLAUDE.md routing rule applies (below).

Write the answers into the scaffolded files in the same session — the interview IS the content. Layers 1–3 seed the spec/PRD skeleton (§overview, §business model, §target buyer); layers 4–5 seed CLAUDE.md.

## Phase 2 — Scaffold the standard kit

Create, in this order:

### 1. Project `CLAUDE.md`
Sections: ⛔ non-negotiables (from Q3) → design philosophy (from Q2, numbered, with a **drift-check duty**: when the user floats an idea conflicting with the philosophy or a promoted decision, flag it conversationally BEFORE capturing it) → canonical-docs hierarchy (spec > schema > CLAUDE.md > process docs > brainstorms > memory; higher layer wins on disagreement) → process rules (below) → working norms.

Include these process rules verbatim (adapted to the project):
- **Session start:** `git status --short` + check the ledger for PENDING rows. No build work while PENDING rows older than 7 days exist.
- **Decision ledger duty:** every settled decision gets a ledger row the moment it's made; idea-centric (search for an existing entry FIRST; resurfacing ideas append a ref, never a duplicate row). Contradictions of PROMOTED entries → flag to the user, then mark the old row SUPERSEDED.
- **Repo-map duty:** any file create/move/delete updates `REPO-MAP.md` in the same action.
- **Commit cadence:** one commit per coherent unit (grill wrap-up, promotion sweep, schema change); Claude runs git, the user never types git commands.
- **CLAUDE.md curation (every wrap-up):** did this session surface anything that must shape EVERY future session? Propose a 1–2 line addition, add on the user's confirm. High bar — detail lives in the spec/ledger; this file gets only the rule or the pointer.
- **Milestone reviews:** at every spec version bump / pre-build gate / pre-ship gate, run a fresh-eyes consistency review — independent agents reading the docs cold + a cross-doc agreement check. Editors can't see their own drift.
- **Battery protocol:** stress-tests = "batteries" — independent fresh-eyes agents attacking the spec through lenses the editors haven't used (simulate users · adversarial security/abuse · business ops · resource arithmetic · instruction-coherence are proven ones). Full agent transcripts ARCHIVED under `audit/` with **parent/child links between the synthesis file and the transcripts** (every conclusion traceable to its source). Keep an **experiment registry** (test types + last-run dates): try ≥1 NEW lens per battery; rerun the most useful batteries at pre-build. **Mini-battery** = ~3 agents validating one specific scenario cheaply.
- **Gap-scan duty (every brainstorm checkpoint):** scan for (a) unbound parameters — propose a concrete default, never a silent TBD; (b) contradictions with promoted decisions/philosophy; (c) ledger rows not updated in the same action; (d) standing-rule candidates — name them NOW with a proposed durable home, confirm with the user, write in the same action; (e) existing-home check — before proposing any new store/structure/file, SEARCH for an existing home; (f) ambiguous referents — a number/date pointing at an unnamed thing gets an open question, never a guessed binary.
- **Paste guard:** a `[Pasted text #N]` placeholder whose content didn't arrive = STOP and request a repaste immediately; never checkpoint past it; unrecovered = a permanent `LOST-INPUT` flag that blocks session completion. Long pastes → suggest file drops into `brainstorms/inbox/`.
- **Dual-CLAUDE.md routing** (only if the product ships AI instructions): the dev repo's CLAUDE.md governs build sessions; the shipped product carries its OWN CLAUDE.md. Every captured rule states which file it targets; shipped-instance content accumulates in the spec/ledger until authored at build — never lands in the dev file, and vice versa.
- **Core-structure auto-propagation:** whenever a core process structure changes (ledger format, repo-map protocol, tombstones, dependency tracking, battery protocol), update this skill's source spec in the same action — unprompted.

### 2. `brainstorms/DECISIONS.md` — the decision ledger
Header defines: **Statuses** — 🔴 PENDING (decided, awaiting promotion into the docs) · 🟡 DISCUSS (direction chosen, needs conversation to finalize) · 🎯 QUEUED-GRILL (needs its own deep-dive session) · ✅ PROMOTED (applied; target column shows where) · ⛔ SUPERSEDED (target column = the dead text to remove). **Index sorting rule:** active on top — PENDING first, then QUEUED-GRILL in dependency-tree order, then DISCUSS; completed sinks to the bottom; re-sort on every edit. Body: an Index table (ID · one-line decision · status), a **Build-sequence dependency tree** (parent→child ordering of queued deep-dives, with the rule: never start a session whose upstream parent is unresolved), a PENDING sweep-queue section, then one detail block per decision (refs + promotion target).

### 3. `REPO-MAP.md` + `check_repo_map.py`
A table of every path: Path · Tag (SHIP / SOURCE / DEV / HISTORY / NEVER-SHIP) · one-line "what it is." Files in a mapped folder inherit the folder tag. Include the **new-file registration protocol**: (1) pattern-match to a folder convention → inherit, no reading; (2) small unrecognized text file → skim, one-line entry; (3) big/binary/unknown → ask the owner "what is this and why is it here?" Generate `check_repo_map.py`: walks the tree, diffs against the map, exits nonzero on unmapped/ghost entries.

### 4. `brainstorms/` + `PARKED-THREADS.md` + tombstones
`brainstorms/` holds dated capture files (`YYYY-MM-DD-topic.md`) + an `inbox/` for file drops. `PARKED-THREADS.md` = master recall index: a "▶ RESUME HERE" block (next action), source dumps, capture list, queued sessions, divergent thoughts, action items. **FROZEN-HISTORY tombstone convention:** every brainstorm capture opens with a banner stating it is frozen reasoning history, not build instructions — superseded decisions inside must not masquerade as current; the skill stamps this banner on every new capture automatically.

### 5. `_NEVER-SHIP/` quarantine (if Q4 said yes)
With a README stating: nothing in the product may reference paths inside it; ship-time = copying the product folder ONLY (default-deny). Add `_NEVER-SHIP/raw/` to `.gitignore` if it will hold licensed/personal data; offer a separate private backup repo for it.

### 6. Verification battery — generate all four checkers
- `check_repo_map.py` (above)
- `check_promotions.py` — reads ledger claims (PROMOTED targets, parked claims) and verifies them against the actual docs; run at session end + before every promotion-sweep commit.
- `check_grill_complete.py` — computes brainstorm-session completion (lost-paste flags, open flags, unrouted "→ route to X" arrows); must pass before a session is stamped COMPLETE.
- `check_orphans.py` — finds files referenced nowhere and not convention-covered; flag → ask the owner before registering or removing.

### 7. `schema/system-flow-map.md` (+ `.html` when there's a pipeline)
Standard artifact: sources → engines → surfaces, status-colored, built FROM the spec + ledger statuses (never from brainstorm captures), regenerated in the same commit as any spec change.

### 8. `ui_versions/` (if Q5 said yes)
PROTECTED drop zone for frontend snapshot zips. Never delete the newest zip; older only with explicit OK. Every new zip gets a conformance skim against the spec's locked sections; each divergence becomes a ledger row. Mid-build incongruence is EXPECTED — noted, not flagged as a problem.

### 9. `git init` + first commit
Commit the scaffold as the first coherent unit. If the user wants off-machine backup, create private remote(s) — quarantined raw data gets its own private repo, never the public one.

## Companion skills (the kit travels as a set of three)

This skill scaffolds the *structure*; two companion skills run the *sessions* inside it. When sharing this kit with someone, send all three folders for `~/.claude/skills/`:
- **`Grill Me`** — runs the brainstorm/interview sessions with checkpointing, gap-scans, and parked-thread maintenance. The init interview above uses its method.
- **`flow-map`** — generates the interactive HTML system flow map (the standard artifact in #7).
- **`battery`** — runs the milestone stress-tests (full and mini batteries) with transcript archiving, synthesis↔transcript linking, and the experiment registry.

Also scaffold a **spec/PRD skeleton** at the repo root from the interview: §0 document map (source-of-truth hierarchy) · §1 product overview (the one-sentence purpose) · §1a business model (tiers/pricing/guarantee from Layer 2) · §3 target buyer + disqualifiers · §parked (the explicit NOT-v1 list from Q14).

## Phase 3 — Educate, orient, and push to the next step
Scaffolding is not the finish line — a user who doesn't know what to do next will stall. End every init by, in plain language matched to their Phase-0 level:
1. **Explain what just got built and why** — each file/folder in one sentence, framed by the problem it prevents ("DECISIONS.md is the logbook so no decision ever gets lost or silently contradicted").
2. **Explain the toolkit** — each available skill, what it does, and *when to reach for it*: **Grill Me** when an idea needs to be pulled out of their head and stress-tested; **flow-map** when they want to SEE the system; **battery** at milestones when the design needs attacking by fresh eyes; this skill again for the next project.
3. **Walk the session loop they'll live in:** session start (git status + PENDING check) → brainstorm/grill with checkpoints + gap-scans → ledger rows same-action → promotion sweeps into the spec → checkers at session end → commit (+push) → wrap-up curation question. Remind them: the system is built so that forgetting is safe — every rule has a checker or a same-action duty.
4. **Name the next concrete action and push toward it.** Don't end with "good luck" — end with "the next thing we do is X; want to start now?" (Usually: the first deep-dive Grill Me on the biggest unresolved design question from the interview, which the dependency tree should already show on top.)
