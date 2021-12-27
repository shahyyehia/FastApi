from fastapi import APIRouter
from config.db import conn
from models.restaurant import restaurants
from schema.restaurant import Restaurant

restaurant = APIRouter()


@restaurant.get("/restaurant/")
async def read_restaurant_data():
    return conn.execute(restaurants.select()).fetchall()


@restaurant.get("/restaurant/{type}")
async def get_restaurant_data(type: str):
    return conn.execute(restaurants.select().where(restaurants.c.type == type)).fetchall()


@restaurant.get("/restaurant/{location}")
async def get_restaurant_data(location: str):
    return conn.execute(restaurants.select().where(restaurants.c.location == location)).fetchall()


@restaurant.get("/restaurant/{location,type}")
async def get_restaurant_data(location: str, type:str):
    return conn.execute(restaurants.select().where(restaurants.c.location == location and restaurants.c.type == type)).fetchall()


@restaurant.post("/restaurant/")
async def add_restaurant_data(restaurant : Restaurant):
    conn.execute(restaurants.insert().values(
        name=restaurant.name,
        type=restaurant.type,
        location=restaurant.location
                                             ))
    return conn.execute(restaurants.select()).fetchall()



@restaurant.put("/restaurant/{id}")
async def update_restaurant_data(id:int,restaurant:Restaurant):
    conn.execute(restaurants.update().values(
        name=restaurant.name,
        type=restaurant.type,
        location=restaurant.location
                                             ).where(restaurants.c.id==id,
                                                     ))
    return conn.execute(restaurants.select()).fetchall()

