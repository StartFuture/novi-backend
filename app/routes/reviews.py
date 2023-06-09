from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.responses import JSONResponse

from dao import dao
from models.models_user import user_review
import utils


router = APIRouter()


@router.post('/review', status_code=status.HTTP_200_OK)
def review(user: user_review, token: str = Depends(utils.verify_token)):
    id_user = token["sub"]
    result = dao.insert_review(user=user, id_user=id_user)
    if not result:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,  detail='it was not possible to insert the comment in the database')
    return JSONResponse(status_code=status.HTTP_200_OK, content='comment inserted successfully.')


@router.get('/read_reviews', status_code=status.HTTP_200_OK)
def read_review(token: str = Depends(utils.verify_token)):
    result = dao.read_review(id_user=token["sub"])
    if not result:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,  detail='No comments were found.')
    return JSONResponse(content=result, status_code=status.HTTP_200_OK) 


@router.get('/read_all_reviews', status_code=status.HTTP_200_OK)
def read_review():
    result = dao.read_all_review()
    if not result:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,  detail='No comments were found.')
    return JSONResponse(content=result, status_code=status.HTTP_200_OK) 


@router.put('/update_review', status_code=status.HTTP_200_OK)
def review(user: user_review, id_review: int, token: str = Depends(utils.verify_token)):
    id_user = token["sub"]
    result = dao.update_review(user=user, id_user=id_user, id_review=id_review)
    if not result:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,  detail='it was not possible to updated the comment in the database')
    return JSONResponse(status_code=status.HTTP_200_OK, content='comment updated successfully.')


@router.delete('/delete_review', status_code=status.HTTP_200_OK)
def review(id_review: int):
    result = dao.delete_review(id_review=id_review)
    if not result:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,  detail='it was not possible to delete the comment in the database')
    return JSONResponse(status_code=status.HTTP_200_OK, content='comment delete successfully.')