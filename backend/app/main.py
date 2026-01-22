from fastapi import FastAPI

# Database
from app.core.database import Base, engine

# Models (important: import so tables are registered)
from app.models import task

# Routers
from app.routers import tasks

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Productivity Platform API",
    description="Backend API for a multi-language productivity platform",
    version="0.1.0",
)

# Include routers
app.include_router(tasks.router)


@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}
