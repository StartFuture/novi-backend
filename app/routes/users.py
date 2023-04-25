from fastapi import APIRouter, HTTPException, status
from dao import dao



router = APIRouter()




@router.delete("/delete_user/{id_user}", status_code=status.HTTP_200_OK)
def delete(id_user: int):
    query_result = dao.delete_user_by_id(id_user=id_user)
    if query_result:
        return {'message': 'user delete.'}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="wrong input")
