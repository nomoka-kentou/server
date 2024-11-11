from typing import Optional

from pydantic import BaseModel, Field, ConfigDict


class UserCreate(BaseModel):
    username: str = Field(max_length=30)
    name: str = Field(max_length=60)


class UserUpdate(BaseModel):
    name: str


class UserResponse(BaseModel):
    id: int
    username: str
    name: str
    created_at: datetime.datetime | None = None
    updated_at: datetime.datetime | None = None

    model_config = ConfigDict(from_attributes=True)
