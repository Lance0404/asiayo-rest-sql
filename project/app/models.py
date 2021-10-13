from datetime import datetime
from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel


class PropertyBase(SQLModel):
    name: str
class Property(PropertyBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)    
    rooms: List["Room"] = Relationship(back_populates="property")

class PropertyCreate(PropertyBase):
    pass


class RoomBase(SQLModel):
    name: str
    property_id: int = Field(default=None, foreign_key="property.id")

class Room(RoomBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    property: Optional[Property] = Relationship(back_populates="rooms")
    orders: List["Order"] = Relationship(back_populates="room")

class RoomCreate(RoomBase):
    pass

class OrderBase(SQLModel):
    price: int
    create_at: Optional[datetime] = Field(default=datetime.now())
    room_id: int = Field(default=None, foreign_key="room.id")

class Order(OrderBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    room: Optional[Room] = Relationship(back_populates="orders")

class OrderCreate(OrderBase):
    pass