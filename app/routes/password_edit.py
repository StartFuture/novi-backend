from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse

from dao import dao_password_edit




router = APIRouter()


@router.post('/password_edit', status_code=status.HTTP_200_OK)
def password_edit(id_user: dict, current_password: dict, new_password: dict):
    id_user = id_user['id_user']
    new_password = new_password['new_password']
    current_password = current_password['current_password']
    result_password = dao_password_edit.verify_user_password(id_user=id_user, current_password=current_password)
    if result_password:
        if result_password['password_user'] == current_password:
            result = dao_password_edit.update_password_user(id_user=id_user, new_password=new_password)
            if result:
                return JSONResponse(status_code=status.HTTP_200_OK, content='Password successfully updated.')
            else:
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Unable to update password in database.')
        else:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='mismatched password.')
    else:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Password user not found.')
