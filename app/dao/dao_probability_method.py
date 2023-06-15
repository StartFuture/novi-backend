import mysql.connector


from parameters import HOST, USER, PASSWORD, DATABASE



def conect_database(host, user, password, database):

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


def get_user_questions(id_user: int):
    connection, cursor = conect_database(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    query = f"""select * from `user` as u
                left join weather_option as wo on u.id = wo.id_user
                left join travel_activities as ta on u.id = ta.id_user
                left join travel_options as t_o on u.id = t_o.id_user
                left join travel_cultures as tc on u.id = tc.id_user
                where u.id = {id_user};"""
    
    try:
        cursor.execute(query)
        result = cursor.fetchone()
    except Exception:
        connection.close()
        return False
    else:
        connection.close()
        return result
    

def get_travels():
    connection, cursor = conect_database(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    query = f"""select * from accommodation;"""
    
    try:
        cursor.execute(query)
        result = cursor.fetchall()
    except Exception:
        connection.close()
        return False
    else:
        connection.close()
        return result
    

def get_tour_travel(id_accommodation: int):
    connection, cursor = conect_database(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    query = f"""select * from tour where id_accommodation = {id_accommodation};"""
    
    try:
        cursor.execute(query)
        result = cursor.fetchall()
    except Exception:
        connection.close()
        return False
    else:
        connection.close()
        return result
    

def get_transport_and_tours_travel(id_accommodation: int):
    connection, cursor = conect_database(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    query = f"""select t.id as id_tour,
                                night_style, music_preference, building_preference,
                                tradicion_preference, party_preference, water_preference, walk_preference,
                                historic_preference, sport_preference, food_preference,
                                tr.details as details_transport, tr.id as id_transport, t.id_accommodation, t.details as details_tour,
                                transport_style, t.price as tour_price, tr.price as transport_price from `tour` as t
                left join transport as tr on t.id_accommodation = tr.id_accommodation
                where tr.id_accommodation = {id_accommodation};"""
    
    try:
        cursor.execute(query)
        result = cursor.fetchall()
    except Exception:
        connection.close()
        return False
    else:
        connection.close()
        return result
    

def get_travel_data(transport_style: int):
    connection, cursor = conect_database(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    query = f"""select * from `tour` as t
            left join accommodation as ac on t.id_accommodation = ac.id
            left join transport as tr on t.id_accommodation = tr.id_accommodation
            where tr.transport_style = {transport_style};"""
    
    try:
        cursor.execute(query)
        result = cursor.fetchall()
    except Exception:
        connection.close()
        return False
    else:
        connection.close()
        return result
    

def get_travel_abroad():
    connection, cursor = conect_database(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    query = f"""select * from accommodation where is_country = 0;"""
    
    try:
        cursor.execute(query)
        result = cursor.fetchall()
    except Exception:
        connection.close()
        return False
    else:
        connection.close()
        return result
    

