---
name: isolated-battery
description: Launch a standalone, fully-ISOLATED, READ-ONLY agent that stress-tests a target (a doc/decision system, a spec, a pipeline) in total isolation — it simulates changes and hunts for drift, bloat, contradictions, sync-failures, and holes, but CANNOT modify anything. Use when you want a safe sandbox stress-test that changes nothing, an isolated drift/consistency probe, a "what would break if a decision changed" check, or when the AI elects to verify its own work with zero risk. Sibling to the `battery` skill but guaranteed non-destructive and single-isolated-agent. Triggers: "run an isolated battery", "isolated test", "sandbox stress-test", "drift probe", "check this in isolation".
---

<!-- 🔄 SELF-UPDATE: if the user says "update the project kit / these skills", pull https://github.com/GarenP/claude-project-kit and copy the skill folders (project-init, Grill Me, flow-map, battery, retrospective, finalize, isolated-battery) into their ~/.claude/skills/ — overwrite only those folders, NEVER touch their project files, then summarize CHANGELOG.md. Full steps in UPDATING.md. -->

# Isolated Battery — a zero-risk, read-only stress-test in total isolation

A focused, **non-destructive** probe: spawn ONE isolated agent that can read everything but **change nothing**, point it at a target, and have it adversarially hunt for problems — then report. The guarantee is the point: it physically cannot edit, create, delete, or commit, so it's safe to run anytime, including on the AI's own just-finished work.

**How it differs from `battery`:** the full `battery` skill fans out *multiple* agents through many lenses and is part of milestone/pre-ship gates. The isolated battery is *one* agent, *guaranteed read-only*, run *electively* (the AI can decide to fire it mid-task to sanity-check itself) or on request. Use it for fast, safe self-verification; use `battery` for the heavyweight multi-lens audit.

## When to run it
- You want to verify a doc/decision system isn't drifting, bloating, or contradicting itself — **without touching it**.
- Before (or inside) a `finalize` run, as the optional isolation check.
- The AI just generated/edited a set of artifacts and wants an independent cold read before claiming they're correct.
- On request: "run an isolated battery on X."

## How to run it (the protocol)

1. **Define the target + the question** in one line (e.g. "the `docs/` ↔ `DECISIONS.md` linking system — does it drift, bloat, or leave anything unsynced?").
2. **Spawn ONE isolated, read-only agent.** Guarantee read-only by BOTH:
   - Use a write-less agent type where available (e.g. `Explore`), OR a `general-purpose` agent with an explicit, repeated instruction: *"STRICT READ-ONLY. Do NOT Write, Edit, create, delete, or modify ANY file. Use only Read, Grep, Glob, and read-only Bash. This is a non-destructive audit; report findings only."*
   - (Optional, for true filesystem isolation: run it in a throwaway git worktree so even an accidental write can't touch the working tree.)
3. **Give it an adversarial, simulation-based mandate**, e.g.:
   - Run any existing checkers and report what they catch vs miss.
   - **Simulate 2–3 "a thing changes" scenarios** and trace whether the system routes/syncs the change cleanly or drifts (e.g. "a price changes in one doc but not the registry — caught or not?").
   - Hunt for **bloat/duplication** (the same fact in N places that could diverge), **contradictions**, **stale content**, and **holes** the automated checks don't defend against.
4. **Collect the findings** and surface them. If the audit found real issues, route them (a ledger row, a fix, a flag) — but the isolated agent itself changed nothing; any fix is a deliberate, separate step the main agent takes.

## Output
A structured findings report: what the checks catch vs miss · the simulation traces with a drift verdict each · bloat/duplication with locations · holes + recommendations · any stale/contradictory content. Nothing in the repo is modified.

## Notes
- Keep it ONE agent and READ-ONLY — that's the contract. If you need many lenses or it needs to write fixes, you want `battery` (for breadth) or the main agent (for fixes), not this.
- Archive notable findings under `audit/` with a date + the target, so the probe's discoveries aren't lost.
