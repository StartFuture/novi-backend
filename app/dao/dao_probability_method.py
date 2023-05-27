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

    query = f"""select * from table_users as tu
            left join weather_option as wo on tu.id_user = wo.id_user
            left join travel_activities as ta on tu.id_user = ta.id_user
            left join travel_options as t_o on tu.id_user = t_o.id_user
            left join travel_cultures as tc on tu.id_user = tc.id_user
            where tu.id_user = {id_user};"""
    
    try:
        cursor.execute(query)
        result = cursor.fetchone()
    except Exception:
        connection.close()
        return False
    else:
        connection.close()
        return result