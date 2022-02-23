from fastapi import FastAPI
from routers import register
import model 



app=FastAPI()



app.include_router(register.router)

