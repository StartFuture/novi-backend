from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware

from routes import autentication, users, reviews

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(autentication.router, prefix="/auth", tags=['autenticaçao'])
app.include_router(users.router, prefix="/user", tags=['usuarios'])
app.include_router(reviews.router, prefix="/reviews", tags=['avaliações'])


