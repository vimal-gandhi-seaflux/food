import re
from urllib import response
from urllib.request import Request
from fastapi import APIRouter
from sqlalchemy import column
from schemas.recipe import add_recipe
from schemas.recipe import update_recipe

from models.recipe_table import Recipe_table
from controllers.recipe import Recipe


Recipe_route=APIRouter(tags=['Recipe'])


@Recipe_route.post('/add_recipe')
def add_recipe(request: add_recipe):
    return Recipe.add_recipe(request)

@Recipe_route.get('/get_data')
def get_date():
    return Recipe.get_data()


@Recipe_route.put("/update-item")
def update_item(request: update_recipe):
    return Recipe.update_item(request)  


@Recipe_route.delete("/recipe-remove")
def remove_recipe(id:int):
    return Recipe.remove_recipe(id)    