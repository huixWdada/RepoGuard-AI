
from fastapi import FastAPI, HTTPException

from app.config.database import check_database
from app.config.redis import check_redis

app = FastAPI(
    title="RepoGuard AI",
    description="Evidence-driven Multi-Agent Repository Governance System",
    version="0.1.0",
)


@app.get("/")
async def root():
    return {
        "project": "RepoGuard AI",
        "version": "0.1.0",
        "status": "running",
    }


@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "repoguard-backend",
    }


@app.get("/health/db")
async def database_health():
    try:
        check_database()
        return {"database": "connected"}
    except Exception as exc:
        raise HTTPException(
            status_code=503,
            detail="Database connection failed",
        ) from exc


@app.get("/health/redis")
async def redis_health():
    try:
        check_redis()
        return {"redis": "connected"}
    except Exception as exc:
        raise HTTPException(
            status_code=503,
            detail="Redis connection failed",
        ) from exc
