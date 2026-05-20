"""Health check endpoints"""

from fastapi import APIRouter, HTTPException
from datetime import datetime

router = APIRouter()


@router.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "service": "Cyber Threat Detection API"
    }


@router.get("/ready")
async def readiness_check():
    """Readiness check endpoint"""
    # TODO: Add actual readiness checks (DB, Redis, Kafka)
    return {
        "ready": True,
        "timestamp": datetime.utcnow().isoformat()
    }
