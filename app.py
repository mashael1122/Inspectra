from fastapi import FastAPI

app = FastAPI(
    title="Inspectra API",
    description="Lightweight service artifact for the Inspectra capstone project.",
    version="1.0.0",
)

@app.get("/")
def root():
    return {
        "project": "Inspectra",
        "status": "ready",
        "message": "Run Inspectra.ipynb in Google Colab for the full multi-agent audit workflow."
    }

@app.get("/health")
def health():
    return {"status": "ok"}
