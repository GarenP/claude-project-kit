---
name: corpus-intake
description: Ingest source material (books, PDFs, transcripts, research docs, articles) into a project's quarantined corpus — archive the raw, convert to clean markdown, image-capture + cite any figures/visual imagery, and register it — so it's ready as falsework for own-words extraction. Use when the user says "ingest these books / this research", "parse this into the corpus", "add to the never-ship", "build the dataset from these", or before firing rubric/knowledge-building agents that need a rich source set. Handles the "copy in, never wire to the source" standalone rule + the falsework / own-words gate automatically.
---

<!-- 🔄 SELF-UPDATE: if the user says "update the project kit / these skills", pull https://github.com/GarenP/claude-project-kit and copy the skill folders (project-init, grill-me, flow-map, battery, retrospective, finalize, isolated-battery, corpus-intake) into their ~/.claude/skills/ — overwrite only those folders, NEVER touch their project files, then summarize CHANGELOG.md. Full steps in UPDATING.md. -->

# Corpus Intake — turn raw source material into clean, cited, quarantined falsework

One repeatable pipeline so you never re-explain it: point it at books / PDFs / transcripts / research docs, and it lands them in the project's quarantine as clean markdown with figures captured + cited, registered and ready for the own-words extraction that downstream agents (rubrics, knowledge bases, methodology) build from.

## Non-negotiables (read first)
- **COPY IN, never wire out.** Sources living outside the project (e.g. a personal "brain"/Research folder) are **copied INTO** the project's `_NEVER-SHIP/`. NEVER make the product read from an external path — that breaks the standalone-template rule. The skill ingests a copy; the original stays where it is.
- **Falsework + own-words gate.** Everything ingested is third-party, copyrighted **falsework** — it lives in `_NEVER-SHIP/` (quarantine, never shipped) and is only ever used to extract METHOD/ideas; shipped artifacts carry OWN-WORDS rewrites, never the source's expression. Flag borrowed phrasing `[OWN-WORDS REBUILD]`.
- **Archive raw FIRST, never parse-in-place.** The untouched original is archived flat before any conversion, so a bad parse never destroys the source.

## The pipeline

### 0 — Scope + HITL selection
- Confirm the source list (paths/URLs) and the destination project's `_NEVER-SHIP/`.
- If there are MANY candidate books/docs, present a **shortlist for the user to pick** (don't blind-ingest a whole library) — title · why it's relevant · which pillar/topic it enriches. Ingest the chosen set.

### 1 — Archive the raw
- Copy each source untouched to `_NEVER-SHIP/raw/<source-type>/archive/` (e.g. `raw/books/archive/`, `raw/youtube/archive/`). This is the immutable original.

### 2 — Convert to markdown
- Per source produce a clean `<title>.md` + a `<title>.index.md` (table of contents / section index for fast retrieval).
- **Use the project's existing converters if present** (`_convert_corpus.py`, `_ocr_acq.py` under `_NEVER-SHIP/raw/books/`) — they're already tuned. Otherwise: pandoc/markitdown for documents, OCR for scanned/image PDFs, the `transcribe` skill for audio/video.
- Keep main context lean — run heavy conversion via **subagents**, don't read whole books into the main thread.

### 3 — Image-capture figures (visual books)
- For any source with figures/diagrams/charts that carry meaning, **extract the images**, downscale them, store under `_NEVER-SHIP/raw/<type>/images/<title>/`, and **link + cite** them from the markdown at the point they're referenced (`![fig](images/<title>/figN.png)` + a citation line). So a downstream agent can cite a visual, not just prose.

### 4 — Register
- Add a row to `_NEVER-SHIP/raw/.../_CORPUS-REGISTRY.md` (or create it): title · author · source · type · topic/pillar it enriches · status (`raw` / `converted` / `figures-done` / `own-words-extracted`).
- Update `REPO-MAP.md` if a new folder/source-type appeared.

### 5 — Hand-off
- Report what was ingested + where, the registry deltas, and which pillars/topics it now enriches — so the next step (own-words extraction / rubric agents) knows what's available. Do NOT do the own-words rewrite here — that's a separate, deliberate step.

## Notes
- Diarize **multi-speaker** audio/video (A–B interviews, panels) through the transcribe path before treating it as one source (speaker labels matter for who-said-what).
- Capture each source's **publish date** at intake — fast-moving domains (social/marketing) weight by recency downstream.
- This skill ENDS at "registered, cited, ready." Extraction, rubric-building, and shipping are downstream and deliberate.
