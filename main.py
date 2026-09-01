from fastapi import FastAPI

app = FastAPI(
    title="HireLens API",
    description="Backend for resume analysis and job recommendations",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to HireLens"
    }


@app.get("/health")
def health():
    return {
        "status": "success",
        "message": "HireLens backend is running"
    }
