<div align="center">
  <h1>⚡ Kane Intake</h1>
  <p><strong>Document-Digitization Intake Agent with Closed-Loop Kane CLI Verification</strong></p>
  <p>
    <a href="https://github.com/Josephjbassey/kane-cli-hackathon-2026"><img src="https://img.shields.io/badge/Verified%20with-Kane%20CLI-059669.svg" alt="Verified with Kane CLI"></a>
    <a href="https://pypi.org/project/djinn-ui/"><img src="https://img.shields.io/badge/UI-Djinn%20UI-1e293b.svg" alt="Djinn UI"></a>
    <a href="https://pypi.org/project/django/"><img src="https://img.shields.io/badge/Backend-Django%206.1-092e20.svg" alt="Django"></a>
    <a href="https://pypi.org/project/pip-audit/"><img src="https://img.shields.io/badge/Security-pip--audit%20Passed-10b981.svg" alt="pip-audit"></a>
  </p>
</div>

---

## 📌 Overview

**Kane Intake** is a document digitization and intake application that accepts invoices and receipts (PDFs/images), extracts structured financial data, and verifies the full workflow end-to-end using **Kane CLI** (`@testmuai/kane-cli`) in a real Chrome browser.

Built specifically for the **TestMu AI Kane CLI Hackathon 2026**.

### 🌟 Key Highlights
- **Clean Django Monolith:** Django 6 + HTMX + SQLite for zero-config simplicity.
- **Djinn UI Component Scaffolding:** Styled with **Djinn UI** (`djinn-ui` on PyPI) — the shadcn/ui equivalent for Django — delivering accessible, native Tailwind CSS components without heavy JS runtime bloat.
- **Design Taste Standards:** Follows anti-slop frontend engineering standards — strict typography (Geist & Geist Mono), calibrated Zinc neutrals, zero neon glows, and tabular numerics.
- **Concrete Kane CLI Verifications:** Ground-truth mock invoice fixtures checking deterministic outcomes like `"verify the total shows ₦12,500"`.
- **Hermes Coding Agent ⟷ Kane CLI Closed Loop:** Kane CLI tests the app in headless Chrome; when a regression or planted bug is caught, the coding agent reads the failure logs & screenshots, patches the service logic, and reruns until 100% verified.

---

## 🔁 The Closed-Loop Architecture

```
   ┌─────────────────────────────────────────────────────────┐
   │                                                         │
   ▼                                                         │
[App Code] ──► [Kane CLI Browser Assertion]                  │
(Django/HTMX)  "verify total shows ₦12,500"                  │
                       │                                     │
                       ├─► PASS (Exit 0) ──► Verified Badge  │
                       │                                     │
                       └─► FAIL (Exit 1)                     │
                               │                             │
                               ▼                             │
                     [Failure Evidence]                      │
                     (Screenshots + Logs)                    │
                               │                             │
                               ▼                             │
                     [Hermes Coding Agent]                   │
                     (Analyzes & Patches Code) ──────────────┘
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | Django 6.1, SQLite, Python 3.14 |
| **Frontend** | Django Templates, HTMX 2.0, Tailwind CSS |
| **UI Components** | **Djinn UI** (`djinn-ui` from PyPI) |
| **Verification** | Kane CLI (`@testmuai/kane-cli`), TestMu AI Cloud |
| **Security** | `pip-audit` vulnerability scanning (0 known issues) |

---

## 🚀 Quickstart

### 1. Clone & Set Up Virtual Environment
```bash
git clone https://github.com/Josephjbassey/kane-cli-hackathon-2026.git
cd kane-cli-hackathon-2026

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Configure Environment
```bash
cp .env.example .env
python manage.py migrate
```

### 3. Generate Mock Invoice Test Fixtures
```bash
python scripts/generate_mock_invoices.py
```

### 4. Run the Development Server
```bash
python manage.py runserver 0.0.0.0:8000
```
Open [http://localhost:8000](http://localhost:8000) in your browser.

---

## 🧪 Testing & Verification

### Run Django Unit Tests
```bash
python manage.py test
```

### Run Security Audit (`pip-audit`)
```bash
./scripts/run_audit.sh
```

### Run Kane CLI Browser Verification
```bash
./scripts/run_kane_verification.sh http://localhost:8000
```
Or run the objective directly with Kane CLI:
```bash
kane-cli run "Go to http://localhost:8000, click on Run Mock Invoice Flow (₦12,500), and verify the total shows ₦12,500" --agent --headless --timeout 120
```

### Run the Closed-Loop Agent Demonstration
```bash
python scripts/closed_loop_agent.py
```
This script plants an intentional bug, runs the assertion check to capture failure, applies the coding agent repair patch, and verifies that the Kane verification passes cleanly.

---

## 📄 License
MIT License. Created by [Joseph John](https://github.com/Josephjbassey).
