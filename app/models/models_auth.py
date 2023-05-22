from pydantic import BaseModel



class UserModel(BaseModel):
    email: str
    password_user: str


class token(BaseModel):
    token: str

