import os

import mysql.connector

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


def select_all():
    connection,cursor = conect_database(host=HOST, user=USER, password=PASSWORD, database=DATABASE)
    query = "SELECT * FROM users;"
    cursor.execute(query)
    user_list = cursor.fetchall()
    connection.close()

    return user_list


async def insert_new_line_user(name_user: str, last_name: str, date_birth: str, email: str, cpf: str, cellphone: str, id_address: int, password_user: str, news: bool, info_conditions:bool):
    connection,cursor = conect_database(host=HOST, user=USER, password=PASSWORD, database=DATABASE)   
    create_user = f"""
    INSERT INTO users 
    (name_user, last_name, date_birth, email, cpf, cellphone, id_address, password_user, news, info_conditions) 
    VALUES 
    ('{name_user}', '{last_name}', '{date_birth}', '{email}', '{cpf}', '{cellphone}', {id_address}, '{password_user}', {news}, {info_conditions});"""
    cursor.execute(create_user)

    connection.commit()
    connection.close()

    return {'message': 'User created successfully'}


async def insert_new_line_address(cep: str, state_user: str, city: str, address_user: str, address_number: str, complements: str):
    connection,cursor = conect_database(host=HOST, user=USER, password=PASSWORD, database=DATABASE)
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


async def verify_cpf(cpf: str):
    connection,cursor = conect_database(host=HOST, user=USER, password=PASSWORD, database=DATABASE)
    query = f"SELECT cpf FROM users WHERE cpf = '{cpf}';"
    cursor.execute(query)
    result = cursor.fetchone()
    connection.close()

    return result is not None


async def verify_email(email: str):
    connection,cursor = conect_database(host=HOST, user=USER, password=PASSWORD, database=DATABASE)
    query = f"SELECT email FROM users WHERE email = '{email}';"
    cursor.execute(query)
    result = cursor.fetchone()
    connection.close()

    return result is not None


# Atualização de dados do usuário
async def update_line_users(id_user: int, name_user: str, last_name: str, email: str, cpf: str, cellphone: str, password_user: str, user: UserUpdate):
    connection,cursor = conect_database(host=HOST, user=USER, password=PASSWORD, database=DATABASE)
    update_user = f"UPDATE users SET" + ", ".join(f" {field} = '{value}' " for field, value in user if value is not None) + f"WHERE id_user = {id_user}"
    cursor.execute(update_user)
    connection.commit()
    if last_name is not None:
        update_last_name = f"UPDATE users SET last_name = '{last_name}' WHERE id_user = {id_user}"
        cursor.execute(update_last_name)
        connection.commit()
    query = f"""SELECT id_address FROM users WHERE id_user = {id_user}"""
    cursor.execute(query)
    result = cursor.fetchone()
    connection.close()

    return result, {'message': 'User updated successfully'}

# Atualização do dado news
async def update_line_users_news(id_user: int, news: bool):
    connection,cursor = conect_database(host=HOST, user=USER, password=PASSWORD, database=DATABASE)
    update_news = f"UPDATE users SET news = {news} WHERE id_user = {id_user}"
    cursor.execute(update_news)
    connection.commit()
    connection.close()
    
    return {'message': 'User news updated successfully'}

# Atualização de dados de address
async def update_line_address(id_address: int, cep: str, state_user: str, city: str, address_user: str, address_number: str, complements: str, address: AddressUpdate):
    connection,cursor = conect_database(host=HOST, user=USER, password=PASSWORD, database=DATABASE)
    update_address = f"UPDATE address SET" + ", ".join(f" {field} = '{value}' " for field, value in address if value is not None) + f"WHERE id_address = {id_address}"
    cursor.execute(update_address)
    connection.commit()
    connection.close()

    return {'message': 'Address updated successfully'}

# Verifica a existência do usuário
async def verify_user_exist(id_user: int):
    connection,cursor = conect_database(host=HOST, user=USER, password=PASSWORD, database=DATABASE)
    query = f"""SELECT id_user FROM users WHERE id_user = {id_user}"""
    cursor.execute(query)
    result = cursor.fetchone()
    connection.close()

    return result is not None

async def verify_data_users(id_user: int, cpf: str, email: str):
    connection,cursor = conect_database(host=HOST, user=USER, password=PASSWORD, database=DATABASE)
    query_cpf = f"""SELECT cpf FROM users WHERE cpf = '{cpf}' AND id_user <> {id_user}"""
    cursor.execute(query_cpf)
    result_cpf = cursor.fetchone()
    query_email = f"""SELECT email FROM users WHERE email = '{email}' AND id_user <> {id_user}"""
    cursor.execute(query_email)
    result_email = cursor.fetchone()
    connection.close()
    
    return result_cpf is not None, result_email is not None
