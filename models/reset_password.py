from sqlalchemy import Column,Table , Integer,String 
from sqlalchemy.sql.sqltypes import DateTime
from config.database import meta

Reset_password=Table(
        "reset_password",
        meta,
        Column("id",Integer,primary_key=True,autoincrement=True),
        Column("user_id",Integer),
        Column('token',String),
        Column("createdAt",DateTime),
        Column("updatedAt",DateTime),
                )                
