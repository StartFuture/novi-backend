from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse

from dao import dao_travel
from models.models_travel import Travel

router = APIRouter()

@router.post('/', status_code=status.HTTP_201_CREATED)
async def write_data(id_user: int, id_accommodation: int, id_transport_from: int , id_transport_return: int, id_tour: int, travel: Travel):
    
    id_travel, messages = await dao_travel.new_travel(
        id_user= id_user,
        id_accommodation= id_accommodation,
        id_transport_from= id_transport_from,
        id_transport_return= id_transport_return,
        date_from= travel.date_from,
        date_return= travel.date_return,
        quantity_people= travel.quantity_people,
        price= travel.price
    )

    await dao_travel.new_tour(
        id_travel= id_travel,
        id_tour= id_tour
    )

    return JSONResponse(content=messages['message'])

# @router.post('/travel_tours', status_code=status.HTTP_201_CREATED)
# async def create_tuor(id_travel: int, id_tour: int):
#     messages = await dao_tour.new_tour(
#         id_travel= id_travel,
#         id_tour= id_tour
#     )

#     return JSONResponse(content=messages['Travel tour create successfully'])