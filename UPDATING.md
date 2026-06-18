# Updating the kit — without losing any of your work

## Easiest way: just tell Claude "update the project kit"
You don't need to copy any URLs or download anything by hand. In your terminal, just say:
> **"update the project kit"** (or "update my project-init skills")

Claude knows the source and does it for you. **Canonical source: `https://github.com/GarenP/claude-project-kit`**

**The exact procedure Claude follows when you ask to update (Claude: do this):**
1. Clone the repo fresh to a temp folder (`git clone https://github.com/GarenP/claude-project-kit`), or `git pull` if a local clone already exists.
2. Copy the eight skill folders — `project-init`, `grill-me`, `flow-map`, `battery`, `retrospective`, `finalize`, `isolated-battery`, `corpus-intake` — into the user's skills directory (`~/.claude/skills/` on Mac/Linux, `C:\Users\<user>\.claude\skills\` on Windows), overwriting ONLY those eight folders. (On the maintainer's own machine these are symlinks INTO this repo, so they update automatically — see the symlink note below.)
3. Confirm what changed (read the new `CHANGELOG.md` and summarize it for the user).
4. **NEVER touch the user's project files.** Skills update; projects don't. Then they keep working — an already-set-up project continues where it left off and backfills any newly-added interview questions (see the no-restart guard).

---



**The one thing to know: updating these skills NEVER touches your project.** The skills live in one place; your project lives in another. They're separate.

- **The skills** live in `~/.claude/skills/` (Mac/Linux) or `C:\Users\<you>\.claude\skills\` (Windows). Updating them = replacing those skill folders.
- **Your project** (your spec, your DECISIONS ledger, your code, your North Star) lives in your project's own folder. Nothing here changes when you update a skill.

So a kit update changes the *method* the AI uses — never your accumulated work. You will not be restarted.

## How to update (safe, 30 seconds)
1. Download the latest kit (this repo: green **Code** → Download ZIP, or `git pull` if you cloned it).
2. Replace the eight skill folders in your skills directory with the new ones: `project-init`, `grill-me`, `flow-map`, `battery`, `retrospective`, `finalize`, `isolated-battery`, `corpus-intake`. (Overwrite the old folders — that's the whole update.)
3. Done. Open your project as normal and keep working — the AI picks up where you left off.

## Built-in protections (so an update can't restart or "dumb down" your project)
- **No restart:** if you run `project init` on a project that's already set up, the skill DETECTS it and switches to continue-mode — it will NOT re-scaffold or overwrite your files. It picks up where you are.
- **Your settings persist:** your project's "North Star" (why you're building this) and your communication level (e.g. "explain in plain words") are written into your project's own `CLAUDE.md`. A skill update can't erase them — they live with your project, not the skill, and the AI re-reads them every session.
- **Your decisions are sacred:** the anti-drift rule means the AI does documentation hygiene and captures new ideas, but never silently rewrites a decision you made.

## For the maintainer (Garen) — STANDARD PROCESS for every push to this repo
Every time you push a kit update, confirm all four before committing:
1. **No-restart preserved** — the idempotency/continue-mode guard in `project-init` (Phase −1) is intact; nothing new makes the AI re-scaffold an existing project.
2. **Settings persist** — nothing removes the North-Star or communication-level persistence into the project's CLAUDE.md.
3. **Plain language preserved** — the non-technical-communication instructions (Phase 0 + the communication-level note) stay intact; updates must not reintroduce engineer-to-engineer talk for non-coders.
4. **Changelog entry** — every change ships a `CHANGELOG.md` line, with the real bug/feedback that prompted it.
Then ship. The promise to users: an update improves how the AI works, and never costs them a single thing they've already built.
