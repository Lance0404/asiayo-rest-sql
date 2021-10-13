from fastapi import Depends, FastAPI
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_session
from app.models import Property, PropertyCreate, Room, RoomCreate, Order, OrderCreate

app = FastAPI()


@app.get("/ping")
async def pong():
    return {"ping": "pong!"}

@app.get("/property")
async def get_property(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Property))
    properties = result.scalars().all()
    return [Property(**property.dict()) for property in properties]

@app.post("/property")
async def add_property(property: PropertyCreate, session: AsyncSession = Depends(get_session)):
    property = Property(name=property.name)
    session.add(property)
    await session.commit()
    await session.refresh(property)
    return property

@app.get("/room")
async def get_room(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Room))
    rooms = result.scalars().all()
    return [Room(**room.dict()) for room in rooms]

@app.post("/room")
async def add_room(room: RoomCreate, session: AsyncSession = Depends(get_session)):
    room = Room(**room.dict())
    session.add(room)
    await session.commit()
    await session.refresh(room)
    return room

@app.get("/order")
async def get_order(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Order))
    orders = result.scalars().all()
    return [Order(**order.dict()) for order in orders]

@app.post("/order")
async def add_order(order: OrderCreate, session: AsyncSession = Depends(get_session)):
    order = Order(**order.dict())
    session.add(order)
    await session.commit()
    await session.refresh(order)
    return order


