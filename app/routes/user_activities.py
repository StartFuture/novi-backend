from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from dao import dao
from models.user_model_interview import user_preferred_activities


router = APIRouter()


@router.post('/insert_activitie', status_code=status.HTTP_200_OK)
def insert_activitie(activitie: user_preferred_activities, id_user: dict):
    id_user = id_user['id_user']
    result = dao.insert_activitie(activitie=activitie, id_user=id_user)
    if not result:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='unable to insert user activities into database.')
    return JSONResponse(status_code=status.HTTP_200_OK, content='User activities entered successfully')


@router.get('/read_activities', status_code=status.HTTP_200_OK)
def read_activities(id_activitie: int):
    result = dao.read_activitie(id_activitie=id_activitie)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No user activity found')
    return JSONResponse(content=result, status_code=status.HTTP_200_OK)


@router.get('/read_all_activities', status_code=status.HTTP_200_OK)
def read_all_activities():
    result = dao.read_all_activities()
    if not result:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='No user activity found')
    return JSONResponse(content=result, status_code=status.HTTP_200_OK)


@router.put('/update_user_activities', status_code=status.HTTP_200_OK)
def update_user_activities(activitie: user_preferred_activities, id_user: dict, id_activitie: dict):
    id_activitie = id_activitie['id_activitie']
    id_user = id_user['id_user']
    result = dao.update_user_activities(activitie=activitie, id_user=id_user, id_activitie=id_activitie)
    if not result:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='unable to update user activities')
    return JSONResponse(status_code=status.HTTP_200_OK, content='User activities updated successfully')


@router.delete('/delete_user_activities', status_code=status.HTTP_200_OK)
def delete_user_activities(id_user: dict, id_activitie: dict):
    id_user = id_user['id_user']
    id_activitie = id_activitie['id_activitie']
    result = dao.delete_user_activities(id_user=id_user, id_activitie=id_activitie)
    if not result:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='unable to delete user activities')
    return JSONResponse(status_code=status.HTTP_200_OK, content='User activities deleted successfully')