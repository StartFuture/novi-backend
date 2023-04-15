from datetime import datetime
from random import randint

from fastapi import FastAPI, Body, Depends, HTTPException, status
from pydantic import BaseModel

import dao
import utils


class UserModel(BaseModel):
    email: str
    password: str



app = FastAPI()


@app.post("/login", status_code=status.HTTP_200_OK)
def auth(user: UserModel) -> dict:
    query_result = dao.verify_user_exist(user.email)
    if query_result:

        if user.password == query_result['password_user']:
            token_result = dao.verify_token_exist(query_result['id_user'])
            if token_result:
                pass
            else:
                pass
        else:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="wrong input")
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")


"""@app.post("/login", status_code=status.HTTP_200_OK)
def auth(user: UserModel) -> dict:
    query_result = dao.verify_user_exist(user.email)
    if query_result:# Usuario existe?
        token_result = dao.verify_token_exist(query_result['id_user'])

        if token_result:# Existe um token?
            is_valid = dao.verify_token_is_revoked(id_token=token_result['id_token'])

            if is_valid:# Se token não revogado:
                date_now = datetime.now().date()

                if (date_now - token_result['create_date']).days <= 3:#Se data de criação e menor ou igual a 3 então token valido
                    return {'access_token': token_result['user_token']}

                else:# Se data de criação maior que 3 entao token invalido:
                    dao.insert_revoked_token(token_result['id_token'], token_result['id_user'])

                    token = utils.signJWT(token_result['id_user'], type_jwt='two_auth')

                    dao.insert_new_token(id_user=token_result['id_user'], user_token=token['access_token'])

                    return {'access_token': token['access_token']}

            else:# Se token revogado:
                token = utils.signJWT(token_result['id_user'], type_jwt='two_auth')

                dao.insert_new_token(id_user=token_result['id_user'], user_token=token['access_token'])

                return {'access_token': token['access_token']}

        else:# Usuario nunca logado antes.
            code = randint(100000, 999999)
            dao.insert_new_code(id_user=query_result['id_user'], user_code=code)
            #Aqui vai a função de enviar email
            token = utils.signJWT(query_result['id_user'], type_jwt='code')
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail={'msg': 'User don´t have two_auth.', 'code': code, 'access_token': token})

    else:# se não existe:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
"""




