from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from dao import dao
from models.user_model import objective_destination


router = APIRouter()


@router.post('/objective_and_destination', status_code=status.HTTP_200_OK)
def insert_objective_and_destination(obj_dest: objective_destination, id_user: dict):
    id_user = id_user['id_user']
    result = dao.insert_objective_and_destination(obj_dest=obj_dest, id_user=id_user)
    if not result:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,  detail='it was not possible to insert the information into the database')
    return JSONResponse(status_code=status.HTTP_200_OK, content='information inserted successfully.')


@router.get('/read_objective_and_destination', status_code=status.HTTP_200_OK)
def read_objective_and_destination(id_dest_obj: int):
    result = dao.read_objective_and_destination(id_dest_obj=id_dest_obj)
    if not result:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,  detail='Not found.')
    return JSONResponse(content=result, status_code=status.HTTP_200_OK) 


@router.get('/read_all_objective_and_destination', status_code=status.HTTP_200_OK)
def read_all_objective_and_destination():
    result = dao.read_all_objective_and_destination()
    print(result)
    if not result:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,  detail='Not found.')
    return JSONResponse(content=result, status_code=status.HTTP_200_OK) 


@router.put('/update_objective_and_destination', status_code=status.HTTP_200_OK)
def update_objective_and_destination(obj_dest: objective_destination, id_user: dict, id_obj_dest: int):
    id_user = id_user['id_user']
    result = dao.update_objective_and_destination(obj_dest=obj_dest, id_user=id_user, id_dest_obj=id_obj_dest)
    if not result:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,  detail='it was not possible to updated database')
    return JSONResponse(status_code=status.HTTP_200_OK, content='database updated successfully.')


@router.delete('/delete_objective_and_destination', status_code=status.HTTP_200_OK)
def delete_objective_and_destination(id_dest_obj: int):
    result = dao.delete_objective_and_destination(id_dest_obj=id_dest_obj)
    if not result:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,  detail='it was not possible to delete information in the database')
    return JSONResponse(status_code=status.HTTP_200_OK, content='successfully deleted.')