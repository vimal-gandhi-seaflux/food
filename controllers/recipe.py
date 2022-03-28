from config.database import db
from schemas.recipe import add_recipe , update_recipe

from models.recipe_table import Recipe_table
from helper.hashing import hash
from fastapi import status,HTTPException,UploadFile,File



class Recipe:
        
    def add_recipe(request: add_recipe):
            new_data = db.execute(Recipe_table.insert().values(
                    banner_image = request.banner_image,
                    title = request.title,
                    description=request.description,
                    ingredients =request.ingredients,
                    process = request.process,
                    any_video_link_if_available= request.any_video_link_if_available
            ))
            print(new_data)
            return 'succesfull'

    def get_data():
               new_data = db.execute(Recipe_table.select()).fetchall()
               return new_data  

    def update_item(request: update_recipe):
        data = db.execute(Recipe_table.select().where(Recipe_table.c.id == request.id)).fetchone()
        if not data:
            return {'NUMBER_NOT_FOUND' }
        else:
            db.execute(
                Recipe_table.update().values(
                    banner_image = request.banner_image,
                    title = request.title,
                    description=request.description,
                    ingredients =request.ingredients,
                    process = request.process,
                    any_video_link_if_available= request.any_video_link_if_available  
                ).where(Recipe_table.c.id == request.id)
            )
            return {"item_UPDATE"}

    def remove_recipe(id):
            data = db.execute(Recipe_table.select().where(Recipe_table.c.id == id)).fetchall()
            if not data:
                return "Recipe_NOT_FOUND"
            else:
                db.execute(Recipe_table.delete().where(Recipe_table.c.id == id))
                return 'remove_recipe'
            
       

            
          