from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from dao import dao_travel_quiz
from models.models_travel_quiz import travel_activities, travel_options, travel_cultures, weather_option


router = APIRouter()


@router.post('/insert_user_questionnaire', status_code=status.HTTP_200_OK)
def insert_user_questionnaire(activitie: travel_activities, options: travel_options, culture: travel_cultures, weather: weather_option, id_user: dict):
    id_user = id_user['id_user']
    result_activitie = dao_travel_quiz.insert_travel_activitie(activitie=activitie, id_user=id_user)
    result_opitions = dao_travel_quiz.insert_travel_options(option=options, id_user=id_user)
    result_cultures = dao_travel_quiz.insert_travel_cultures(culture=culture, id_user=id_user)
    result_weather = dao_travel_quiz.insert_weather_option(weather=weather, id_user=id_user)

    if not result_activitie:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='unable to insert travel activitie into database.')
    if not result_opitions:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='unable to insert travel opitions into database.')
    if not result_cultures:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='unable to insert travel cultures into database.') 
    if not result_weather:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='unable to insert travel weather into database.')
    return JSONResponse(status_code=status.HTTP_200_OK, content='Travel quiz entered successfully')


