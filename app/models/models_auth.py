from pydantic import BaseModel


class token(BaseModel):
    token: str


class edit_password(BaseModel):
    current_password: str 
    new_password: str
