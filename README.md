# Inspectra

**Inspectra** is an autonomous multi-agent system that audits public websites and web applications for **UX quality and accessibility issues**.

The project was built as a capstone for **Advanced Agentic AI Systems Engineering — SDAIA Academy**.

SDAIA Academy on GitHub: https://github.com/SDAIAAcademy

---

## What Inspectra does

A user provides a public URL. Inspectra then:

1. Validates the target URL and applies security guardrails.
2. Uses a **Planner Agent** to create a bounded audit plan.
3. Uses a **Browser Agent** with Playwright to explore the application.
4. Collects screenshots, DOM evidence, and axe-core accessibility results.
5. Uses a **UX Reviewer Agent** to evaluate usability.
6. Uses an **Accessibility Agent** to evaluate accessibility findings.
7. Merges and prioritizes issues.
8. Uses a **Report Writer Agent** to prepare the audit report.
9. Pauses at a real **Human-in-the-Loop** approval step.
10. Approves, rejects, or re-crawls before export.

## Reasoning pattern

Inspectra uses **Plan-and-Execute**:

- The Planner Agent creates the inspection plan.
- The Browser Agent executes it with real browser/accessibility tools.
- Specialized reviewer agents analyze evidence.
- The graph can retry or re-crawl based on state and human input.

## Architecture

```text
Planner
  ↓
Browser
  ├── retry ───────┐
  └── continue     │
        ↓          │
    UX Reviewer    │
        ↓          │
Accessibility      │
        ↓          │
Merge Findings     │
        ↓          │
Report Generation  │
        ↓          │
Human Approval     │
   ├── approve → Export
   ├── reject  → Rejected
   └── recrawl ───→ Browser
```

Detailed architecture: [`docs/architecture.md`](docs/architecture.md)

## Main technologies

- Python
- Google Colab
- LangGraph
- LangChain
- OpenRouter
- Playwright
- axe-core
- BeautifulSoup
- SQLite checkpointer
- Gradio
- ReportLab
- FastAPI
- Docker

## Repository structure

```text
Inspectra/
├── Inspectra.ipynb
├── README.md
├── requirements.txt
├── .gitignore
├── app.py
├── Dockerfile
└── docs/
    └── architecture.md
```

# How to run the full project

## Recommended environment: Google Colab

Open `Inspectra.ipynb` in Google Colab and run the cells from top to bottom.

### 1. Add the OpenRouter API key

This repository does **not** include API keys.

In Google Colab:

1. Open **Secrets** from the key icon in the left sidebar.
2. Add a secret named:

```text
OPENROUTER_API_KEY
```

3. Paste your own OpenRouter API key.
4. Enable notebook access to the secret.

### 2. Run the notebook

Use:

**Runtime → Run all**

The setup cells install the required Python/browser packages.

### 3. Launch the Gradio interface

After the notebook finishes setup, launch the Gradio UI.

Enter a public website URL and start an audit.

### 4. Complete the Human-in-the-Loop step

The workflow supports:

- Approve
- Reject
- Re-crawl

Approval resumes the persisted LangGraph workflow and allows export.

## Expected outputs

A completed audit can include:

- visited-page evidence
- screenshots
- DOM summaries
- accessibility findings
- UX findings
- merged/prioritized findings
- execution logs
- final report artifacts

Generated runtime files are excluded from Git through `.gitignore`.

# Capstone rubric mapping

| Rubric area | Inspectra evidence |
|---|---|
| Agentic Reasoning & Tool Use | Plan-and-Execute pattern, Planner Agent, Browser Agent, Playwright and axe-core tool use |
| Graph-Based Orchestration | LangGraph `StateGraph`, shared state, nodes, edges, conditional routing, retry/re-crawl loops |
| Multi-Agent System | Planner, Browser, UX Reviewer, Accessibility, and Report Writer agents |
| Security & Guardrails | URL guardrails, prompt-injection detection, PII masking, same-origin bounded crawling |
| Observability | Structured logging and execution information in the notebook/runtime |
| Persistence | SQLite-based LangGraph checkpointer |
| Human-in-the-Loop | Graph pauses before approval and resumes after approve/reject/re-crawl input |
| Cloud artifact | `app.py` FastAPI artifact + `Dockerfile` |
| Documentation | README + architecture documentation + executed notebook evidence |

# FastAPI / Docker artifact

The repository includes a lightweight FastAPI artifact to demonstrate a production/cloud service boundary.

Run locally:

```bash
pip install fastapi uvicorn
uvicorn app:app --reload
```

Then open:

```text
http://127.0.0.1:8000/health
```

With Docker:

```bash
docker build -t inspectra .
docker run -p 8000:8000 inspectra
```

# Security

Do not commit:

- API keys
- `.env` secrets
- private credentials
- generated logs containing sensitive data

The `.gitignore` included in this repository excludes common secret/runtime files.

# Notes for evaluator

The **main capstone implementation is `Inspectra.ipynb`**.

For the most reproducible evaluation:

1. Open the notebook in Google Colab.
2. Add `OPENROUTER_API_KEY` to Colab Secrets.
3. Run all cells.
4. Launch the Gradio interface.
5. Audit a public URL.
6. Review the generated findings.
7. Exercise the Human-in-the-Loop approve/reject/re-crawl flow.

The notebook should be kept with its executed outputs before final submission so the evaluation evidence is visible directly in GitHub/Colab.
