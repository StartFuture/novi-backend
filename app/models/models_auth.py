from pydantic import BaseModel



class UserModel(BaseModel):
    email: str
    password_user: str


class token(BaseModel):
    token: str


class edit_password(BaseModel):
    current_password: str 
    new_password: str
