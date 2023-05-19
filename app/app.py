from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware

from routes import autentication, users, reviews, profile, dest_obj

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
app.include_router(profile.router, prefix="/profile", tags=['perfil'])
app.include_router(dest_obj.router, prefix="/dest_obj", tags=['Objetivo e Destino da viagem'])
