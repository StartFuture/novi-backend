from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse

from dao import dao_travel
from models.models_travel import Travel
from utils import get_user_id, signJWT

router = APIRouter()

@router.post('/', status_code=status.HTTP_201_CREATED)
async def write_data(token: str, travel: Travel):

    try:
        id_user = 2 #get_user_id(token)
    except Exception:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='User not authorized')

    id_travel, messages = await dao_travel.new_travel(
        id_user= id_user,
        id_accommodation= travel.id_accommodation,
        id_transport_from= travel.id_transport_from,
        id_transport_return= travel.id_transport_return,
        date_from= travel.date_from,
        date_return= travel.date_return,
        quantity_people= travel.quantity_people,
        price= travel.price ##? Preço publico no FrontEnd
    )

    await dao_travel.new_tour(
        id_travel= id_travel,
        id_tour= travel.id_tour
    )

    return JSONResponse(content=messages['message'])