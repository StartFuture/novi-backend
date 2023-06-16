import mysql.connector


from parameters import HOST, USER, PASSWORD, DATABASE, PORT
from dao.dao import connect_database


def verify_user_password(id_user: int):
    connection, cursor = connect_database(
        host=HOST,
        port=int(PORT),
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    query = f"""select password_user from `user` where id = {id_user};"""
    
    try:
        cursor.execute(query)
        result = cursor.fetchone()
    except Exception:
        connection.close()
        return None
    else:
        connection.close()
        return result



def update_password_user(id_user: int, new_password: str):
    connection, cursor = connect_database(
        host=HOST,
        port=int(PORT),
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    action = f"""UPDATE `user` SET password_user = '{new_password}' WHERE id = {id_user} ;"""
    
    try:
        cursor.execute(action)
    except Exception:
        connection.close()
        return False
    else:
        connection.commit()
        connection.close()
        return True
