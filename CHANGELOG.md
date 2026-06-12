# Changelog — Claude Project Kit

All notable changes to the four skills (project-init · Grill Me · flow-map · battery). Newest first. Dates are when the change shipped to this repo.

The kit is dogfooded on a live project ("Good Money Dashboard") — most improvements are battle-tested fixes from real sessions, noted as such.

## 2026-06-12

### Added
- **Grill Me:** the spawn-scan — when a new idea arrives, fire 2–3 system-aware curiosity questions (how does it fit the current system? · what could it interfere with? · what's the blind spot?) BEFORE developing it. A frontline catch at idea-arrival, distinct from the gap-scan (post-checkpoint) and consequence-scan (post-lock). Near-free since grill context is already loaded.
- **battery:** self-resolution boundary (anti-drift) — when acting on findings, an agent may only do documentation hygiene + capture open items; it may never silently change a locked decision, promote to the spec, or resolve a design call without the owner, and every batch ends with a reviewable what-changed/how-to-revert summary. *Born from the owner asking "how do I know your auto-fixes stay in line with my decisions?" — the honest answer is a hard boundary + an audit trail, not trust.*
- **project-init:** security baseline — a plain-language security-practices doc (`security-baseline.md`) scaffolded for any AI product: the "lethal trifecta" principle, tool-less ingestion, outbound-exfil blocking, trick-character stripping, memory provenance tags, signed ask-before-apply updates (security free for all / features gated), monthly red-teaming, marketplace-skill caution. *Distilled from a live security review that caught a fleet-wide auto-update backdoor and an outbound data-leak path before they shipped.*
- **project-init:** the final brain-check gate — last step before build reviews the shipped AI's system prompt/CLAUDE.md for completeness, consistency, and loose ends. *Born from a real oversight: the advisor identity was nearly designed into conversation history (where it decays) instead of the system prompt (where it's re-sent every turn).*
- **project-init:** changelog discipline — when the kit edits its own skills, every change ships a CHANGELOG entry in the same commit, with the real bug/session that prompted it.
- **project-init:** Phase 0 — gauge the user's technical level FIRST, then tailor all language to it (non-coders get plain words + a setup sentence on every jargon term). Reworked the delivery-substrate question into easiest→hardest options with pros/cons.
- **project-init:** Phase 1.5 — MVP scope-lock drill (identify Tier 1 fast, tier everything else, hold the line against mid-project scope creep).
- **project-init:** Phase 3 — closes by educating the user on what was built, explaining each companion skill + when to use it, and pushing toward the named next action.
- **project-init:** ledger completeness counter convention (the index is status-sorted, never numeric — the counter is the at-a-glance integrity check). *Fix born from a real "the ledger looks truncated at D-024" scare — it wasn't; status-sorting just hid the high numbers.*
- **project-init / first-map reveal:** auto-open + guided plain-language tour the first time a project's system-flow-map is generated.
- **battery:** new skill — multi-agent stress-test batteries (full + mini), fresh-eyes lenses, adversarial grounding, full transcript archiving with parent/child links, per-project experiment registry. *Born from losing a battery's agent transcripts because only the synthesis was saved.*
- **Grill Me:** consequence-scan rule — every RESOLVED decision gets its second-order questions enumerated (grilled now or queued), never a silent RESOLVED stamp.
- **flow-map:** educational node tooltips (ⓘ dot + plain-words popup), status badges (✓ specced / ◐ direction-set / ○ not-designed), next-step + blocker lines on pending nodes, animated blocker arrows ("① build first → ② then this unlocks") with tooltip auto-placement away from the chain, NEXT-UP treatment on the docket's top item, click-to-read drawer (nodes AND category panels) with an audience-relative "why it matters" section.
- **flow-map:** home-vs-workplace rule — a module that lives in one layer but operates on another draws BOTH its home column and a dotted duty wire to where it works (never phantom-duplicate a shared layer). *Born from a bridge sub-module that looked mis-placed because its operating wire wasn't drawn.*

### Changed
- Repo restructured so the four skills are the single source of truth; the local `~/.claude/skills/` entries are junctions into this repo (no more copy-drift between "the skills I use" and "the skills I publish").

## 2026-06-11 — initial kit
- Extracted the decision-discipline system battle-tested on a live project into four shareable skills: **project-init** (scaffold a drift-proof workspace), **Grill Me** (checkpointed interview sessions), **flow-map** (interactive system maps), and the conventions they share (decision ledger, repo map, parked-threads, quarantine, verification checkers).
