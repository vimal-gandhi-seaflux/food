
from sqlite3 import Timestamp
from pydantic import BaseModel

class register(BaseModel):
    name:str
    email:str
    password:str
    createdAt=Timestamp
    class config():
        orm_mode=True

class login(BaseModel):
    email:str
    password:str

