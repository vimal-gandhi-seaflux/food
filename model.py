from sqlalchemy import Column,Table , Integer,String ,ForeignKey
from database import meta
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.orm import relationship

login=Table(
        "login",
        meta,
        Column("id",Integer,primary_key=True,autoincrement=True),
        Column("name",String),
        Column("numbers",Integer),
        Column('email',String),
        Column('password',String),
        Column("createdAt",DateTime),
        Column("updatedAt",DateTime)
                ) 
   
    