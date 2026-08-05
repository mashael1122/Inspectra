# Inspectra Architecture

## Overview

Inspectra is a multi-agent UX and accessibility auditing system orchestrated with LangGraph.

## Reasoning pattern

**Plan-and-Execute**

1. The Planner Agent decides what should be inspected.
2. The Browser Agent executes the plan using browser/accessibility tools.
3. Specialized reviewer agents analyze the collected evidence.
4. Findings are merged and converted into a report.
5. A Human-in-the-Loop approval step decides whether to approve, reject, or re-crawl.

## Agents

- **Planner Agent** — creates the bounded audit plan.
- **Browser Agent** — explores the target site and collects evidence.
- **UX Reviewer Agent** — evaluates usability and interaction quality.
- **Accessibility Agent** — reviews accessibility evidence and violations.
- **Report Writer Agent** — converts findings into a professional audit report.

## Shared state

The LangGraph workflow uses a shared state object that carries data between nodes, including URL information, visited pages, screenshots, DOM summaries, accessibility results, findings, retry data, reports, and approval state.

## Main nodes

```text
Planner
  ↓
Browser
  ├── retry ───────┐
  │                │
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

## Tools and integrations

- Playwright for browser automation
- axe-core for automated accessibility checks
- LangChain/OpenRouter for structured LLM calls
- SQLite checkpointer for persistence
- Gradio for the interactive interface
- ReportLab for report export

## Guardrails

Inspectra includes input/data protection controls such as:

- URL validation
- Blocking unsafe localhost/private targets
- Prompt-injection detection
- PII masking
- Same-origin bounded crawling
- Structured output validation

## Persistence and HITL

The graph is compiled with a SQLite-based checkpointer so workflow state can persist. Human approval is implemented as a real graph pause/resume step with approve, reject, and re-crawl outcomes.

## Cloud / production artifact

The repository includes:

- `app.py` — FastAPI service artifact
- `Dockerfile` — container artifact

The full agentic workflow remains notebook-first for reproducibility in Google Colab.
