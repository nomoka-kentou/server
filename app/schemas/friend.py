from typing import Optional

from pydantic import BaseModel, Field, ConfigDict


class FriendCreate(BaseModel):
    name: str = Field(max_length=60)


class FriendUpdate(BaseModel):
    name: str


class FriendResponse(BaseModel):
    id: int
