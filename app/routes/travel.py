from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse

from dao import dao_travel
from models.models_travel import Travel
import utils 

router = APIRouter()

@router.post('/', status_code=status.HTTP_201_CREATED)
def write_data(token: str, travel: Travel):

    try:
        id_user = 2 #utils.get_user_id(token)
    except Exception:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='User not authorized')

    id_travel, messages = dao_travel.new_travel(
        id_user= id_user,
        id_accommodation= travel.id_accommodation,
        id_transport_from= travel.id_transport_from,
        id_transport_return= travel.id_transport_return,
        date_from= travel.date_from,
        date_return= travel.date_return,
        quantity_people= travel.quantity_people,
        price= travel.price ##? Preço publico no FrontEnd
    )

    dao_travel.new_travel_tour(
        id_travel= id_travel,
        id_tour= travel.id_tour
    )


    return JSONResponse(content=messages['message'])
    return JSONResponse(content=messages['message'])

@router.get("/history/{id_user}", status_code=status.HTTP_200_OK)
def get_history(id_user: int):
    
    query_travel = dao_travel.select_history(id_user)

    new_query_travel = []
    for item in query_travel:
        item['date_from'] = utils.format_date(item['date_from'])
        new_query_travel.append(item)

    data ={'travel': new_query_travel}
    return JSONResponse(content=data)

@router.get("/next_travel/{id_user}", status_code=status.HTTP_200_OK)
def get_next_travel(id_user: int):

    query_travel = dao_travel.next_travel(id_user)

    query_travel['date_from'] = utils.format_date(query_travel['date_from'])


    