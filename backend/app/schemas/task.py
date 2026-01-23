from pydantic import BaseModel, Field
from datetime import datetime


class TaskBase(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    description: str | None = None


class TaskCreate(TaskBase):
    pass


class TaskResponse(TaskBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
