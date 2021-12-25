from fastapi import FastAPI
from routes.restaurant import restaurant
from routes.users import user

app=FastAPI()
app.include_router(restaurant)
app.include_router(user)