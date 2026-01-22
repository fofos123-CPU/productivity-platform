from fastapi import FastAPI
from app.routers.health import router as health_router
from app.core.config import settings
from app.core.database import engine, Base

app = FastAPI(title=settings.app_name)

Base.metadata.create_all(bind=engine)

app.include_router(health_router)
