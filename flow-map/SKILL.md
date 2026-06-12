---
name: flow-map
description: Build or update an interactive HTML system flow map (data pipeline / backend architecture diagram) with pan/zoom, hover-tracing, and status colors. Use when the user asks for a system flow map, pipeline visualization, architecture diagram, data-flow chart, or to update an existing system-flow-map.html. Standard artifact for every project (auto-updated at promotion sweeps).
---

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

- **Wheel zoom toward cursor + drag pan + "⟲ fit" button** (transform translate+scale on an absolutely-positioned canvas div).
- **Hover-tracing:** hovering a node sets `hot` on every path whose member-set contains it and `dim` on the rest; non-neighbor nodes fade. Register membership per path when drawing (`addPath(d, cls, members[])`) — trunks list ALL their feeders so hovering one feed lights the whole river.
- Wires drawn into one absolutely-positioned `<svg>` from DOM offsets (`offsetLeft/Top` walk) after layout; redraw on resize.

## Reference implementation

`Good Money Dashboard/schema/system-flow-map.html` is the living template (Senti palette: espresso/burgundy/cream/orange). Copy its skeleton for new projects; swap the palette to the project's brand. Keep the companion `.md` (editable outline + status table) in sync.

## Source of truth + regeneration cadence (standing rule)

The map is **built from the project's canonical spec** (the PRD / layer-1 doc) **+ the decision ledger's statuses** — NEVER from raw brainstorm captures or from memory. Cite the source sections in the map's header. **Regenerate the map on every commit that touches the PRD** (promotion sweeps included) and on request; keep the companion `.md` outline in sync in the same commit.

## Process

1. **Inventory first:** list every node, its category, status, and every edge (with lane type) from the project's canonical docs — never from memory.
2. **Plan coordinates on paper** (in-thinking): assign panel x-ranges with ≥120px corridors; order nodes within panels so flow-neighbors are y-aligned and wires don't cross; place the hub center.
3. **Build** the HTML; derive wire control points from node positions (avoid magic literals where possible).
4. **Render & validate loop (mandatory):** open in the browser (`Start-Process <file>` on Windows). Ask the user for a screenshot (or read one they drop) and audit: text clipping · unintended overlaps · arrows crossing foreign panels · ambiguous labels · uneven spacing · unbalanced composition · does the eye flow the designed path? Fix and re-render. Typically 2–3 iterations — expect the user's eye to be the final judge.
5. **Checkpoint before big rewrites:** commit + git tag (`flow-map-vN-checkpoint`) so any version is one command away from restoration.

## What NOT to do

- Don't use Mermaid/auto-layout for the final artifact — auto-layout staggers categories and tangles wires (it's fine for a quick draft).
- Don't make every wire the same weight/color — that's how diagrams become spaghetti.
- Don't put each node in an identical card grid ("Kanban look") — shape + scale must carry meaning.
- Don't draw a wire when adjacency can carry the relationship (satellites touching the hub need only a stub).
