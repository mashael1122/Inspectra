# 🔍 Inspectra

**Inspectra** is an AI-powered **Multi-Agent UX & Accessibility Auditing System** designed to autonomously inspect public websites and web applications, identify usability and accessibility issues, and generate structured professional audit reports.

The project was developed as part of the **Advanced Agentic AI Engineering** course, presented by **SDAIA Academy** in collaboration with **Daico Academy**.

---

## 👥 Team Members

* **Norah Almansour**
* **Mashael Alshathri**
* **Ayidah Alswayed**

---

## 🎓 Training Program

**Course:** Advanced Agentic AI Engineering
**Presented by:** SDAIA Academy
**In collaboration with:** Daiko Academy

SDAIA Academy GitHub: https://github.com/SDAIAAcademy

---

## 💡 About Inspectra

Inspectra automates the process of reviewing websites and web applications from both **User Experience (UX)** and **Accessibility** perspectives.

The user provides a public application URL, and Inspectra uses a coordinated multi-agent workflow to explore the website, collect evidence, analyze UX and accessibility issues, prioritize findings, and generate a professional audit report.

The system demonstrates advanced Agentic AI engineering concepts including:

* Multi-Agent Systems
* LangGraph orchestration
* Plan-and-Execute reasoning
* Real browser tool usage
* Shared state and conditional routing
* Security guardrails
* Observability and logging
* Persistent state
* Human-in-the-Loop (HITL)
* Report generation

---

## 🤖 Multi-Agent Architecture

Inspectra consists of specialized AI agents, each with a distinct responsibility:

### 🧠 Planner Agent

Analyzes the target application and creates a bounded plan for the audit process.

### 🌐 Browser Agent

Uses **Playwright** to explore the target website, inspect pages, capture screenshots, collect DOM evidence, and execute accessibility checks.

### 🎨 UX Reviewer Agent

Analyzes the collected evidence and evaluates:

* Navigation
* Layout
* Visual hierarchy
* Consistency
* Forms
* Responsiveness
* Feedback
* Error handling
* Overall user flow

### ♿ Accessibility Agent

Analyzes accessibility evidence collected using **axe-core** and identifies potential accessibility violations.

### 📝 Report Writer Agent

Combines and prioritizes the findings and generates a structured UX & Accessibility audit report.

---

## 🔄 Workflow

```text
User URL
   ↓
Planner Agent
   ↓
Browser Agent
   ↓
UX Reviewer Agent
   ↓
Accessibility Agent
   ↓
Merge Findings
   ↓
Report Writer Agent
   ↓
Human-in-the-Loop
 ┌───────┼────────┐
Approve Reject  Re-crawl
   ↓              ↓
 Export         Browser
```

The workflow is implemented using **LangGraph StateGraph** with shared state, conditional edges, retry logic, and workflow loops.

---

## 🧠 Reasoning Pattern

Inspectra implements the **Plan-and-Execute** reasoning pattern.

The **Planner Agent** determines what should be inspected, while the **Browser Agent** executes the plan using real browser and accessibility tools.

The collected evidence is then passed through specialized reviewer agents before the final report is generated.

---

## 🛠️ Technologies

* Python
* Google Colab
* LangGraph
* LangChain
* OpenRouter
* Playwright
* axe-core
* BeautifulSoup
* SQLite
* Gradio
* ReportLab
* FastAPI
* Docker

---

## 🛡️ Security & Guardrails

Inspectra includes several security and data-protection mechanisms:

* URL validation
* Blocking unsafe local/internal targets
* Prompt-injection detection
* PII masking
* Same-origin bounded crawling
* Structured output validation
* Browser timeout and retry controls

---

## 💾 Persistence

Inspectra uses a **SQLite-based LangGraph checkpointer** to persist workflow state.

This allows the application to preserve the state of long-running audits and resume execution when required.

---

## 👤 Human-in-the-Loop

Before the final report is exported, Inspectra pauses the LangGraph workflow for human review.

The reviewer can choose to:

* ✅ Approve
* ❌ Reject
* 🔁 Re-crawl

The graph then resumes execution based on the selected decision.

---

# 🚀 How to Run Inspectra

The recommended environment is **Google Colab**.

### 1. Open the Notebook

Open:

```text
Inspectra.ipynb
```

in Google Colab.

### 2. Configure OpenRouter

Inspectra does **not** store API keys in the GitHub repository.

In Google Colab:

1. Open the **Secrets** panel.
2. Create a secret named:

```text
OPENROUTER_API_KEY
```

3. Add your OpenRouter API key.
4. Enable notebook access to the secret.

### 3. Run the Project

From the Google Colab menu select:

```text
Runtime → Run all
```

The notebook installs the required dependencies and browser components.

### 4. Launch Inspectra

After setup is complete, launch the **Gradio interface**.

Enter a public website or web application URL and start the audit.

### 5. Review the Results

Inspectra will automatically:

```text
Plan
→ Browse
→ Collect Evidence
→ Review UX
→ Review Accessibility
→ Merge Findings
→ Generate Report
→ Request Human Approval
```

Approve the audit to generate the final report.

---

## 📊 Expected Output

Inspectra can generate:

* Visited page evidence
* Website screenshots
* DOM summaries
* Accessibility findings
* UX findings
* Prioritized issues
* Execution logs
* Structured audit report
* PDF report

---

## 📁 Repository Structure

```text
Inspectra/
│
├── Inspectra.ipynb
├── README.md
├── requirements.txt
├── .gitignore
├── app.py
├── Dockerfile
│
└── docs/
    └── architecture.md
```

---

## ☁️ Production / Cloud Artifact

The repository includes a lightweight **FastAPI service** and **Dockerfile** as production-readiness artifacts.

The complete multi-agent implementation remains available inside `Inspectra.ipynb` for easy and reproducible evaluation using Google Colab.

---

## 📚 Capstone Concepts Demonstrated

Inspectra demonstrates key concepts covered in **Advanced Agentic AI Engineering**, including:

* Agentic reasoning
* Real tool usage
* Graph-based orchestration
* Multi-agent collaboration
* Agent role specialization
* Shared state
* Conditional routing
* Retry loops
* Security guardrails
* Observability
* Persistent checkpoints
* Human-in-the-Loop workflows
* Production-readiness concepts

---

## 👩‍💻 Developed By

**Norah Almansour**
**Mashael Alshathri**
**Ayidah Alswayed**

Developed as part of the **Advanced Agentic AI Engineering** course presented by **SDAIA Academy in collaboration with Daico Academy**.
