from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from dao import dao
from models.user_model import perfil


router = APIRouter()


@router.post('/perfil', status_code=status.HTTP_200_OK)
def insert_perfil(perfil: perfil, id_user: dict):
    id_user = id_user['id_user']
    result = dao.insert_perfil(user=perfil, id_user=id_user)
    if not result:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,  detail='it was not possible to insert the profile in the database')
    return JSONResponse(status_code=status.HTTP_200_OK, content='profile inserted successfully.')


@router.get('/read_perfil', status_code=status.HTTP_200_OK)
def read_perfil(id_user: int):
    result = dao.read_perfil(id_user=id_user)
    if not result:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,  detail='profile not found.')
    return JSONResponse(content=result, status_code=status.HTTP_200_OK) 


@router.get('/read_all_perfil', status_code=status.HTTP_200_OK)
def read_all_perfil():
    result = dao.read_all_perfil()
    print(result)
    if not result:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,  detail='profiles not found.')
    return JSONResponse(content=result, status_code=status.HTTP_200_OK) 


@router.put('/update_perfil', status_code=status.HTTP_200_OK)
def update_perfil(user: perfil, id_user: dict, id_perfil: int):
    id_user = id_user['id_user']
    result = dao.update_perfil(user=user, id_user=id_user, id_perfil=id_perfil)
    if not result:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,  detail='it was not possible to updated the profile in the database')
    return JSONResponse(status_code=status.HTTP_200_OK, content='profile updated successfully.')


@router.delete('/delete_perfil', status_code=status.HTTP_200_OK)
def delete_perfil(id_user: int):
    result = dao.delete_perfil(id_user=id_user)
    if not result:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,  detail='it was not possible to delete the profile in the database')
    return JSONResponse(status_code=status.HTTP_200_OK, content='profile delete successfully.')