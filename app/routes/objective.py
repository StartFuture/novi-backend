from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from dao import dao
from models.user_model import objective


router = APIRouter()


@router.post('/objective', status_code=status.HTTP_200_OK)
def insert_objective(objective: objective, id_destination: dict):
    id_destination = id_destination['id_destination']
    result = dao.insert_objective(objective=objective, id_destination=id_destination)
    if not result:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,  detail='it was not possible to insert the objective into the database')
    return JSONResponse(status_code=status.HTTP_200_OK, content='Objective inserted successfully.')


@router.get('/read_objective', status_code=status.HTTP_200_OK)
def read_objective(id_objective: int):
    result = dao.read_objective(id_objective=id_objective)
    if not result:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,  detail='Objective Not found.')
    return JSONResponse(content=result, status_code=status.HTTP_200_OK) 


@router.get('/read_all_objective', status_code=status.HTTP_200_OK)
def read_all_objective():
    result = dao.read_all_objective()
    print(result)
    if not result:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,  detail='No travel objectives found.')
    return JSONResponse(content=result, status_code=status.HTTP_200_OK) 


@router.put('/update_objective', status_code=status.HTTP_200_OK)
def update_objective(objective: objective, id_destination: int, id_objective: int):
    result = dao.update_objective(objective=objective, id_destination=id_destination, id_objective=id_objective)
    if not result:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,  detail='it was not possible to updated database')
    return JSONResponse(status_code=status.HTTP_200_OK, content='database updated successfully.')


@router.delete('/delete_objective', status_code=status.HTTP_200_OK)
def delete_objective(id_objective: int):
    result = dao.delete_objective(id_objective=id_objective)
    if not result:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,  detail='it was not possible to delete information in the database')
    return JSONResponse(status_code=status.HTTP_200_OK, content='successfully deleted.')