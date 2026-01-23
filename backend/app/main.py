from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import tasks

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # luego se restringe
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tasks.router)


@app.get("/")
def root():
    return {"status": "API running"}
