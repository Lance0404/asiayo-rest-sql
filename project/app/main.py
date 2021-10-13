from datetime import datetime
from dateutil.relativedelta import relativedelta
from fastapi import Depends, FastAPI
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import func
from typing import List

from sqlalchemy.orm import selectinload

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


@app.get("/property/{year}/{month}/{top}/")
async def get_top_property(year: int = 2021, month: int = 10, top: int = 10, session: AsyncSession = Depends(get_session)):
    ym = datetime.strptime(f"{year}-{month}", "%Y-%m")
    ym_max = ym + relativedelta(months=1)
    count = func.count(Property.id)
    # stmt = (
    #     session.query(Property, count)
    #     # .select_from(Room, Order)
    #     .join(Room.property)
    #     # .select_from(Order)
    #     # .join(Order.room)
    #     # .filter(Order.create_at >= ym)
    #     # .filter(Order.create_at < ym_max)
    #     .group_by(Property.name)
    #     # .order_by(count.desc())
    #     # .limit(top)
    # )
    # results = stmt.all()
    # print(f'results {results}')


    stmt = (
        select(Order, Room, Property)
        # .select_from(Order)
        # .select_from(Order, Room, Property)
        .options(selectinload(Order.room))
        .options(selectinload(Room.property))
        # .join_from(Order, Room, Order.room_id == Room.id)
        .join(Room, Order.room_id == Room.id)
        .join(Property, Room.property_id == Property.id)
        .filter(Order.create_at >= ym)
        .filter(Order.create_at < ym_max)
        .group_by(Property.name)
    ) 
    """"
    raw SQL confirmed in pgAdmin:

    * spread out version
SELECT "order".price, "order".create_at, "order".room_id, "order".id, "room".name, property.name
FROM "order" 
JOIN room ON "order".room_id = room.id 
JOIN property ON room.property_id = property.id
WHERE create_at >= '2021-10-01'::date
AND create_at < ('2021-10-01'::date + '1 month'::interval)

    * aggregated version
SELECT property.name, count(*) as counts
FROM "order" 
JOIN room ON "order".room_id = room.id 
JOIN property ON room.property_id = property.id
WHERE create_at >= '2021-10-01'::date
AND create_at < ('2021-10-01'::date + '1 month'::interval)
GROUP BY property.name
ORDER BY counts
LIMIT 10
    """
    # session.
    result = await session.execute(stmt)
    orders: List[Order] = result.scalars().all()
    # print(orders)
    # print(type(orders))
    # [Order(room_id=1, create_at=datetime.datetime(2021, 10, 13, 10, 36, 9, 3180), price=600, id=2), Order(room_id=2, create_at=datetime.datetime(2021, 10, 13, 10, 50, 41, 779089), price=200, id=3)]

    # for order in orders:
    #     print(type(order.room))
    #     print(order.room)
    return None
    # return [order.room.name for order in orders]
