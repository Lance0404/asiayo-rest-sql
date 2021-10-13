from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel, Field


class Property(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

class Room(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    property_id: int
    name: str

class Orders(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    room_id: int
    price: int
    create_at: datetime

# class SongBase(SQLModel):
#     name: str
#     artist: str
#     year: Optional[int] = None


# class Song(SongBase, table=True):
#     id: int = Field(default=None, primary_key=True)


# class SongCreate(SongBase):
#     pass
