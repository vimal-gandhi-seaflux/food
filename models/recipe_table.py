from sqlalchemy import Column,Table , Integer,String 
from sqlalchemy.sql.sqltypes import DateTime
from config.database import meta

Recipe_table=Table(
        "recipe_table",
        meta,
        Column("id",Integer,primary_key=True,autoincrement=True),
        Column("banner_image",String),
        Column("title",String),
        Column("description",String),
        Column("ingredients",String),
        Column("process",String),
        Column("any_video_link_if_available",String),
        Column("createdAt",DateTime),
        Column("updatedAt",DateTime),
        )                
