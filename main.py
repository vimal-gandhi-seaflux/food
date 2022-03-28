# Importing libraries
from fastapi import FastAPI
from routes.auth import Signup_route
from routes.recipe import Recipe_route


# Loading the .env file
from dotenv import load_dotenv

# Setting up dotenv
load_dotenv(dotenv_path='./.env')

# Initializing app
app = FastAPI(
    title='Food Recipe',
)

# Including the routes
app.include_router(Signup_route),
app.include_router(Recipe_route),











































# from ast import Str
# from fastapi import FastAPI,Depends
# from fastapi.security import OAuth2PasswordBearer , OAuth2PasswordRequestForm

# app = FastAPI()

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

# @app.post('/token')
# def token(form_data : OAuth2PasswordRequestForm = Depends()):
#     return {'access_token': form_data.username + 'token'}

# @app.get('/')
# def index(token: str = Depends(oauth2_scheme)):
#     return{'the_token ' : token }        
