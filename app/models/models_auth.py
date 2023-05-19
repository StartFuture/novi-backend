from pydantic import BaseModel



class UserModel(BaseModel):
    email: str
    password: str


class token(BaseModel):
    token: str

