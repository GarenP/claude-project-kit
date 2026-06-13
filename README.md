# Claude Project Kit

Five Claude Code skills that turn a blank folder into a drift-proof project workspace — built and battle-tested while designing a real product with Claude Code daily.

**The problem they solve:** long-running AI-assisted projects rot. Decisions get lost in chat history, documents drift apart and contradict each other, and six weeks in nobody knows which file is the truth. This kit makes forgetting safe — every rule has a checker script or a same-action duty, so nothing depends on anyone's memory.

## The five skills

| Skill | What it does | When it fires |
|---|---|---|
| **project-init** | Interviews you about your project's purpose, business model, delivery method, boundaries, and design philosophy (in plain language — no jargon assumed), then scaffolds the whole workspace: rules file, decision ledger, repo map, brainstorm system, quarantine folder, verification scripts, and a spec skeleton. Ends by teaching you the workflow and pointing at your next step. | Starting any new project: "project init" |
| **Grill Me** | Relentless one-question-at-a-time interviews that pull a plan out of your head and stress-test it, checkpointing every answer to a file so nothing is lost. | "grill me on this idea" |
| **battery** | Multi-agent stress-tests of your spec/design: independent fresh-eyes agents attack it through different lenses (simulated users, security, business ops, capacity math…), findings get verified, full transcripts archived and linked. | Milestones: "run a battery" |
| **flow-map** | Generates an interactive HTML map of your system — data sources → engines → screens, color-coded by build status, with pan/zoom and hover-tracing. | "make a flow map" |
| **retrospective** | Mines a captured conversation, mock, or real transcript for the method, signals, and rules inside it, turning them into buildable structure + clarifying questions tied to the moment each arose. The convergent counterpart to battery: a battery finds a spec's flaws, a retrospective harvests the method out of a conversation. | After a mock/call: "run a retrospective" |

## Install

1. Download this repo (green **Code** button → Download ZIP, or `git clone`).
2. Copy the five folders into your Claude Code skills folder:
   - **Windows:** `C:\Users\<you>\.claude\skills\`
   - **Mac/Linux:** `~/.claude/skills/`
3. Start Claude Code anywhere and say: **"project init"**

It will take it from there — including explaining the other four skills to you when the time is right.

## Requirements

- [Claude Code](https://claude.com/claude-code) with an active Claude subscription.
- Git installed (the kit initializes a repo for your project; Claude runs all git commands for you).

## Updates

New versions roll out to this repo. **To update, just tell Claude in your terminal: "update the project kit."** It pulls the latest from `https://github.com/GarenP/claude-project-kit` and refreshes the five skill folders for you — no copy-pasting URLs, and **it never touches your project** (skills update; your work doesn't). An already-set-up project picks up where it left off and backfills any newly-added questions. Details in [`UPDATING.md`](UPDATING.md).
