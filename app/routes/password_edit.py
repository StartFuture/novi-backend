from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.responses import JSONResponse

from dao import dao_password_edit
import utils


router = APIRouter()


@router.post('/password_edit', status_code=status.HTTP_200_OK)
def password_edit(current_password: dict, new_password: dict, token: str = Depends(utils.verify_token)):
    
    id_user = token["sub"]

    new_password = utils.get_pwd_hash(password=new_password['new_password'])
    current_password = current_password['current_password']
    result_password = dao_password_edit.verify_user_password(id_user=id_user)
    
    if result_password:
        if utils.check_pwd_hash(password_hash=result_password['password_user'], password=current_password ):
            result = dao_password_edit.update_password_user(id_user=id_user, new_password=new_password)

            if result:
                return JSONResponse(status_code=status.HTTP_200_OK, content='Password successfully updated.')
            else:
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Unable to update password in database.')
        else:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='mismatched password.')
    else:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Password user not found.')
