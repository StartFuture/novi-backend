from datetime import datetime

from fastapi import APIRouter, HTTPException, status

from dao import dao
import utils
from models import models_auth


router = APIRouter()


@router.post("/login", status_code=status.HTTP_200_OK)
def auth(user: models_auth.UserModel) -> dict:
    query_result = dao.verify_user_exist(user.email)# Verificação de existencia de usuario
    if query_result:# Se usuario existe:
        if user.password == query_result['password_user']:# Validçãp de senha do usuario
            token_result = dao.verify_token_exist(query_result['id_user'])# Verificação de existencia de token
            if token_result:#Se token existe:
                is_revoked = dao.verify_token_is_revoked(id_token=token_result['id_token'])# Verificação se token esta revogado
                if not is_revoked:#Se token não esta revogado:
                    date_now = datetime.now().date()# Data do dia atual.
                    if(date_now.day - token_result['date_experience'].day) <= 3:#Se data de expiração e menor ou igual a 3 então token valido:
                        return {'message': 'Token is valid'}#retorna mensagem de token valido
                    else:#Se data de expiração é maior que 3 entao token e invalido:
                        dao.insert_revoked_token(id_token=token_result['id_token'], id_user=token_result['id_user'])#colocando token na tabela revoked_token
                        token = utils.signJWT(user_id=query_result['id_user'], type_jwt='JWT')#criar novo token
                        dao.update_token(token_result['id_user'])#Atualizando data de expiração do token no banco
                        return token# retorna novo token para o front
                else:#se token esta revogado:
                    token = utils.signJWT(query_result['id_user'], type_jwt='JWT')#criar novo token
                    dao.update_token(token_result['id_user'])#Atualizando data de expiração do token no banco
                    raise token# retorna novo token para o front 
            else:#Se token não existe:
                token = utils.signJWT(query_result['id_user'], type_jwt='JWT')#criar novo token
                dao.insert_new_token_and_code(query_result['id_user'])# inserindo token no banco
                return token#retorna token para o front   
        else:#Se senha esta incorreta:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Wrong input")#Mensagem informando input incorreto
    else:#se usuario não existe:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")#Mensagem informando que usuario não foi encontrado
    



