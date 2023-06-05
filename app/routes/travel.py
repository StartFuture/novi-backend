from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse

from dao import dao_travel, dao_probability_method
from models.models_travel import Travel,  TravelCalc
import probability_method
from utils import get_user_id


router = APIRouter()


@router.post('/', status_code=status.HTTP_201_CREATED)
def write_data(id_user: int, travel: Travel):

    # try:
    #     id_user = 2 #utils.get_user_id(token)
    # except Exception:
    #     raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
    #                         detail='User not authorized')

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
        id_travel= id_travel['LAST_INSERT_ID()'],
        id_tour= travel.id_tour
    )

    return JSONResponse(content=messages['message'])


@router.get("/history/{id_user}", status_code=status.HTTP_200_OK)
def get_history(id_user: int):
    
    query_travel = dao_travel.select_history(id_user)
    

    new_query_travel = []
    for item in query_travel:
        item['date_from'] = utils.format_date(item['date_from'])
        item['travel_destination'] = utils.format_travel(item['travel_destination'])
        new_query_travel.append(item)

    data = {'travel_history': new_query_travel}

    return JSONResponse(content=data)


@router.post('/probality_method', status_code=status.HTTP_200_OK)
def get_probability_method(id_user: int):
    user_quiz = dao_probability_method.get_user_questions(id_user=id_user)
    if user_quiz['can_leave_country'] == 1:
        travel_abroad = dao_probability_method.get_travel_abroad()
        result = probability_method.probability_calculation_travels(travels=travel_abroad, user_quiz=user_quiz)
    else:
        travel_data = dao_probability_method.get_travels()
        result = probability_method.probability_calculation_travels(travels=travel_data, user_quiz=user_quiz)

    return JSONResponse(result) 