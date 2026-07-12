from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, field_validator


class TodoBase(BaseModel):
    title: str = Field(..., min_length=1)

    @field_validator("title")
    @classmethod
    def validate_title(cls, value: str) -> str:
        if not value or not value.strip():
            raise ValueError("title must not be empty")
        return value.strip()


class TodoCreate(TodoBase):
    pass


class TodoUpdate(BaseModel):
    completed: Optional[bool] = None


class TodoRead(TodoBase):
    id: int
    completed: bool
    created_at: datetime
    updated_at: datetime
