from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from dao import dao_travel_activities
from models.models_travel_activities import travel_activities


router = APIRouter()


@router.post('/insert_travel_activitie', status_code=status.HTTP_200_OK)
def insert_travel_activitie(activitie: travel_activities, id_user: dict):
    id_user = id_user['id_user']
    result = dao_travel_activities.insert_travel_activitie(activitie=activitie, id_user=id_user)
    if not result:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='unable to insert travel activities into database.')
    return JSONResponse(status_code=status.HTTP_200_OK, content='Travel activities entered successfully')


@router.get('/read_travel_activities', status_code=status.HTTP_200_OK)
def read_travel_activities(id_activitie: int):
    result = dao_travel_activities.read_travel_activitie(id_activitie=id_activitie)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No travel activity found')
    return JSONResponse(content=result, status_code=status.HTTP_200_OK)


@router.get('/read_all_travel_activities', status_code=status.HTTP_200_OK)
def read_all_travel_activities():
    result = dao_travel_activities.read_all_travel_activities()
    if not result:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='No travel activity found')
    return JSONResponse(content=result, status_code=status.HTTP_200_OK)


@router.put('/update_travel_activities', status_code=status.HTTP_200_OK)
def update_travel_activities(activitie: travel_activities, id_user: dict, id_activitie: dict):
    id_activitie = id_activitie['id_activitie']
    id_user = id_user['id_user']
    result = dao_travel_activities.update_tarvel_activities(activitie=activitie, id_user=id_user, id_activitie=id_activitie)
    if not result:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='unable to update travel activities')
    return JSONResponse(status_code=status.HTTP_200_OK, content='Travel activities updated successfully')


@router.delete('/delete_travel_activities', status_code=status.HTTP_200_OK)
def delete_travel_activities(id_user: dict, id_activitie: dict):
    id_user = id_user['id_user']
    id_activitie = id_activitie['id_activitie']
    result = dao_travel_activities.delete_travel_activities(id_user=id_user, id_activitie=id_activitie)
    if not result:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='unable to delete travel activities')
    return JSONResponse(status_code=status.HTTP_200_OK, content='Travel activities deleted successfully')