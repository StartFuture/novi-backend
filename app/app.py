from fastapi import FastAPI, status, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from routes import autentication, users, destinations, reviews, profile, objective, travel_quiz, password_edit, travel, table

app = FastAPI()

@app.get("/status", status_code=status.HTTP_200_OK)
def health_check():

    return JSONResponse(content='Status OK')


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

app.include_router(autentication.router, prefix="/auth", tags=['Autenticação'])
app.include_router(users.router, prefix="/user", tags=['Usuários'])
app.include_router(reviews.router, prefix="/reviews", tags=['Avaliações'])
app.include_router(profile.router, prefix="/profile", tags=['Perfil'])
app.include_router(objective.router, prefix="/objective_tour", tags=['Objetivo da viagem'])
app.include_router(travel_quiz.router, prefix="/travel_quiz", tags=['Questionário para a viagem'])
app.include_router(destinations.router, prefix="/destination", tags=['Destinatination']) # Remover Destination
app.include_router(password_edit.router, prefix="/password", tags=['Edição de senha'])
app.include_router(travel.router, prefix="/travel", tags=['Viagens'])
app.include_router(table.router, prefix="/table", tags=['Tabelas'])

# python3 -m uvicorn app:app --reload

# Get all comments to landing page
@app.get("/get-comment", status_code=status.HTTP_200_OK)
def get_all_comments():
    comments = [
        {'id': 1, 'img': 'img', 'user_name': 'Paula Lima Santos', 'perfil': 'Viajante', 'stars': 5, 'comment': 'Lorem ipsum dolor sit amet consectetur. Turpis dignissim sed et et interdum non dolor. Aliquam amet eleifend sit sagittis egestas etiam sed morbi. Suspendisse suscipit mauris at aliquam tristique risus nunc netus nullam. Ac sociis lorem a in sed mauris.'},
        {'id': 1, 'img': 'img', 'user_name': 'Paula Lima Santos', 'perfil': 'Viajante', 'stars': 5, 'comment': 'Lorem ipsum dolor sit amet consectetur. Turpis dignissim sed et et interdum non dolor. Aliquam amet eleifend sit sagittis egestas etiam sed morbi. Suspendisse suscipit mauris at aliquam tristique risus nunc netus nullam. Ac sociis lorem a in sed mauris.'},
        {'id': 1, 'img': 'img', 'user_name': 'Paula Lima Santos', 'perfil': 'Viajante', 'stars': 5, 'comment': 'Lorem ipsum dolor sit amet consectetur. Turpis dignissim sed et et interdum non dolor. Aliquam amet eleifend sit sagittis egestas etiam sed morbi. Suspendisse suscipit mauris at aliquam tristique risus nunc netus nullam. Ac sociis lorem a in sed mauris.'},
        {'id': 1, 'img': 'img', 'user_name': 'Paula Lima Santos', 'perfil': 'Viajante', 'stars': 5, 'comment': 'Lorem ipsum dolor sit amet consectetur. Turpis dignissim sed et et interdum non dolor. Aliquam amet eleifend sit sagittis egestas etiam sed morbi. Suspendisse suscipit mauris at aliquam tristique risus nunc netus nullam. Ac sociis lorem a in sed mauris.'}   
    ]
    return comments
