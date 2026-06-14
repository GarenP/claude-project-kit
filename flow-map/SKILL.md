---
name: flow-map
description: Build or update an interactive HTML system flow map (data pipeline / backend architecture diagram) with pan/zoom, hover-tracing, and status colors. Use when the user asks for a system flow map, pipeline visualization, architecture diagram, data-flow chart, or to update an existing system-flow-map.html. Standard artifact for every project (auto-updated at promotion sweeps).
---

<!-- 🔄 SELF-UPDATE: if the user says "update the project kit / these skills", pull https://github.com/GarenP/claude-project-kit and copy the five skill folders (project-init, Grill Me, flow-map, battery, retrospective) into their ~/.claude/skills/ — overwrite only those folders, NEVER touch their project files, then summarize CHANGELOG.md. Full steps in UPDATING.md. -->

# Flow Map — interactive system/pipeline diagrams as a single HTML file

Build self-contained HTML diagrams (no build step; only Google-Fonts CDN optional) that read like a backend engineer's whiteboard but look brand-grade. Adapted from the Excalidraw diagram skill's principles, re-targeted at our hand-positioned HTML+SVG template.

## The two validation tests (run before AND after building)

- **Isomorphism test:** if you removed every label, would the *structure alone* still communicate the architecture? (Trunks converging into a fat hub = ingestion; a gate bar above a column = access control.)
- **Education test:** can a non-architect learn how the system works by tracing it for 60 seconds, or does it just label boxes?

## Layout principles (the ones that actually make it readable)

1. **One dominant story.** The happy path reads as a thick left→right spine: sources → processing → THE HUB → engines → outputs. Everything else is visually subordinate.
2. **Hub treatment.** The most important node (usually the database/core store) is the LARGEST element, center-stage, with a glow ring. Hierarchy through scale: hero ≈ 2× primary ≈ 2× secondary.
3. **Bundle wires like a river.** N parallel feeds merge into a bus bar → ONE thick trunk into the hub. Never draw N parallel curves to the same target.
4. **Arrowheads on everything.** Direction is never inferred. SVG `marker-end`.
5. **Color-code lanes** (e.g. olive = auto-ingest, cream = validated, orange = outputs, dashed amber = special/skeptical). Legend chips up top.
6. **Row alignment.** Each engine/process sits at the same y as the output it drives — short straight arrows are the most readable connector that exists.
7. **GENEROUS group spacing.** Category panels (visible soft containers with floating titles) separated by ≥120px corridors. Wires live in the corridors; nothing crosses a panel it doesn't belong to. Whitespace = importance: the hub gets the most empty space around it.
8. **Container discipline.** Group membership = containment in a titled panel, never position-guessing. But don't box labels — wire labels and zone subtitles are free-floating text.
9. **Same-column (vertical) edges bow sideways** through the corridor to clear intermediate nodes; long cross-board edges sag through the empty corridor *below* the panels rather than crossing them.
10. **Canonical category set for data systems** (adapt as needed): Sources (split by lane if validation differs) · Validation/Ingestion · **Storage (its own category — all stores/cylinders live here)** · Engines/Processing · Outputs/Screens. A gatekeeper (access/unlock controller) renders as a bar ABOVE the column it governs, dotted drop labeled "gates …".
11. **Claude bridge is ALWAYS shown when the system uses Claude as its engine — even before it's specced.** Any project whose product runs on Claude (Claude Code / Agent SDK / API) has a bridge layer: the connection between the app and Claude that every AI feature flows through. Render it as its own category/column (a `.gate` bar or a panel) sitting BETWEEN storage and the engines/screens, marked `.todo` (planned) with a plain placeholder tip ("the connection to Claude — every AI feature runs through here; details get filled in as the project defines them") until the project clarifies what processes through it. Update it on every regeneration as the bridge's sub-modules (invocation, sessions, security, batching) get defined. Don't wait for a finished spec to draw it — its existence is implied the moment the project chose Claude as its engine.
12. **Home vs workplace (cross-cutting modules):** when a module LIVES in one layer but OPERATES on another flow (a bridge sub-module guarding the inbound lanes; shared infrastructure serving two directions), draw BOTH: the node sits in its home column (where it gets built), and a **dotted duty wire** runs to where it actually works, labeled with the duty ("inspects all 3rd-party text first"). A node whose label implies a position its wires don't show is a map error — the reader will reasonably ask "shouldn't this be over there?", and the answer must already be drawn. One shared layer serving multiple duties is ONE column with duty wires — never duplicated into two phantom layers.

## Required bottom sections (the map is a STATUS BOARD, not just a picture)
Every map MUST end with two `<section>` blocks below the interactive canvas (the bundled `template.html` includes them — keep them, populate from the ledger): **(1) Build sequence** — the ordered stages as a `.stair` strip; **(2) Build status** — a `<table>` of Component · Status · Where, with `tr.done`/`tr.wip`/`tr.todo` status stripes. Without these, the reader can't see at a glance what's built vs. planned. (Real bug: a generated map shipped without them because they were missing from the template.)

## Shape semantics (CSS classes in the template)

| Meaning | Shape | Class |
|---|---|---|
| External feed / input | Slanted parallelogram | `.src` |
| Document / artifact | Folded-corner page | `.doc` |
| Process / engine | Double-strut box (predefined-process) | `.proc` |
| Data store | Cylinder (CSS ellipse cap) | `.store` (+`.hub` for the hero) |
| UI / screen | Mini browser window (dots + title bar) | `.ui` |
| Gatekeeper | Dark bar | `.gate` |

Status states: `.（default）` = locked/specced (solid cream, orange spine) · `.wip` = direction set (amber tint, dashed) · `.todo` = not designed (ghosted translucent, muted text). Status legend always present.

## Interaction (all hand-rolled, zero libraries)

- **Wheel zoom toward cursor (clamped per-event so touchpads don't rocket) + on-screen +/− zoom buttons + drag pan + "⟲ fit" button** (transform translate+scale on an absolutely-positioned canvas div).
- **Hover-tracing:** hovering a node sets `hot` on every path whose member-set contains it and `dim` on the rest; non-neighbor nodes fade. Register membership per path when drawing (`addPath(d, cls, members[])`) — trunks list ALL their feeders so hovering one feed lights the whole river.
- **Educational node tooltips (for non-technical owners):** every node carries a hover popup that explains in plain words what the thing IS and what it does in this system ("a database — the filing cabinet where your transactions live; the engines below read from it"). A small, consistent visual cue (a tiny ⓘ dot in the node corner) signals that hovering teaches — first-time users don't know hovering does anything until something tells them. Write the popup text at the project owner's knowledge level (if the project was scaffolded by project-init, Phase 0 gauged it).
- **Status badges:** every node wears a corner badge — green ✓ = specced/locked · amber ◐ = direction set · gray ○ = not designed — with matching legend chips. Color-as-tint alone is not enough; the badge makes build status readable at a glance.
- **Next-step + blocker lines (pending nodes only, keeps clutter off built ones):** ◐/○ tooltips append two compact lines — "▸ next: \<what gets decided, and in which session/venue\>" and "⛓ waits on: \<blocker\>". When the blocker is itself a node on the map, hovering draws an **animated red dashed arrow from the blocker INTO the blocked node** (marching dashes give direction), a red "① build first" chip on the blocker, and a light "② then this unlocks" chip on the hovered node. **The tooltip card always places itself on the side AWAY from the blocker** so it never covers the chain (fall back to below/above when both sides fail).
- **Blockers self-resolve (don't hand-maintain them):** the "waits on / build first" relationship reads each blocker's CURRENT status — a blocker auto-drops the moment its node is marked done (the `activeBlk()` helper filters to nodes still `.todo`/`.wip`). So when you complete a section, just flip its status; the children's blocker arrows clear themselves. Never manually edit a child to remove a finished dependency.
- **NEXT UP treatment:** the docket's top item (from the project's dependency tree / ledger) gets a flowing animated conic-gradient ring (brand palette, CSS `@property` angle animation, blurred behind the node) + a pulsing "⭑ NEXT UP" chip — the master view answers "what's being built next?" at a glance. If the next item isn't on the map yet, that's a map gap: add the node.
- **Click-to-read drawer:** clicking any node slides a side panel with the layman's deep dive — status pill with a plain-words status sentence · "What it is" · **"Why it matters" (audience-relative: written for whoever the PROJECT serves — e.g. business owners — never engineer-speak)** · "What happens next" · "What has to come first". Escape/✕ closes.
- **Category panels are explainable too:** every group panel gets its own ⓘ dot, hover tip, and click-drawer ("SYSTEM LAYER" pill · what this layer does · why it matters · what's next when pending) — the reader can learn the system top-down (layers first) or bottom-up (nodes first).
- Wires drawn into one absolutely-positioned `<svg>` from DOM offsets (`offsetLeft/Top` walk) after layout; redraw on resize.

## Start from the bundled template — DO NOT hand-roll a simpler version

**`template.html` ships in THIS skill folder. ALWAYS copy it to `<project>/schema/system-flow-map.html` and populate it** — it carries the full interactive engine (hand-positioned nodes with meaningful SHAPES, curved SVG wires, pan/zoom, hover-tracing, ⓘ teaching tooltips, status badges, click-to-read drawer, blocker arrows). To populate: swap the `:root` palette to the project brand (keep the status colors), replace the EXAMPLE panels/nodes with the project's real ones using the right shape class per node type, fill `TIPS{}` / `WHY{}` / `PANELTIPS{}`, wire the edges in `draw()` with `addPath(...)`, and set the header title + North-Star subtitle. Keep the companion `.md` (editable outline + status table) in sync.

**❌ Failure mode to avoid (real, observed):** producing a plain CSS-grid of cards connected by text "→" arrows instead of the shape-coded, curved-wire, pan/zoom canvas. A grid of cards is NOT this artifact. The shapes carry meaning, the wires show flow you can trace, and the map pans/zooms — if those are missing, it's wrong. The bundled `template.html` already has all of it; start there, never from a blank file or from the markdown description alone.

*(The bundled `template.html` was extracted from a fully-populated real-world map — but it's self-contained, so you never need any external file; just copy and populate it.)*

## Source of truth + regeneration cadence (standing rule)

The map is **built from the project's canonical spec** (the PRD / layer-1 doc) **+ the decision ledger's statuses** — NEVER from raw brainstorm captures or from memory. Cite the source sections in the map's header. **Regenerate the map on every commit that touches the PRD** (promotion sweeps included) and on request; keep the companion `.md` outline in sync in the same commit.

## Process

1. **Inventory first:** list every node, its category, status, and every edge (with lane type) from the project's canonical docs — never from memory.
2. **Plan coordinates on paper** (in-thinking): assign panel x-ranges with ≥120px corridors; order nodes within panels so flow-neighbors are y-aligned and wires don't cross; place the hub center.
3. **Build** the HTML; derive wire control points from node positions (avoid magic literals where possible).
4. **Render & validate loop (mandatory):** open in the browser (`Start-Process <file>` on Windows). Ask the user for a screenshot (or read one they drop) and audit: text clipping · unintended overlaps · arrows crossing foreign panels · ambiguous labels · uneven spacing · unbalanced composition · does the eye flow the designed path? Fix and re-render. Typically 2–3 iterations — expect the user's eye to be the final judge.
4b. **First-render reveal (mandatory on a project's FIRST map):** auto-open the HTML for the user and give a guided plain-language tour — what the map shows, how to read it (left = where data comes from, right = what the user sees; shapes mean things; colors = build status), and point out the hover behaviors (tracing + the ⓘ tooltips). Calibrate depth to the owner's knowledge level — for a newcomer this is a teaching moment about their own system, not a render check.
5. **Checkpoint before big rewrites:** commit + git tag (`flow-map-vN-checkpoint`) so any version is one command away from restoration.

## What NOT to do

- Don't use Mermaid/auto-layout for the final artifact — auto-layout staggers categories and tangles wires (it's fine for a quick draft).
- Don't make every wire the same weight/color — that's how diagrams become spaghetti.
- Don't put each node in an identical card grid ("Kanban look") — shape + scale must carry meaning.
- Don't draw a wire when adjacency can carry the relationship (satellites touching the hub need only a stub).
