import mysql.connector

from parameters import HOST, USER, PASSWORD, DATABASE

def connect_database(host, user, password, database):

    """Essa função tem como objetivo se conectar
    com o banco de dados"""

    connetion= mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database,

    )
    cursor = connetion.cursor(dictionary=True)

    return connetion, cursor

def table_accommodation(id, travel_destination, travel_style, accommodation_style, is_country, warn, mild, cold, price, details, local_name):
    connection, cursor = connect_database(
        host=HOST, 
        user=USER, 
        password=PASSWORD, 
        database=DATABASE
    )

    insert_accommodation = """
    INSERT (id, travel_destination, travel_style, accommodation_style, is_country, warn, mild, cold, price, details, local_name) 
    INTO accomodation 
    VALUES
    (default, {travel_destination},{travel_style}, {accommodation_style}, {is_country}, {warn}, {mild}, {cold}, {price}, '{details}', {local_name});    
    """


def table_transport(id, night_style, music_preference, building_preference, tradicion_preference, party_preference, water_preference, walk_preference, historic_preference, sport_preference, food_preference, id_accommodation, price, details):
    connection, cursor = connect_database(
        host=HOST, 
        user=USER, 
        password=PASSWORD, 
        database=DATABASE
    )

    insert_tour = """
    INSERT (id, night_style, music_preference, building_preference, tradicion_preference, party_preference, water_preference, walk_preference, historic_preference, sport_preference, food_preference, id_accommodation, price, details)
    INTO tour
    VALUES
    (default, {night_style}, {})
    """