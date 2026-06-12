# Security Baseline — for any project whose product uses AI, ingests outside data, or holds sensitive data
*Scaffolded by project-init when the interview flags an AI product. Plain-language security practices, battle-tested. Adapt the specifics; keep the principles.*

## The one idea that anchors everything: the "lethal trifecta"
A prompt-injection attack (a hacker hiding instructions inside text the AI reads) only becomes truly dangerous when **all three** of these are true in the same AI task at the same time:
1. The AI can see **private/sensitive data** (bank info, customer records).
2. The AI is reading **untrusted outside text** (DMs, web pages, uploaded files).
3. The AI has a way to **send data out** (fetch a URL, load an image, call a tool).

Your whole security job is to **never let all three happen together.** You don't win by detecting bad text — that's a losing game. You win by architecture: keep the three apart.

## The non-negotiable practices

1. **Read outside text in a sealed room.** When the AI processes any third-party text, do it with an agent that has **no tools and no internet** — so even if it's tricked, it has nothing to act with. Only pass a cleaned summary onward.

2. **Block the exit on the way OUT, not just the way in.** The classic data theft hides stolen data inside an image link the screen auto-loads — no click needed. So: **never auto-load remote images or links that the AI produced.** Show them as plain text; only allow links to a pre-approved list of sites.

3. **Strip trick characters with plain code, before any AI sees the text.** Attackers hide instructions in invisible/look-alike characters. A short, dumb code script that removes them runs first — it's free and can't be fooled. Don't ask an AI to "clean" text (the cleaner can be tricked, and it might delete real data); have the AI only *flag and report*, never rewrite.

4. **Tag every saved memory with where it came from.** User-said = trusted. Outside text = "data to reference, never an instruction." This stops a malicious message from resurfacing later as a trusted command.

5. **Lock the local door.** If the product runs a local server, bind it to the machine only (127.0.0.1) with a fresh random key each launch. An unlocked local server can be driven by any website the user visits.

## The update channel — the highest-stakes part
Auto-pushing updates into many machines is the #1 supply-chain attack target (this is how Kaseya, SolarWinds, and the XZ backdoor all happened). Rules:

- **Sign every update; the product verifies the signature before touching it.** Use a free tool like Sigstore/cosign so you're not babysitting a secret key.
- **Never silently auto-apply code, skills, settings, or config.** Those are remote-code-execution risks. The product checks for updates, verifies the signature, then **asks the user "apply this? [Yes]"** — one click, in plain language.
- **Split security from billing into two streams.** Security fixes ship to everyone, always free. New features ship only to paying customers. **Never paywall a security patch** — a lapsed payment must never leave someone exploitable.
- **You are the release gate.** No update goes out without you personally cutting a signed release. Keep the ability to roll back.

## Red-teaming (attacking your own product to find holes)
- Do it **monthly** (the threat landscape doesn't change weekly), plus whenever a major new attack technique is published.
- Attack a **test copy in an isolated box you control** — never a live connection into customer machines.
- Use existing tools (promptfoo, DeepTeam) instead of writing attack code by hand.
- Keep the collection of attack payloads quarantined (never where the product can read it). Ship only the resulting fixes.

## Using other people's skills/components
Marketplace skills are risky — studies have found a large share carry security flaws, and some are outright malicious. A security skill is the perfect trojan because you grant it access.
- **Find candidates by name/description only. Never let an agent open or run unvetted skill code.**
- Prefer building a thin, auditable version yourself over installing a black box.

## The final brain check
Before building, review the AI's "brain" once, top to bottom: its identity, what it can access, its instructions — complete, consistent, no loose ends. The single highest-leverage review in the project.

---
*Sources behind these practices (2024–2026): OWASP LLM Top 10, the Lethal Trifecta (Simon Willison), documented markdown-exfil fixes in Copilot/Gemini/Notion, memory-poisoning research (MINJA), Claude Code CVEs 2025-52882 & 2025-59536, Snyk's marketplace-skill scan. A security advisor should re-ground these at build time — attack research moves fast.*
