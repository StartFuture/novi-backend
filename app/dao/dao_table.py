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
