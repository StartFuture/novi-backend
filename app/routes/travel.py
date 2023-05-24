from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse

from dao import dao_travel
from models.models_travel import Travel

router = APIRouter()

@router.post('/', status_code=status.HTTP_201_CREATED)
async def write_data(id_user: int, id_accommodation: int, id_transport_from: int , id_transport_return: int, travel: Travel):
    
    messages = await dao_travel.new_travel(
        id_user= id_user,
        id_accommodation= id_accommodation,
        id_transport_from= id_transport_from,
        id_transport_return= id_transport_return,
        date_from= travel.date_from,
        date_return= travel.date_return,
        quantity_people= travel.quantity_people,
        price= travel.price
    )

    return JSONResponse(content=messages['message'])
