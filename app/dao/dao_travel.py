import mysql.connector
import pydantic

from parameters import HOST, USER, PASSWORD, DATABASE
from models.models_travel import Travel


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

async def new_travel(id_user: int, id_accommodation: int, id_transport_from: int , id_transport_return: int, date_from: str, date_return: str, quantity_people: int, price: float):
    connection, cursor = connect_database(
        host=HOST, 
        user=USER, 
        password=PASSWORD, 
        database=DATABASE
    )

    create_travel = f"""
    INSERT INTO travel
    (id_user, id_accommodation, id_transport_from, id_transport_return, date_from, date_return, quantity_people, price)
    VALUES
    ({id_user}, {id_accommodation}, {id_transport_from}, {id_transport_return}, '{date_from}', '{date_return}', {quantity_people}, {price})
    """

    cursor.execute(create_travel)
    connection.commit()

    query = f"SELECT "

    connection.close()

    return {'message': 'Travel Created Succesfully'}
