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

    insert_accommodation = """
    INSERT INTO accomodation 
    (id, travel_destination, travel_style, accommodation_style, is_country, warn, mild, cold, price, details, local_name) 
    VALUES
    (default, {accommodation.travel_destination}, {accommodation.travel_style}, {accommodation.accommodation_style}, {accommodation.is_country}, {accommodation.warn}, {accommodation.mild}, {accommodation.cold}, {accommodation.price}, '{accommodation.details}', {accommodation.local_name});    
    """


def table_transport(transport: Transport):
    connection, cursor = connect_database(
        host=HOST, 
        user=USER, 
        password=PASSWORD, 
        database=DATABASE
    )

    insert_tour = """
    INSERT INTO tour
    (id, night_style, music_preference, building_preference, tradicion_preference, party_preference, water_preference, walk_preference, historic_preference, sport_preference, food_preference, id_accommodation, price, details)
    VALUES
    (default, {transport.night_style}, {transport.music_preference}, {transport.building_preference}, {transport.tradicion_preference}, {transport.party_preference}, {transport.water_preference}, {transport.historic_preference}, {transport.sport_preference}, {transport.food_preference}, {transport.id_accommodation}, {transport.price}, '{transport.details}')
    """

    
def table_transport(transport: Transport):
    connection, cursor = connect_database(
        host=HOST, 
        user=USER, 
        password=PASSWORD, 
        database=DATABASE
    )

    insert_transport = """
    INSERT INTO transport
    (id, details, price, transport_style)
    VALUES
    (default, '{tour.details}', {tour.price}, {tour.transport_style})
    """