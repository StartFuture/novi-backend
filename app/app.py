from datetime import datetime
from random import randint

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Body, Depends, HTTPException, status
from pydantic import BaseModel

import dao
import utils


class UserModel(BaseModel):
    email: str
    password: str



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



@app.post("/login", status_code=status.HTTP_200_OK)
def auth(user: UserModel) -> dict:
    query_result = dao.verify_user_exist(user.email)# Verificação de existencia de usuario
    if query_result:# Se usuario existe:

        if user.password == query_result['password_user']:# Validçãp de senha do usuario
            token_result = dao.verify_token_exist(query_result['id_user'])# Verificação de existencia de token

            if token_result:#Se token existe:
                is_revoked = dao.verify_token_is_revoked(id_token=token_result['id_token'])# Verificação se token esta revogado
                if not is_revoked:#Se token não esta revogado:
                    date_now = datetime.now().date()# Data do dia atual.

                    if(date_now.day - token_result['date_experience'].day) <= 3:#Se data de expiração# e menor ou igual a 3 então token valido:
                        return {'message': 'Token is valid'}

                    else:#Se data de expiração é maior que 3 entao token e invalido:
                        dao.insert_revoked_token(id_token=token_result['id_token'], id_user=token_result['id_user'])
                        token = utils.signJWT(user_id=query_result['id_user'], type_jwt='JWT')
                        dao.update_token(token_result['id_user'])
                        return token

                else:#se token esta revogado:
                    token = utils.signJWT(query_result['id_user'], type_jwt='JWT')
                    dao.update_token(token_result['id_user'])
                    raise token

            else:#Se token não existe:
                token = utils.signJWT(query_result['id_user'], type_jwt='JWT')
                dao.insert_new_token_and_code(query_result['id_user'])
                return token

        else:#Se senha esta incorreta:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Wrong input")#Mensagem informando input incorreto
    else:#se usuario não existe:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")#Mensagem informando que usuario não foi encontrado



@app.post("/delete_user/{id_user}", status_code=status.HTTP_200_OK)
def delete(id_user: int):
    query_result = dao.delete_user_by_id(id_user=id_user)
    if query_result:
        return {'message': 'user delete.'}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="wrong input")


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