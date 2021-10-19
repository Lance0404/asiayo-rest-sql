from enum import Enum
from datetime import datetime
from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel

class CurrenyType(str, Enum):
    TWD = "TWD"
    JPY = "JPY"
    USD = "USD"

class CurrencyFrom(SQLModel):
    from_currency: CurrenyType
    from_amount: float = 1
    to_currency: CurrenyType
    # to_amount: str


class PropertyBase(SQLModel):
    name: str

class Property(PropertyBase, table=True):
    __tablename__ = 'property'
    id: Optional[int] = Field(default=None, primary_key=True)    
    rooms: List["Room"] = Relationship(back_populates="property")

class PropertyCreate(PropertyBase):
    pass

class PropertyInfo(PropertyBase):
    order_count: Optional[int]

class Properties(SQLModel):
    properties: List[PropertyInfo]


# class DateInfo(SQLModel):
#     pass
#     year: 
class RoomBase(SQLModel):
    name: str
    property_id: int = Field(default=None, foreign_key="property.id")

class Room(RoomBase, table=True):
    __tablename__ = 'room'
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
    # TODO: inconsistency btw the table name and class name is bad, but order is a keyword in SQL
    __tablename__ = 'orders'
    id: Optional[int] = Field(default=None, primary_key=True)
    room: Optional[Room] = Relationship(back_populates="orders")

class OrderCreate(OrderBase):
    pass
