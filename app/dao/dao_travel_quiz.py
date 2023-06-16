from parameters import HOST, USER, PASSWORD, DATABASE, PORT
from models.models_travel_quiz import travel_activities, travel_options, travel_cultures, weather_option
from dao.dao import connect_database


#inserindo atividades de preferencia do ususario
def insert_travel_activitie(activitie: travel_activities, id_user: int):
    connection, cursor = connect_database(
        host=HOST,
        port=int(PORT),
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    action = f"""insert into travel_activities (water_preference, walk_preference, historic_preference, sport_preference, food_preference, id_user)
                values ({activitie.water_preference}, {activitie.walk_preference}, {activitie.historic_preference},
                {activitie.sport_preference}, {activitie.food_preference}, {id_user});"""
    
    try:
        cursor.execute(action)
    except Exception:
        connection.close()
        return False
    else:
        connection.commit()
        connection.close()
        return True
    

def insert_travel_options(option: travel_options, id_user: int):
    connection, cursor = connect_database(
        host=HOST,
        port=int(PORT),
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    action = f"""insert into travel_options(travel_destination, travel_style, accommodation_style, night_style, can_leave_country, transport_style, id_user)
                values ({option.travel_destination}, {option.travel_style}, {option.acommodation_style},
                  {option.night_style}, {option.can_leave_country}, {option.transport_style}, {id_user});"""
    
    try:
        cursor.execute(action)
    except Exception:
        connection.close()
        return False
    else:
        connection.commit()
        connection.close()
        return True
    

def insert_travel_cultures(culture: travel_cultures, id_user: int):
    connection, cursor = connect_database(
        host=HOST,
        port=int(PORT),
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    action = f"""insert into travel_cultures(music_preference, building_preference, tradicion_preference, party_preference, no_preference, id_user)
                values ({culture.music_preference}, {culture.building_preference}, {culture.tradicion_preference},
                  {culture.party_preference}, {culture.no_preference}, {id_user});"""
    
    try:
        cursor.execute(action)
    except Exception:
        connection.close()
        return False
    else:
        connection.commit()
        connection.close()
        return True
    

def insert_weather_option(weather: weather_option, id_user: int):
    connection, cursor = connect_database(
        host=HOST,
        port=int(PORT),
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    action = f"""insert into weather_option(warm, mild, cold, no_preference, id_user)
                values ({weather.warm}, {weather.mild}, {weather.cold}, {weather.no_preference}, {id_user});"""
    
    try:
        cursor.execute(action)
    except Exception:
        connection.close()
        return False
    else:
        connection.commit()
        connection.close()
        return True
    
