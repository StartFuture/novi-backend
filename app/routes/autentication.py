from datetime import datetime

from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.responses import JSONResponse
from fastapi.security import  OAuth2PasswordBearer, OAuth2PasswordRequestForm

from dao import dao, dao_users
import utils


router = APIRouter()


@router.post("/login", status_code=status.HTTP_200_OK)
def auth(user: OAuth2PasswordRequestForm = Depends()) -> dict:
    query_result = dao_users.verify_user_exist(user.username)# Verificação de existencia de usuario
    if query_result:# Se usuario existe:

        if utils.check_pwd_hash(password_hash=query_result["password_user"], password=user.password):# se senha esta correta
            token = utils.signJWT(user_id=query_result["id_user"], email= user.username)
            return JSONResponse(status_code=status.HTTP_200_OK, content=token)
        
        else:#Se senha esta incorreta:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Wrong input")#Mensagem informando input incorreto
        
    else:#se usuario não existe:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")#Mensagem informando que usuario não foi encontrado


@router.get("/get_user_by_id", status_code=status.HTTP_200_OK)
def get_user_by_id(token: str = Depends(utils.verify_token)):
    print(token["sub"])
    #print(token_result)
    query = dao.verify_user_exist_by_id_join_address(token["sub"])
    return JSONResponse(content='it´s working')