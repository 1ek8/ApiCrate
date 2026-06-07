from fastapi import FastAPI
from app.routes.projects import router as projects_router

app = FastAPI(title="ApiCrate", version="0.1.0")
app.include_router(projects_router)


@app.get("/")
def root():
    return {"status": "ok", "service": "ApiCrate"}