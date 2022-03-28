import fastapi
from config.database import db
from schemas.auth import Signup , login , forgot ,reenter_password
from schemas.token import Token,TokenData
from models.user_registration import Signup_table
from models.reset_password import Reset_password
from helper.hashing import hash
from fastapi import APIRouter, Depends, Response,status,HTTPException,UploadFile,File
from datetime import datetime
from helper.token import TokenHelper
import uuid
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


class Authentication:
            # Add user-Registration API Implementation
            def Signup(request: Signup):
                new_data = db.execute(Signup_table.insert().values(name=request.name,email=request.email,password =hash.bcrypt(request.password)))
                return 'succesfull'
                
            # Login api implementation & OAuth2 
            def login(locale: str = "en",request: OAuth2PasswordRequestForm = Depends()):
                user = db.execute(Signup_table.select().where(Signup_table.c.email == request.username)).fetchall()
                if user == [] or not hash.verify(
                    request.password, user[0]["password"]
                ):
                    return 'INVALID_CREDENTIAL'
                else:
                    access_token = TokenHelper.create_access_token(
                    data={"sub": request.username}
                )
                    user = db.execute(Signup_table.select().where(Signup_table.c.email == request.username).with_only_columns(Signup_table.c.id,Signup_table.c.name,Signup_table.c.email)).fetchall()
                    return {
                        "access_token": access_token,
                        "token_type": "bearer",
                        "data": user[0],
                    }
            # #login User API  
     
            # def login(request: login):
            #     user = db.execute( Signup_table.select(whereclause=(Signup_table.c.email == request.email))).first()
            #     if not user:
            #         raise HTTPException (status_code=status.HTTP_404_NOT_FOUND,detail=f"invalid  ")

            #     if not hash.verify( request.password , user.password   ):
            #         raise  HTTPException (status_code=status.HTTP_404_NOT_FOUND,detail=f"invalid password")
            #     access_token = create_access_token(data={"sub": user.email})

            #     # new_data = db.execute(Signup_table.insert().values(token=request.token))
            #     return {"access_token": access_token, "token_type": "bearer"}
    
            #     # else:
            #     #     return "Logged in successfully"     

           # Forgot Password API
            def forgot(request :forgot):
                user = db.execute( Signup_table.select(whereclause=(Signup_table.c.email == request.email))).first()  
                if not user:
                    raise HTTPException (status_code=status.HTTP_404_NOT_FOUND,detail=f"invalid  ")
                token = uuid.uuid4()
                new_data = db.execute(Reset_password.insert().values(user_id=user.id ,token = token))
                return token

            # ------------------- update password ---------------

            def reenter_password(request :reenter_password):
                user = db.execute(Reset_password.select(whereclause=(Reset_password.c.token == request.token))).first()
                if not user:
                        raise HTTPException (status_code=status.HTTP_404_NOT_FOUND,detail=f"invalid  token ")
                else :
                    db.execute(Signup_table.update().values(password = hash.bcrypt(request.password)).where(user.user_id == Signup_table.c.id))
                    return "successfully"