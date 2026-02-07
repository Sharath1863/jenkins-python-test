from fastapi import FastAPI
import os

app = FastAPI(title="CI/CD Demo App")

@app.get("/")
def root():
    return {
        "message": "FastAPI app is running",
        "status": "ok"
    }

@app.get("/health")
def health():
    return {
        "status": "UP"
    }

@app.get("/version")
def version():
    return {
        "build": os.getenv("APP_VERSION", "local"),
        "env": os.getenv("ENV", "dev")
    }
