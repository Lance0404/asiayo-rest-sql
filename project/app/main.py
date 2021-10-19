from datetime import datetime
from dateutil.relativedelta import relativedelta
from fastapi import Depends, FastAPI
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from sqlalchemy.sql.expression import bindparam
from sqlalchemy import func
from typing import List

from sqlalchemy.orm import selectinload
from sqlalchemy.sql.sqltypes import DateTime, Integer

from app.db import get_session
from app.models import CurrencyFrom, Property, PropertyCreate, PropertyInfo, Room, RoomCreate, Order, OrderCreate

app = FastAPI()


@app.get("/ping")
async def pong():
    return {"ping": "pong!"}

currencies = {
    "TWD": {
        "TWD": 1,
        "JPY": 3.669,
        "USD": 0.03281
    },
    "JPY": {
        "TWD": 0.26956,
        "JPY": 1,
        "USD": 0.00885
    },
    "USD": {
        "TWD": 30.444,
        "JPY": 111.801,
        "USD": 1
    }
}

@app.post("/currency")
async def convert_currency(cf: CurrencyFrom) -> str:
    # REF: https://pythonguides.com/python-format-number-with-commas/
    to_amount: float = cf.from_amount * currencies[cf.from_currency][cf.to_currency]
    formated_to_amount = '{:,.2f}'.format(to_amount)
    print(f'origin    {cf.from_amount}')
    print(f'converted {to_amount}')    
    print(f'formated  {formated_to_amount}')
# origin    914.314
# converted 29.998642339999996
# formated  30.00    
    return formated_to_amount

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

def do_group_by(session: Session, dt_min: datetime, dt_max: datetime, limit: int):
    c = func.count(Property.id)
    q = (
        session.query(Property.name, c)
        .filter(Order.room_id == Room.id)
        .filter(Room.property_id == Property.id)        
        .filter(Order.create_at >= dt_min)
        .filter(Order.create_at < dt_max)
        .group_by(Property.name)
        .order_by(c)
        .limit(limit)
    )
    print(q)
    ret = q.all()
    print(f'ret {ret}')
    return [PropertyInfo(name=i[0], order_count=i[1]) for i in ret]

@app.get("/property/{year}/{month}/{top}/")
async def get_top_property(year: int = 2021, month: int = 10, top: int = 10, session: AsyncSession = Depends(get_session)):
    """
    https://docs.sqlalchemy.org/en/14/orm/extensions/asyncio.html#running-synchronous-methods-and-functions-under-asyncio
    """
    ym = datetime.strptime(f"{year}-{month}", "%Y-%m")
    ym_max = ym + relativedelta(months=1)
    return await session.run_sync(do_group_by, ym, ym_max, top)

@app.get("/property_test/{year}/{month}/{top}/")
async def get_top_property_test(year: int = 2021, month: int = 10, top: int = 10, session: AsyncSession = Depends(get_session)):
    """
    https://docs.sqlalchemy.org/en/14/core/tutorial.html#using-textual-sql
    """
    ym = datetime.strptime(f"{year}-{month}", "%Y-%m")
    ym_max = ym + relativedelta(months=1)
    s = text(
        "select property.name, count(property.id) as c "
        "FROM orders, room, property "
        "WHERE orders.room_id = room.id "
        "AND room.property_id = property.id "
        "AND orders.create_at >= :min "
        "AND orders.create_at < :max "
        "GROUP BY property.name "
        "ORDER BY c DESC "
        "LIMIT :top"
    )
    s = s.bindparams(
        bindparam("min", type_=DateTime),
        bindparam("max", type_=DateTime),
        bindparam("top", type_=Integer)
    )
    params = {
        "min": ym,
        "max": ym_max,
        "top": top
    }
    result = await session.execute(s, params)
    ret = result.all()
    return [PropertyInfo(name=i[0], order_count=i[1]) for i in ret]