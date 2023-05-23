import mysql.connector


from parameters import HOST, USER, PASSWORD, DATABASE

from models.models_travel_activities import travel_activities


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




#Crud atividades de preferencia do ususario
def insert_travel_activitie(activitie: travel_activities, id_user: int):
    print(HOST, USER, PASSWORD, DATABASE)
    connection, cursor = conect_database(
        host=HOST,
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
    

def update_tarvel_activities(activitie: travel_activities, id_user: int, id_activitie: int):
    connection, cursor = conect_database(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    action = f"""UPDATE travel_activities SET water_preference = {activitie.water_preference}, walk_preference = {activitie.walk_preference},
             historic_preference = {activitie.historic_preference}, sport_preference = {activitie.sport_preference}, food_preference = {activitie.food_preference} 
             WHERE id_activities= {id_activitie} and id_user = {id_user};"""
    
    try:
        print(action)
        cursor.execute(action)
    except Exception:
        connection.close()
        return False
    else:
        connection.commit()
        connection.close()
        return True
    

def delete_travel_activities(id_user: int, id_activitie: int):
    connection, cursor = conect_database(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    action = f"""delete travel_activities.* from travel_activities where id_activities = {id_activitie} and id_user = {id_user} ;"""
    
    try:
        cursor.execute(action)
    except Exception:
        connection.close()
        return False
    else:
        connection.commit()
        connection.close()
        return True


def read_travel_activitie(id_activitie: int):
    connection, cursor = conect_database(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    query = f"""select * from travel_activities where id_activities = {id_activitie};"""
    
    try:
        cursor.execute(query)
        result = cursor.fetchall()
    except Exception:
        connection.close()
        return False
    else:
        connection.commit()
        connection.close()
        return result
    

def read_all_travel_activities():
    connection, cursor = conect_database(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    query = f"""select * from travel_activities;"""
    
    try:
        cursor.execute(query)
        result = cursor.fetchall()
    except Exception:
        connection.close()
        return False
    else:
        connection.commit()
        connection.close()
        return result
