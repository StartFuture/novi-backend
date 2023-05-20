import mysql.connector
import pydantic

from parameters import HOST, USER, PASSWORD, DATABASE
from models.models_destinations import  Destination, UpdateDestination

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


async def write_data_destination(destination: Destination):
    connection, cursor = connect_database(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    values = ', '.join([f"'{value}'" for value in destination])
    #create_destination = f"INSERT INTO table_destinations (id_destination, continent, country, state_destination, city, journey) VALUES (default, {values})"
    create_destination = f"INSERT INTO table_destinations (id_destination, continent, country, state_destination, city, journey) VALUES (default, " + ", ".join([f"'{value}'" for value in destination.dict().values()]) + ")"
    print(create_destination)

    cursor.execute(create_destination)
    connection.commit()
    connection.close()

    return {'message': 'Destination created successfully'}


async def verify_duplicated_data(destination: Destination):
    connection, cursor = connect_database(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    values = " AND ".join([f"{field} = '{value}'" for field, value in destination])
    query = f"SELECT continent, country, state_destination, city, journey FROM table_destinations WHERE " + values

    cursor.execute(query)
    result = cursor.fetchone()
    connection.close()

    return bool(result)


async def select_data_destination(id_destination:int):
    connection, cursor = connect_database(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    query = f"SELECT * FROM table_destinations WHERE id_destination = {id_destination}"

    cursor.execute(query)
    query_destination = cursor.fetchone()

    query = f"SELECT id_destination FROM table_destinations WHERE id_destination = {id_destination}"

    cursor.execute(query)
    result = cursor.fetchone()
    connection.close()

    return query_destination, bool(result)


async def update_data_destination(id_destination: int, destination: UpdateDestination):
    connection, cursor = connect_database(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    if any(value is not None for _, value in destination):
        values = ", ".join(f" {field} = '{value}' " for field, value in destination if value is not None)
        update_destination = f"UPDATE table_destinations SET" + values + f"WHERE id_destination = {id_destination}"
        
        cursor.execute(update_destination)
        connection.commit()
    else:
        update_destination = False
    
    connection.close()

    return update_destination, {'message': 'Destination updated sucessfully'}

async def verify_id_destination(id_destination: int):
    connection, cursor = connect_database(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )
    query = f"SELECT id_destination FROM table_destinations WHERE id_destination = {id_destination}"

    cursor.execute(query)
    verify_id = cursor.fetchone()
    connection.close()

    return bool(verify_id)


async def delete_data_destination(id_destination: int):
    connection, cursor = connect_database(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    delete_destination = f"DELETE table_destinations.* FROM table_destinations WHERE id_destination = {id_destination}"

    cursor.execute(delete_destination)
    connection.commit()
    connection.close()

    return {'message': 'Destination deleted successfully'}
