import email
from lib2to3.pgen2 import token
from os import name
from sqlite3 import Timestamp
from venv import create
from pydantic import BaseModel
from typing import List,Optional

class Signup(BaseModel):
    name:str    
    email:str
    password:str
    createdAt=Timestamp
    updatedAt=Timestamp
    class config():
        orm_mode=True

        

class login(BaseModel):
    email:str
    password:str 
    class config():
        orm_mode=True

class forgot(BaseModel):
    email:str
    class config():
        orm_mode=True

class reenter_password(BaseModel):
    token:str
    password:str






       