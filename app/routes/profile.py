from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.responses import JSONResponse
from dao import dao
from models.user_model import perfil
import utils

router = APIRouter()


@router.post('/profile', status_code=status.HTTP_200_OK)
def insert_perfil(profile: perfil,  token: str = Depends(utils.verify_token)):
    id_user = token["sub"]
    result = dao.insert_profile(user=profile, id_user=id_user)
    if not result:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,  detail='it was not possible to insert the profile in the database')
    return JSONResponse(status_code=status.HTTP_200_OK, content='profile inserted successfully.')


@router.get('/read_profile', status_code=status.HTTP_200_OK)
def read_profile(token: str = Depends(utils.verify_token)):

    result = dao.read_profile(id_user=token["sub"])
    if not result:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,  detail='profile not found.')
    return JSONResponse(content=result, status_code=status.HTTP_200_OK) 


@router.get('/read_all_profile', status_code=status.HTTP_200_OK)
def read_all_profile():
    result = dao.read_all_profile()
    print(result)
    if not result:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,  detail='profiles not found.')
    return JSONResponse(content=result, status_code=status.HTTP_200_OK) 


@router.put('/update_profile', status_code=status.HTTP_200_OK)
def update_profile(user: perfil, id_profile: int, token: str = Depends(utils.verify_token)):
    id_user = token["sub"]
    result = dao.update_profile(user=user, id_user=id_user, id_profile=id_profile)
    if not result:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,  detail='it was not possible to updated the profile in the database')
    return JSONResponse(status_code=status.HTTP_200_OK, content='profile updated successfully.')


@router.delete('/delete_profile', status_code=status.HTTP_200_OK)
def delete_perfil(token: str = Depends(utils.verify_token)):
    result = dao.delete_profile(id_user=token["sub"])
    if not result:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,  detail='it was not possible to delete the profile in the database')
    return JSONResponse(status_code=status.HTTP_200_OK, content='profile delete successfully.')