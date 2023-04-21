from fastapi import FastAPI

from routes.user_route import user

app = FastAPI()

app.include_router(user, prefix='/usuarios', tags=['User'])
