# Launch Buzz Drafts — Kane CLI Hackathon 2026

## Post #1 (X / Twitter) — The Announcement & Architecture
**Target:** X / Twitter (Thread / Single Post)
**Status:** Ready for queue

> 🚀 Excited to ship for the **Kane CLI Hackathon** by @TestMuAI!
> 
> We built an autonomous Document Digitization Intake Agent powered by Django, HTMX, and @shadcn-style @djinn_ui components.
> 
> But here's the game-changer: We closed the loop between our coding agent (Hermes) and @kane_cli. 
> 
> When Kane runs browser-level quality assertions (e.g. verifying invoice line-items & totals like ₦12,500 in real Chrome) and catches an extraction bug, Hermes inspects the failure evidence, patches the code, and reruns until verified.
> 
> 🔗 Repo: https://github.com/Josephjbassey/kane-intake
> #KaneCLIHack #AIAgents #Django #WebDev #BuildInPublic

---

## Post #2 (LinkedIn / Hacker News / Reddit) — The Deep Dive & Closed Loop
**Target:** LinkedIn / Reddit (r/django, r/Python, r/artificial)
**Status:** Ready for queue

> **Closing the Loop: How we wired an AI coding agent directly to Kane CLI for autonomous QA in Django**
> 
> Most hackathon projects showcase an AI agent building an app, or an agent doing OCR. But during the **TestMu AI Kane CLI Hackathon**, we took verification a step further:
> 
> We paired our coding agent directly with **Kane CLI** in a continuous self-healing loop:
> 
> 1️⃣ **Intake:** User uploads invoices/receipts (or runs mock fixtures) into a clean Django + HTMX monolith styled with Djinn UI components.
> 2️⃣ **Real Browser Verification:** Kane CLI spins up headless Chrome and tests concrete assertions: *"Verify the extracted total matches ₦12,500.00 and line items reconcile."*
> 3️⃣ **Autonomous Self-Correction:** When an edge-case bug is caught (e.g. currency symbol stripping or date misparsing), Kane logs the failure and screenshot. Our coding agent inspects the failure artifact, patches the Django service, and re-triggers Kane until 100% pass (exit code 0).
> 
> No mock tests. No slides. Real end-to-end browser verification.
> 
> 📦 Check out the open-source repo: https://github.com/Josephjbassey/kane-intake
> 
> #KaneCLI #TestMuAI #Python #SoftwareTesting #DevOps #AutonomousAgents
