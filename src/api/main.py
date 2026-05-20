"""Main FastAPI application for Cyber Threat Detection System"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import logging

from src.api.routes import threats, response, explainability, health
from src.core.config import settings
from src.core.database import init_db

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifecycle management"""
    # Startup
    logger.info("Starting Cyber Threat Detection API")
    await init_db()
    yield
    # Shutdown
    logger.info("Shutting down Cyber Threat Detection API")


# Create FastAPI app
app = FastAPI(
    title="Cyber Threat Detection API",
    description="AI-Driven Autonomous Cyber Threat Detection and Response System",
    version="0.1.0",
    lifespan=lifespan
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.api.cors.origins,
    allow_credentials=settings.api.cors.allow_credentials,
    allow_methods=settings.api.cors.allow_methods,
    allow_headers=settings.api.cors.allow_headers,
)

# Include routers
app.include_router(health.router, tags=["Health"])
app.include_router(threats.router, prefix="/api/v1/threats", tags=["Threats"])
app.include_router(response.router, prefix="/api/v1/response", tags=["Response"])
app.include_router(explainability.router, prefix="/api/v1/explain", tags=["Explainability"])


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Welcome to Cyber Threat Detection System",
        "version": "0.1.0",
        "docs": "/docs"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
