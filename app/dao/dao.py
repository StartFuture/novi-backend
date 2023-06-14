from datetime import datetime

import mysql.connector
import pydantic

from parameters import HOST, USER, PASSWORD, DATABASE

from models.models_user import AddressUpdate, UserUpdate, user_review, User


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


def verify_user_exist_by_email(email: str):

    """Essa função tem como objetivo fazer uma consulta
    na tabela table_users para saber se existe um usuario com
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

    query = f"""select user, password_user from user where email = '{email}';"""

    cursor.execute(query)

    result = cursor.fetchone()
    connection.close()

    if result:
        return result
    else:
        return None


def verify_token_exist_by_id(id_user: int):
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

    query = f"""select id_token, date_expires, id_user from two_auth where id_user = '{id_user}';"""

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

    query = f"""update two_auth set date_expires = '{datetime.today().date()}' where id_user = '{id_user}';"""

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

    query = f"""insert into two_auth (id_user, date_expires) values ('{id_user}', '{datetime.today().date()}');"""

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

    query = f"""insert into two_auth (id_user, user_code, date_expires)
         values (default , {id_user}, {user_code}, "{datetime.today().date()}");"""

    cursor.execute(query)
    connection.commit()
    connection.close()


def insert_new_user_comment(user_name: str, perfil: str, stars: int, user_comment: str):
    connection, cursor = conect_database(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    action = f"""insert into ratings_comments (name_user, perfil, stars, user_comment, id_user)
                values ("{user_name}", "{perfil}", "{stars}", "{user_comment}");"""

    cursor.execute(action)
    connection.commit()

    query = f"""select name_user from ratings_comments where user_comment = "{user_comment}";"""

    cursor.execute(query)
    result = cursor.fetchone()

    connection.commit()
    connection.close()

    return bool(result)

  
def insert_review(user: user_review, id_user: int):
    connection, cursor = conect_database(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    action = f"""insert into ratings_comments (name_user, perfil, stars, user_comment, id_user) values
    ('{user.name_user}', '{user.perfil}', '{user.stars}', '{user.comment}', '{id_user}');"""
    
    try:
        cursor.execute(action)
    except Exception:
        connection.close()
        return False
    else:
        connection.commit()
        connection.close()
        return True
    

def update_review(id_user: int, user: user_review, id_review: int):
    connection, cursor = conect_database(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    action = f"""UPDATE ratings_comments SET user_comment='{user.comment}', stars={user.stars} WHERE id_user = {id_user} and id_review = {id_review};"""
    
    try:
        cursor.execute(action)
    except Exception:
        connection.close()
        return False
    else:
        connection.commit()
        connection.close()
        return True
    

def delete_review(id_review: int):
    connection, cursor = conect_database(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    action = f"""delete ratings_comments.* from ratings_comments where id_review={id_review} ;"""
    
    try:
        cursor.execute(action)
    except Exception:
        connection.close()
        return False
    else:
        connection.commit()
        connection.close()
        return True


def read_review(id_user: int):
    connection, cursor = conect_database(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    query = f"""select * from ratings_comments where id_user={id_user};"""
    
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
    

def read_all_review():
    connection, cursor = conect_database(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    query = f"""select * from ratings_comments;"""
    
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


def verify_user_exist_by_id_join_address(id_user: int):
    connection, cursor = conect_database(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    query = f"""select * from table_users join table_address where table_users.id_user = {id_user};"""
    
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
