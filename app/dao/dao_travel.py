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

def new_travel(id_user: int, id_accommodation: int, id_transport_from: int , id_transport_return: int, date_from: str, date_return: str, quantity_people: int, price: float):
    connection, cursor = connect_database(
        host=HOST, 
        user=USER, 
        password=PASSWORD, 
        database=DATABASE
    )

    create_travel = f"""
    INSERT INTO travel
    (id, id_user, id_accommodation, id_transport_from, id_transport_return, date_from, date_return, quantity_people, price)
    VALUES
    (default, {id_user}, {id_accommodation}, {id_transport_from}, {id_transport_return}, '{date_from}', '{date_return}', {quantity_people}, {price})
    """

    cursor.execute(create_travel)
    connection.commit()

    query = f"SELECT LAST_INSERT_ID() FROM travel;"

    cursor.execute(query)
    id_travel = cursor.fetchone()
    connection.close()

    return id_travel, {'message': 'Travel Created Succesfully'}

def new_travel_tour(id_travel: int, id_tour: int):
    connection, cursor = connect_database(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    create_travel_tour = f"""
    INSERT INTO traveltour
    (id, id_travel, id_tour)
    VALUES
    (default, {id_travel}, {id_tour})
    """

    cursor.execute(create_travel_tour)
    connection.commit()
    connection.close()

    return {'message': 'TravelTour Created Succesfully'}


def select_history(id_user: int):
    connection, cursor = connect_database(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    query = f"""
    SELECT DISTINCT t.date_from, t.quantity_people, a.travel_destination, a.local_name
    FROM travel t
    LEFT JOIN accommodation a on a.id = t.id_accommodation 
    WHERE id_user = {id_user} AND date_from < CURRENT_DATE AND date_return < CURRENT_DATE
    ORDER BY date_from DESC
    LIMIT 3;
    """

    cursor.execute(query)
    query_travel = cursor.fetchall()
    connection.close()

    return query_travel
