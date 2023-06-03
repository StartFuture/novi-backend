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

def next_travel(id_user: int):
    connection, cursor = connect_database(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    query = f"""
    SELECT tl.id as id_travel, 
	      tl.id_accommodation, 
          tl.id_transport_from,
          tl.id_transport_return, 
          tl.date_from, 
          tl.quantity_people, 
          t.id as id_transport, 
          t.transport_style,
          t.details as transport_details,
          a.id as id_accommodation,
          a.travel_destination,
          t2.id_tour,
          t3.details as tour_details
	FROM travel tl 
    LEFT JOIN transport t ON tl.id_transport_from = t.id
    LEFT JOIN accommodation a ON a.id = tl.id_accommodation 
    LEFT JOIN traveltour t2 ON t2.id_travel = tl.id 
    LEFT JOIN tour t3 ON t3.id = t2.id_tour 
    WHERE date_from > CURDATE() AND id_user = 1
    ORDER BY date_from;
    """

    cursor.execute(query)
    query_next_travel = cursor.fetchall()

    return query_next_travel