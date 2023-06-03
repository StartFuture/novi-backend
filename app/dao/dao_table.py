import mysql.connector

from models.models_table import Accomodation, Transport, Tour
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

def table_accommodation(accommodation: Accomodation):
    connection, cursor = connect_database(
        host=HOST, 
        user=USER, 
        password=PASSWORD, 
        database=DATABASE
    )

    insert_accommodation = f"""
    INSERT INTO accomodation 
    (id, travel_destination, travel_style, accommodation_style, is_country, warn, mild, cold, price, details, local_name) 
    VALUES
    (default, {accommodation.travel_destination}, {accommodation.travel_style}, {accommodation.accommodation_style}, {accommodation.is_country}, {accommodation.warn}, {accommodation.mild}, {accommodation.cold}, {accommodation.price}, '{accommodation.details}', {accommodation.local_name});    
    """

    cursor.execute()
    connection.commit()

    query = f"SELECT LAST_INSERT_ID() FROM accommodation"

    cursor.execute(query)
    id_accommodation = cursor.fetchone()

    return id_accommodation


def table_tour(tour: Tour):
    connection, cursor = connect_database(
        host=HOST, 
        user=USER, 
        password=PASSWORD, 
        database=DATABASE
    )

    insert_tour = f"""
    INSERT INTO tour
    (id, night_style, music_preference, building_preference, tradicion_preference, party_preference, water_preference, walk_preference, historic_preference, sport_preference, food_preference, id_accommodation, price, details)
    VALUES
    (default, {tour.night_style}, {tour.music_preference}, {tour.building_preference}, {tour.tradicion_preference}, {tour.party_preference}, {tour.water_preference}, {tour.historic_preference}, {tour.sport_preference}, {tour.food_preference}, {tour.id_accommodation}, {tour.price}, '{tour.details}')
    """

    
def table_transport(transport: Transport):
    connection, cursor = connect_database(
        host=HOST, 
        user=USER, 
        password=PASSWORD, 
        database=DATABASE
    )

    insert_transport = f"""
    INSERT INTO transport
    (id, details, price, transport_style)
    VALUES
    (default, '{transport.details}', {transport.price}, {transport.transport_style})
    """