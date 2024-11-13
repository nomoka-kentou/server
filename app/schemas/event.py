from typing import Optional

from pydantic import BaseModel, Field, ConfigDict


class EventCreate(BaseModel):
    title: str = Field(max_length=30)


class EventUpdate(BaseModel):
    title: str


class EventResponse(BaseModel):
    id: int
    title: str
    created_at: datetime.datetime | None = None
    updated_at: datetime.datetime | None = None

    model_config = ConfigDict(from_attributes=True)
