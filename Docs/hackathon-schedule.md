# Hackathon Schedule — Kane CLI Hackathon by TestMu AI

**Deadline:** 19 Nov 2026, 11:59 PM IST  
**Current date:** 13 Nov 2026 (Friday) — 1 day already elapsed (kickoff was Thu 12 Nov)  
**Remaining:** Fri 13 Nov through Thu 19 Nov (6 days)

## Phase Overview (adapted for 6 remaining days)

| Day | Date | Focus | Goal |
|-----|------|-------|------|
| Fri | 13 Nov | Idea locked, repo created, Kane CLI + agent wired, hello world deployed | Repo public, upload page renders, Kane CLI runs |
| Sat | 14 Nov | Must-have #1: document upload + agent extraction | File upload → agent extracts fields |
| Sun | 15 Nov | Must-have #2: Kane CLI verification flow | Kane CLI verifies extraction in real browser |
| Mon | 16 Nov | Must-have #3: closed loop (agent + Kane CLI talk) | Kane failure → agent retries → passes |
| Tue | 17 Nov | Must-have #4: deploy + smoke test | Live URL working; backup video recorded |
| Wed | 18 Nov | Polish + demo video + submission form | YouTube video edited; submission filled |
| Thu | 19 Nov | Submit before 11:59 PM IST | Submit early; servers may crash near deadline |

## Detailed Daily Schedule

### Friday 13 Nov — Day 1: Foundation
**Goal:** Repo created, hello world deployed, Kane CLI installed and wired to agent

- Morning: Register on TestMu AI, claim 10,000 credits; install Kane CLI (`npm install -g @testmuai/kane-cli`); run one flow to verify it works
- Morning (cont.): Append Kane CLI agent instructions (`curl -fsSL https://www.testmuai.com/kane-cli-agent/AGENTS.md >> AGENTS.md`); verify agent can run a Kane CLI objective
- Afternoon: Create public GitHub repo (initialized on or after 12 Nov); initialize Django project; create document upload page (HTMX)
- Evening: Deploy to Railway/Render (even if just a landing page); commit and push
- Night: Record 30-second "hello world" sanity check video

**Exit criteria:** Repo is public, Django app renders upload page, Kane CLI runs one flow successfully, AGENTS.md present in repo

### Saturday 14 Nov — Day 2: Must-Have #1
**Goal:** Document upload → agent extraction works end to end

- Morning: Wire up file upload (PDF/image, size/type limits); save to temp storage
- Afternoon: Connect Hermes agent to extract structured fields from uploaded document
- Evening: Display extracted fields on results page; test with 3-4 mock documents
- Night: Commit and push; run `npm audit`

**Exit criteria:** Upload a document, see extracted fields on screen, no crashes

### Sunday 15 Nov — Day 3: Must-Have #2
**Goal:** Kane CLI verifies extraction in a real browser

- Morning: Write Kane CLI test flow (plain English: "upload a document, verify extracted fields match")
- Afternoon: Run Kane CLI against the deployed/live URL; capture pass/fail output
- Evening: Integrate Kane CLI result into the UI (show pass/fail badge)
- Night: Record backup demo video (upload → extract → Kane verifies)

**Exit criteria:** Kane CLI caught or proved something meaningful about the extraction flow

### Monday 16 Nov — Day 4: Must-Have #3 (Closed Loop)
**Goal:** Kane CLI result feeds back to the agent

- Morning: On Kane CLI failure, agent re-reads the document and re-extracts
- Afternoon: Verify the retry loop converges (agent corrects, Kane passes)
- Evening: Test the full loop with intentionally "bad" documents to prove correction works
- Night: Commit and push; smoke test on deployed URL

**Exit criteria:** Agent and Kane CLI talk to each other; closed loop demonstrated

### Tuesday 17 Nov — Day 5: Must-Have #4 (Deploy + Smoke Test)
**Goal:** Live URL working; backup video ready

- Morning: Finalize deployment; test in incognito mode; verify credentials handover for judges
- Afternoon: Record final demo video (3-5 min, YouTube); edit and upload
- Evening: Write README (pitch, how to run, demo link, video link); fill submission form draft
- Night: Backup: save video locally in case YouTube upload fails

**Exit criteria:** Live URL works, YouTube video uploaded, submission form drafted

### Wednesday 18 Nov — Day 6: Polish + Submission Prep
**Goal:** Everything ready to submit

- Morning: Final `npm audit`; verify `.env` in `.gitignore`; remove any hardcoded secrets
- Afternoon: Launch buzz — post #1 (Hacker News, X, Reddit, or LinkedIn)
- Evening: Launch buzz — post #2 (different platform); final review of submission form
- Night: Early submission buffer (in case of issues)

**Exit criteria:** Two public posts made; submission form complete; video and repo verified

### Thursday 19 Nov — Day 7: Submit
**Goal:** Submit before 11:59 PM IST

- Morning/Afternoon: Final checks; submit via https://kaneclihack.sh/o/submit
- Evening: Submit early — do not wait until the deadline (servers may crash)
- Night: Celebrate

**Exit criteria:** Submission confirmed before deadline

## Submission Form Data (pre-filled)
- GitHub URL: TBD (repo to be created)
- About your app: Document-digitization intake agent with Kane CLI verification
- Agent used: Hermes Agent
- What Kane does: Verifies document upload → extraction flow in a real browser; feeds results back to agent for correction
- Demo video: YouTube link TBD
- Live URL: TBD (optional)
