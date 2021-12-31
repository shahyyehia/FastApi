import uvicorn
from fastapi import FastAPI
from restaurantR import restaurant
from usersR import user

app=FastAPI()
app.include_router(restaurant)
app.include_router(user)

if __name__ == "__main__":
    uvicorn.run(app)

