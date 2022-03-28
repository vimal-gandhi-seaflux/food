from ast import Str
import email
from lib2to3.pgen2 import token
from os import name
from sqlite3 import Timestamp
from venv import create
from pydantic import BaseModel
from typing import List,Optional

class add_recipe(BaseModel):
    banner_image:str
    title:str
    description:str
    ingredients:str
    process:str
    any_video_link_if_available:str
    createdAt=Timestamp
    updatedAt=Timestamp
    class config():
        orm_mode=True

class update_recipe(BaseModel):
    id:int
    banner_image:str
    title:str
    description:str
    ingredients:str
    process:str
    any_video_link_if_available:str
    createdAt=Timestamp
    updatedAt=Timestamp
    class config():
        orm_mode=True





