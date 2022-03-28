#Importing libraries
from fastapi import APIRouter, Request
from fastapi.param_functions import Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from controllers.auth import Authentication
from schemas.auth import Signup, forgot,login ,reenter_password


Signup_route=APIRouter(tags=['Authentication'])


@Signup_route.post('/Signup')
def user_registion(request: Signup):
    return Authentication.Signup(request)

@Signup_route.post("/login")
def login(request: Request, user: OAuth2PasswordRequestForm = Depends()):
    return Authentication.login(request=user, locale= request.headers['accept-language'])


@Signup_route.post("/forgot")
def forgot(request: forgot):
    return Authentication.forgot(request)

@Signup_route.put("/reenter_password")
def reenter_password(request: reenter_password):
    return Authentication.reenter_password(request)    











# @Signup_route.post("/login")
# # def login(request: login):
# #     return Authentication.login(request)