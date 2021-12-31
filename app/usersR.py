from fastapi import APIRouter
from db import conn
from usersM import users
from usersS import Users

user = APIRouter()


@user.get("/users/")
async def read_users_data():
    return conn.execute(users.select()).fetchall()

@user.get("/users/{email}")
async def read_users_data_byemail(email: str):
    return conn.execute(users.select().where(users.c.email == email)).fetchall()

@user.post("/users/")
async def add_users_data(user : Users):
    conn.execute(users.insert().values(
        name=user.name,
        password=user.password,
        email=user.email))
    return conn.execute(users.select()).fetchall()



@user.put("/users/{id}")
async def update_users_data(id:int,user:Users):
    conn.execute(users.update().values(
        name=user.name,
        password=user.password,
        email=user.email,
                                             ).where(users.c.id==id,
                                                     ))
    return conn.execute(users.select()).fetchall()

@user.delete("/users/{id}")
async def delete_users_data(id:int):
    conn.execute(users.delete().where(users.c.id==id))
    return conn.execute(users.select()).fetchall()