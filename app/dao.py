from datetime import datetime

import mysql.connector
import pydantic


HOST = 'localhost'
USER = 'root'
PASSWORD = ''
DATABASE = 'two_auth'


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




def verify_user_exist(email: str):

    """Essa função tem como objetivo fazer uma consulta
    na tabela users para saber se existe um usuario com
     o mesmo email que foi adicionado na variavel email.
     Se existe um usuario com email correspondente,
      retorna-se o id do usuario e sua senha porem se
      não retorna um valor vazio."""

    connection, cursor = conect_database(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    query = f"""select id_user, password_user from users where email = '{email}';"""

    cursor.execute(query)

    result = cursor.fetchone()
    connection.close()

    if result:
        return result
    else:
        return None



def verify_token_exist(id_user: int):
    """Essa função tem como objetivo fazer uma consulta
    na tabela two_auth para saber se existe a um token
    correspondente a chave estrangeira id_user.
    Se existe ,retorna-se  id_token, user_token e
    create_date porem se não retorna um valor vazio."""

    connection, cursor = conect_database(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    query = f"""select id_token, date_experience, id_user from two_auth where id_user = '{id_user}';"""

    cursor.execute(query)

    result = cursor.fetchone()
    connection.close()

    if result:
        return result
    else:
        return None




def verify_token_is_revoked(id_token: int):
    """Essa função verifica se o token do usuario
    esta revogado retornando um valor bool(boleano)."""

    connection, cursor = conect_database(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    query = f"""select id_token from revoked_token where id_token = '{id_token}';"""

    cursor.execute(query)

    result = cursor.fetchone()
    connection.close()

    return bool(result)



def insert_revoked_token(id_token: int, id_user: int):
    connection, cursor = conect_database(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    query = f"""insert into revoked_token (id_user, id_token) values ({id_user}, {id_token});"""

    cursor.execute(query)
    connection.commit()
    connection.close()



def update_token(id_user: int):
    connection, cursor = conect_database(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    query = f"""update two_auth set date_experience = '{datetime.today().date()}' where id_user = '{id_user}';"""

    cursor.execute(query)
    connection.commit()
    connection.close()



def insert_new_token_and_code(id_user: int):
    connection, cursor = conect_database(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    query = f"""insert into two_auth (id_user, date_experience) values ('{id_user}', '{datetime.today().date()}');"""

    cursor.execute(query)
    connection.commit()
    connection.close()



def insert_new_code(id_user: int, user_code: int,):
    connection, cursor = conect_database(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    query = f"""insert into two_auth (id_user, user_code, date_experience)
         values (default , {id_user}, {user_code}, "{datetime.today().date()}");"""

    cursor.execute(query)
    connection.commit()
    connection.close()



def delete_user_by_id(id_user: int):
    connection, cursor = conect_database(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    action = f"""delete users.* from users where id_user = "{id_user}";"""

    cursor.execute(action)
    connection.commit()

    query = f"""select id_user from users where id_user = "{id_user}";"""

    cursor.execute(query)
    result = cursor.fetchone()
    connection.commit()
    connection.close()

    return not bool(result)






