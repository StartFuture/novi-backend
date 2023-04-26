from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware

from routes import autentication, users

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

# python3 -m uvicorn app:app --reload

# Get all comments to landing page
@app.get("/get-comment", status_code=status.HTTP_200_OK)
def get_all_comments():
    comments = [
        {'id': 1, 'img': 'img', 'user_name': 'Paula Lima Santos', 'perfil': 'Viajante', 'stars': 1, 'comment': 'Lorem ipsum dolor sit amet consectetur. Turpis dignissim sed et et interdum non dolor. Aliquam amet eleifend sit sagittis egestas etiam sed morbi. Suspendisse suscipit mauris at aliquam tristique risus nunc netus nullam. Ac sociis lorem a in sed mauris.'},
        {'id': 1, 'img': 'img', 'user_name': 'Paula Lima Santos', 'perfil': 'Viajante', 'stars': 2, 'comment': 'Lorem ipsum dolor sit amet consectetur. Turpis dignissim sed et et interdum non dolor. Aliquam amet eleifend sit sagittis egestas etiam sed morbi. Suspendisse suscipit mauris at aliquam tristique risus nunc netus nullam. Ac sociis lorem a in sed mauris.'},
        {'id': 1, 'img': 'img', 'user_name': 'Paula Lima Santos', 'perfil': 'Viajante', 'stars': 3, 'comment': 'Lorem ipsum dolor sit amet consectetur. Turpis dignissim sed et et interdum non dolor. Aliquam amet eleifend sit sagittis egestas etiam sed morbi. Suspendisse suscipit mauris at aliquam tristique risus nunc netus nullam. Ac sociis lorem a in sed mauris.'},
        {'id': 1, 'img': 'img', 'user_name': 'Paula Lima Santos', 'perfil': 'Viajante', 'stars': 5, 'comment': 'Lorem ipsum dolor sit amet consectetur. Turpis dignissim sed et et interdum non dolor. Aliquam amet eleifend sit sagittis egestas etiam sed morbi. Suspendisse suscipit mauris at aliquam tristique risus nunc netus nullam. Ac sociis lorem a in sed mauris.'}   
    ]
    return comments
