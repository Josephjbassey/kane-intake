# Hackathon Plan — Kane CLI Hackathon by TestMu AI

**Folder:** `/mnt/Development/Linux/hackathon/kane-cli-hackathon-2026/`
**Deadline:** 19 Nov 2026, 11:59 PM IST

## One-Sentence Pitch
A document-digitization intake agent that accepts uploaded PDFs/images, extracts structured data via an AI agent, and uses Kane CLI to verify the full upload → OCR → extraction → validation flow end to end in a real browser.

**Demo promise:** Upload a document, watch the agent extract fields, and see Kane CLI confirm the extracted data matches — all recorded in a 3-minute video.

## Kane CLI Agent Integration (critical — required for scoring)

Kane CLI is the only mandatory requirement beyond building with an agent. Here's how to wire Hermes Agent (or any agent) to Kane CLI:

**Install prerequisites:**
```bash
npm install -g @testmuai/kane-cli        # Kane CLI itself
npx @testmuai/kane-cli-skill              # Installs Kane skill for Claude Code, Codex CLI, Gemini CLI
```

**For Hermes Agent (not covered by the skill installer):**
Append the Kane CLI instruction file at your repo root:
```bash
curl -fsSL https://www.testmuai.com/kane-cli-agent/AGENTS.md >> AGENTS.md
```
Then run objectives like: `check that the document upload page loads` or `verify extracted fields match the source document`.

**Kane CLI exit codes:**
| Code | Meaning |
|------|---------|
| 0 | Passed |
| 1 | Failed: objective ran but did not pass, or upload failed |
| 2 | Did not start (sign-in, config, no start URL, Chrome, network) — no credits used |
| 3 | Timeout or cancelled |

**Save a replayable test:**
```bash
kane-cli --name document-extraction          # writes .testmuai/tests/document-extraction_test.md + output-*/
```
Move both into the repo; without the output folder, `testmd run` re-authors every step.

**Test cases from requirements (optional but strengthens "Verified" score):**
```bash
kane-cli context ingest requirements/checkout.md --mode agent
kane-cli design tests --use-case <uc-ref> --mode agent --max 8
kane-cli cover                               # which requirements have passing evidence
```

**References:**
- Full agent instructions: https://www.testmuai.com/kane-cli-agent/AGENTS.md
- Short map: https://www.testmuai.com/kane-cli/llms.txt
- How-to guides: https://www.testmuai.com/kane-cli/agents/
- CLI reference: https://www.testmuai.com/docs/kane-cli-cli-reference
- Source: https://github.com/LambdaTest/kane-cli

## MoSCoW Feature List

### Must have (demo cannot work without these)
1. Document upload UI (PDF or image) with 10MB limits
2. AI agent extracts structured fields from the document (vendor, inv #, date, items, total: ₦12,500)
3. Kane CLI test flow that verifies extraction in a real browser (`verify the total shows ₦12,500`)
4. Closed loop: Kane tests the app → fails on planted bug → Coding Agent (Hermes) reads logs/screenshots, fixes code, reruns until 100% pass
5. Public GitHub repo + YouTube demo video (3-5 min)

### Should have (strengthens the demo; cut first if time runs short)
6. Live deployed URL (optional per rules, but good for craft score)
7. Mock invoice generation script with deterministic values
8. In-app extraction retry as secondary bonus loop

### Could have (nice-to-have; only after must-haves are demo-ready)
9. User accounts / login
9. Dashboard showing extraction history
10. Email export of results

### Won't have (explicitly out of scope)
- Mobile app (web only)
- Payments / billing
- Real user data (use mock documents only)
- Microservices (one monolith max)

## Stack Decision
| Layer | Choice | Reason |
|-------|--------|--------|
| Agent | Hermes Agent | Already known; user runs Hermes across machines |
| Backend | Django + SQLite | Already known; one database max; zero-config |
| Frontend | Django templates + HTMX + Djinn UI (`djinn-ui`) | Native Django templates styled with shadcn-like components; no heavy JS framework |
| Verification | Kane CLI (`@testmuai/kane-cli`) | Mandatory requirement |
| Deploy | Railway or Render (one-click) | One-click deploy; avoids Vercel complexity |
| Auth | None (skip; demo uses mock data) | One auth provider max; skip entirely to save time |

**Stack rule:** Everything here is already known by the user. No learning during the hackathon.

## Build Rules
- Commit early and often; one branch (`main`), no long-lived feature branches
- Deploy on day one (Friday night), even if it's just a landing page
- No performance gold-plating; no "we might need this later"
- If a feature blocks >2 hours, cut it and move on
- Record a backup demo video Saturday night (live demos fail)
- No secrets in code: API keys in `.env`, added to `.gitignore` before first commit
- Input validation on every public endpoint; limit file uploads (type + size)
- No shipping real user data — use mock documents only
- Run `pip-audit` to guarantee 0 vulnerabilities before submitting

## Pitch Outline (3 minutes)
1. **Problem (30s):** Document digitization is manual and error-prone; businesses waste hours re-typing data from PDFs.
2. **Demo (90s):** Upload mock invoice (₦12,500) → agent extracts fields → Kane CLI verifies in real browser → coding agent closed-loop fixes any detected regression.
3. **How it works (30s):** Django backend + HTMX frontend + Djinn UI + Hermes coding agent + Kane CLI verification closed loop.
4. **What's next / ask (30s):** Multi-document batch processing, email export, and production deployment.

## Submission Checklist
- [x] Repo is public with a clear README (https://github.com/Josephjbassey/kane-cli-hackathon-2026)
- [x] README has: one-line pitch, how to run locally, demo link, demo video link
- [ ] Deployed link works (incognito test)
- [ ] Demo video uploaded to YouTube (3-5 minutes)
- [ ] Submission form filled before 11:59 PM IST on 19 Nov
- [x] At least two public posts drafted in Docs/launch-posts-draft.md
- [ ] Kane CLI installed; AGENTS.md appended to repo; at least one flow run
- [ ] TestMu AI registered; 10,000 credits claimed

## Security Notes
- [x] No secrets in code — `.env` in `.gitignore` before first commit
- [x] No hardcoded credentials in demo data or frontend
- [x] Input validation on every public endpoint
- [x] File upload limits (type + size: 10MB) enforced
- [x] No user input executed server-side
- [x] Authentication boundary: N/A (no accounts in MVP)
- [x] No real user data — mock documents only
- [x] `pip-audit` verified cleanly: 0 known vulnerabilities
- [x] Deploy hygiene: debug mode disabled in production

## Composition Sequence (per skill)
prd-author → prebuild-plan → hackathon-plan → build
This hackathon-plan is the entry point; prd-author and prebuild-plan should be run before coding begins if scope is not already locked.
