from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.responses import JSONResponse

from dao import dao_travel, dao_probability_method
from models.models_travel import Travel
import probability_method
import utils


router = APIRouter()


@router.post('/', status_code=status.HTTP_201_CREATED)
def write_data(travel: Travel, token: str = Depends(utils.verify_token)):

    try:
        id_user = token["sub"]
    except Exception:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='User not authorized')

    id_travel, messages = dao_travel.new_travel(
        id_user= token["sub"],
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


@router.get("/history", status_code=status.HTTP_200_OK)
def get_history(token: str = Depends(utils.verify_token)):
    
    query_travel = dao_travel.select_history(token["sub"])

    new_query_travel = []
    for item in query_travel:
        item['date_from'] = utils.format_date(item['date_from'])
        item['travel_destination'] = utils.format_travel(item['travel_destination'])
        new_query_travel.append(item)

    data = {'travel_history': new_query_travel}

        return JSONResponse(content=data)


@router.get("/next_travel", status_code=status.HTTP_200_OK)
def get_next_travel(token: str = Depends(utils.verify_token)):

    query_travel = dao_travel.next_travel(token["sub"])

    query_travel['date_from'] = utils.format_date(query_travel['date_from'])

    return JSONResponse(content=query_travel)

 
@router.post('/probality_method', status_code=status.HTTP_200_OK)
def get_probability_method(token: str = Depends(utils.verify_token)):

    user_quiz = dao_probability_method.get_user_questions(id_user=token["sub"])
    
    if user_quiz['can_leave_country'] == 1:

        travel_abroad = dao_probability_method.get_travel_abroad()
        result = probability_method.probability_calculation_travels(travels=travel_abroad, user_quiz=user_quiz)

    else:

        travel_data = dao_probability_method.get_travels()
        result = probability_method.probability_calculation_travels(travels=travel_data, user_quiz=user_quiz)

    return JSONResponse(result) 
