from datetime import datetime

import mysql.connector
import pydantic

from parameters import HOST, USER, PASSWORD, DATABASE
from models.user_model import  AddressUpdate, UserUpdate

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


def select_all():
    connection,cursor = conect_database(
        host=HOST, 
        user=USER, 
        password=PASSWORD, 
        database=DATABASE
    )
    query = "SELECT * FROM users;"

    cursor.execute(query)
    user_list = cursor.fetchall()
    connection.close()

    return user_list


async def select_user(id_user: int):
    connection,cursor = conect_database(
        host=HOST, 
        user=USER, 
        password=PASSWORD, 
        database=DATABASE
    )

    query_id = f"SELECT * FROM users WHERE id_user = {id_user}"

    cursor.execute(query_id)
    query_user = cursor.fetchone()

    query_id_address = f"SELECT id_address FROM users WHERE id_user = {id_user}"
    cursor.execute(query_id_address)
    id_address = cursor.fetchone()
    connection.close()

    return query_user, id_address


async def select_address(id_address: int):
    connection,cursor = conect_database(
        host=HOST, 
        user=USER, 
        password=PASSWORD, 
        database=DATABASE
    )

    query = f"SELECT * FROM address WHERE id_address = {id_address['id_address']}"

    cursor.execute(query)
    query_address = cursor.fetchone()
    connection.close()

    return query_address
    

async def insert_new_line_address(cep: str, state_user: str, city: str, address_user: str, address_number: str, complements: str):
    connection,cursor = conect_database(
        host=HOST, 
        user=USER, 
        password=PASSWORD, 
        database=DATABASE
    )

    create_address = f"""
    INSERT INTO address
    (id_address, cep, state_user, city, address_user, address_number, complements)
    VALUES
    (default, '{cep}', '{state_user}', '{city}', '{address_user}', '{address_number}', '{complements}');"""
    
    cursor.execute(create_address)
    connection.commit()

    query = f"SELECT LAST_INSERT_ID() FROM address;"

    cursor.execute(query)
    result = cursor.fetchone()
    connection.close()

    return result, {'message': 'Address created successfully'}


async def insert_new_line_user(name_user: str, last_name: str, date_birth: str, email: str, cpf: str, cellphone: str, id_address: int, password_user: str, news: bool, info_conditions:bool):
    connection,cursor = conect_database(
        host=HOST, 
        user=USER, 
        password=PASSWORD, 
        database=DATABASE
    )

    create_user = f"""
    INSERT INTO users 
    (name_user, last_name, date_birth, email, cpf, cellphone, id_address, password_user, news, info_conditions) 
    VALUES 
    ('{name_user}', '{last_name}', '{date_birth}', '{email}', '{cpf}', '{cellphone}', {id_address}, '{password_user}', {news}, {info_conditions});"""
    
    cursor.execute(create_user)

    connection.commit()
    connection.close()

    return {'message': 'User created successfully'}


async def verify_data_overwrite(cpf: str, email: str):
    connection,cursor = conect_database(
        host=HOST, 
        user=USER, 
        password=PASSWORD, 
        database=DATABASE
    )

    query_cpf = f"SELECT cpf FROM users WHERE cpf = '{cpf}';"

    cursor.execute(query_cpf)
    result_cpf = cursor.fetchone()

    query_email = f"SELECT email FROM users WHERE email= '{email}'"

    cursor.execute(query_email)
    result_email = cursor.fetchone()
    connection.close()

    return bool(result_cpf), bool(result_email)


async def verify_email(email: str):
    connection,cursor = conect_database(
        host=HOST, 
        user=USER, 
        password=PASSWORD, 
        database=DATABASE
    )

    query = f"SELECT email FROM users WHERE email = '{email}';"

    cursor.execute(query)
    result = cursor.fetchone()
    connection.close()

    return result is not None


# Atualização de dados do usuário
async def update_line_users(id_user: int, name_user: str, last_name: str, email: str, cpf: str, cellphone: str, password_user: str, user: UserUpdate):
    connection,cursor = conect_database(
        host=HOST, 
        user=USER, 
        password=PASSWORD, 
        database=DATABASE
    )

    update_user = f"UPDATE users SET" + ", ".join(f" {field} = '{value}' " for field, value in user if value is not None) + f"WHERE id_user = {id_user}"

    cursor.execute(update_user)
    connection.commit()

    if last_name is not None:
        update_last_name = f"UPDATE users SET last_name = '{last_name}' WHERE id_user = {id_user}"
        cursor.execute(update_last_name)
        connection.commit()

    query = f"SELECT id_address FROM users WHERE id_user = {id_user}"

    cursor.execute(query)
    result = cursor.fetchone()
    connection.close()

    return result, {'message': 'User updated successfully'}


# Atualização do dado news
async def update_line_users_news(id_user: int, news: bool):
    connection,cursor = conect_database(
        host=HOST, 
        user=USER, 
        password=PASSWORD, 
        database=DATABASE
    )

    update_news = f"UPDATE users SET news = {news} WHERE id_user = {id_user}"

    cursor.execute(update_news)
    connection.commit()
    connection.close()
    
    return {'message': 'User news updated successfully'}


# Atualização de dados de address
async def update_line_address(id_address: int, cep: str, state_user: str, city: str, address_user: str, address_number: str, complements: str, address: AddressUpdate):
    connection,cursor = conect_database(
        host=HOST, 
        user=USER, 
        password=PASSWORD, 
        database=DATABASE
    )

    update_address = f"UPDATE address SET" + ", ".join(f" {field} = '{value}' " for field, value in address if value is not None) + f"WHERE id_address = {id_address}"

    cursor.execute(update_address)
    connection.commit()
    connection.close()

    return {'message': 'Address updated successfully'}


# Verifica a existência do usuário
async def verify_user_exist(id_user: int):
    connection,cursor = conect_database(
        host=HOST, 
        user=USER, 
        password=PASSWORD, 
        database=DATABASE
    )

    query = f"SELECT id_user FROM users WHERE id_user = {id_user}"

    cursor.execute(query)
    result = cursor.fetchone()
    connection.close()

    return bool(result)


async def verify_data_users(id_user: int, cpf: str, email: str):
    connection,cursor = conect_database(
        host=HOST, 
        user=USER, 
        password=PASSWORD, 
        database=DATABASE
    )

    query_cpf = f"SELECT cpf FROM users WHERE cpf = '{cpf}' AND id_user <> {id_user}"

    cursor.execute(query_cpf)
    result_cpf = cursor.fetchone()

    query_email = f"SELECT email FROM users WHERE email = '{email}' AND id_user <> {id_user}"

    cursor.execute(query_email)
    result_email = cursor.fetchone()
    connection.close()
    
    return bool(result_cpf), bool(result_email)



