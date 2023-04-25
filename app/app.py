from fastapi import FastAPI
from routes import autentication, users

app = FastAPI()

app.include_router(autentication.router, prefix="/auth", tags=['autenticaçao'])
app.include_router(users.router, prefix="/user", tags=['usuarios'])
























