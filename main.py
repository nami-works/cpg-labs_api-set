#!/usr/bin/env python3
"""
CPG Labs APIs - Main FastAPI Application
SEO Lab API for AI-powered content generation
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import uvicorn
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("🚀 CPG Labs APIs starting up...")
    print("📝 SEO Lab API ready for content generation")
    yield
    # Shutdown
    print("🛑 CPG Labs APIs shutting down...")

# Create main FastAPI app
app = FastAPI(
    title="CPG Labs APIs",
    description="AI-powered APIs for content generation using CrewAI",
    version="1.0.0",
    lifespan=lifespan
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure properly for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Import and include SEO Lab API
from apis.seo_lab.api_service import app as seo_app
app.mount("/api/seo", seo_app)

@app.get("/")
async def root():
    return {
        "message": "CPG Labs APIs",
        "version": "1.0.0",
        "status": "healthy",
        "description": "AI-powered APIs for content generation",
        "apis": {
            "seo": "/api/seo",
            "docs": "/docs",
            "health": "/health"
        }
    }

@app.get("/health")
async def health_check():
    return {
        "status": "healthy", 
        "timestamp": "2024-01-01T00:00:00Z",
        "services": {
            "seo_lab": "available"
        }
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
