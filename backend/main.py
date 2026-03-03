from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import jobs, analytics, auth
import uvicorn

app = FastAPI(
    title="ContentStudio API",
    description="AI Content Repurposing Studio Backend",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(jobs.router, prefix="/api/jobs", tags=["jobs"])
app.include_router(analytics.router, prefix="/api/analytics", tags=["analytics"])

@app.get("/api/health")
def health():
    return {"status": "ok", "service": "ContentStudio API"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
