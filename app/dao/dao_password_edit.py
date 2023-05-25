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


def verify_user_password(id_user: int, current_password: str):
    connection, cursor = conect_database(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )
    query = f"""select password_user from table_users where id_user = {id_user} and password_user = '{current_password}';"""
    
    try:
        cursor.execute(query)
        result = cursor.fetchone()
        if result['password_user'] == current_password:
            result = True
        else:
            result = False
    except Exception:
        connection.close()
        return False
    else:
        connection.commit()
        connection.close()
        return result



def update_password_user(id_user: int, new_password: str):
    connection, cursor = conect_database(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    action = f"""UPDATE table_users SET password_user='{new_password}' WHERE id_user = {id_user} ;"""
    
    try:
        cursor.execute(action)
    except Exception:
        connection.close()
        return False
    else:
        connection.commit()
        connection.close()
        return True