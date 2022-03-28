from sqlalchemy import Column,Table , Integer,String 
from sqlalchemy.sql.sqltypes import DateTime
from config.database import meta

Signup_table=Table(
        "user_registration",
        meta,
        Column("id",Integer,primary_key=True,autoincrement=True),
        Column("name",String),
        Column('email',String),
        Column('password',String),
        Column("createdAt",DateTime),
        Column("updatedAt",DateTime),
                )    
