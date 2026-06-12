# Lessons — the reactive-learning half of the kit's self-improvement

Every entry is a real-world miss that taught the kit something. The intelligence is in the **clusters**: when several misses share a root cause, we abstract a **principle** that kills the whole family — not just the instance. Each fix is judged against the kit's Commander's Intent (a fast, clean, buildable spec with minimal user friction). Newest clusters on top.

> How this works: a miss surfaces in real use → it's logged here → a fix is proposed → on the owner's confirm, the fix goes into the skill + a "born from real X" CHANGELOG note. Propose-and-confirm, never silent self-rewrite.

---

## Principle: a skill update must change the METHOD, never the user's WORK
*(cluster: restart-risk · silent-gap-on-update)*
- **Miss:** updating skills could throw an in-progress project back to square one. **Fix:** no-restart idempotency guard (Phase −1) + `UPDATING.md` (skills and projects live in separate places). 
- **Miss:** a newly-added interview question would never reach a project that already passed its interview. **Fix:** `interview-checklist.md` + a backfill check on update — existing projects get asked only what's new.
- **The family this kills:** any future change that could clobber, restart, or silently skip part of a user's accumulated work. New rule of thumb: every kit change asks "what does this do to someone who's mid-project?"

## Principle: the AI must hold the REAL problem, or it drifts to generic
*(cluster: drift · ambiguity-is-drift)*
- **Miss:** a non-technical user's AI didn't understand her actual job/pain and drifted into generic software. **Fix:** Layer-1 deep pain excavation + the North Star block anchored at the top of CLAUDE.md (re-read every session) + a drift-guard rule.
- **Miss:** SPEC-first/code-last was only *implied* by the process, so an AI started drifting toward writing code mid-design. **Fix:** made it an explicit hard rule.
- **The family this kills:** anything load-bearing that's left implicit. New rule of thumb: if a rule matters, STATE it; if a purpose matters, ANCHOR it where it's re-read.

## Principle: skills must be SELF-CONTAINED — never depend on the author's machine
*(cluster: downgrade-to-simpler · missing-piece-in-extraction)*
- **Miss:** the flow-map skill told the AI to "copy the author's project map as the template," but that file only existed on the author's machine — so other users' AIs improvised a plainer grid-of-cards. **Fix:** bundled the full interactive `template.html` inside the skill.
- **Miss:** when that template was extracted, the bottom build-status board got left out, so generated maps shipped without it. **Fix:** added the sections to the template; skill marks them required.
- **The family this kills:** any instruction that assumes access to something only the author has. New rule of thumb: a skill must produce its best output for someone who has ONLY the skill — and when extracting a template from a real artifact, verify every standard part survived.

## Principle: self-improvement needs a stated objective, or it gold-plates
*(cluster: aimless-improvement)*
- **Insight (not a bug — caught proactively):** an unguided "self-improving" system tinkers, adds complexity, optimizes the wrong thing. **Fix:** the **Commander's Intent** — a stated end-state every improvement is judged against ("does this serve it?"). Lets the AI use initiative while staying coherent.

---
*This log is the dogfood record of the kit improving itself from real use. It is also the seed of a future cross-project battery/lessons index (held for now — privacy + malicious-contribution security need their own design pass).*
