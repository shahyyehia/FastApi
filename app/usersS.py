from pydantic import BaseModel


class Users(BaseModel):
    name: str
    password: str
    email: str
