# Claude Project Kit

Four Claude Code skills that turn a blank folder into a drift-proof project workspace — built and battle-tested while designing a real product with Claude Code daily.

**The problem they solve:** long-running AI-assisted projects rot. Decisions get lost in chat history, documents drift apart and contradict each other, and six weeks in nobody knows which file is the truth. This kit makes forgetting safe — every rule has a checker script or a same-action duty, so nothing depends on anyone's memory.

## The four skills

| Skill | What it does | When it fires |
|---|---|---|
| **project-init** | Interviews you about your project's purpose, business model, delivery method, boundaries, and design philosophy (in plain language — no jargon assumed), then scaffolds the whole workspace: rules file, decision ledger, repo map, brainstorm system, quarantine folder, verification scripts, and a spec skeleton. Ends by teaching you the workflow and pointing at your next step. | Starting any new project: "project init" |
| **Grill Me** | Relentless one-question-at-a-time interviews that pull a plan out of your head and stress-test it, checkpointing every answer to a file so nothing is lost. | "grill me on this idea" |
| **battery** | Multi-agent stress-tests of your spec/design: independent fresh-eyes agents attack it through different lenses (simulated users, security, business ops, capacity math…), findings get verified, full transcripts archived and linked. | Milestones: "run a battery" |
| **flow-map** | Generates an interactive HTML map of your system — data sources → engines → screens, color-coded by build status, with pan/zoom and hover-tracing. | "make a flow map" |

## Install

1. Download this repo (green **Code** button → Download ZIP, or `git clone`).
2. Copy the four folders into your Claude Code skills folder:
   - **Windows:** `C:\Users\<you>\.claude\skills\`
   - **Mac/Linux:** `~/.claude/skills/`
3. Start Claude Code anywhere and say: **"project init"**

It will take it from there — including explaining the other three skills to you when the time is right.

## Requirements

- [Claude Code](https://claude.com/claude-code) with an active Claude subscription.
- Git installed (the kit initializes a repo for your project; Claude runs all git commands for you).

## Updates

New versions roll out to this repo — re-download and overwrite the four folders to update.
