from fastapi import FastAPI
from routes import autentication, users, reviews

app = FastAPI()

app.include_router(autentication.router, prefix="/auth", tags=['autenticaçao'])
app.include_router(users.router, prefix="/user", tags=['usuarios'])
app.include_router(reviews.router, prefix="/reviews", tags=['avaliações'])
























