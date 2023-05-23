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


# Seleciona id_address e id_user
async def select_user(id_user: int):
    connection,cursor = conect_database(
        host=HOST, 
        user=USER, 
        password=PASSWORD, 
        database=DATABASE
    )

    query_id = f"SELECT * FROM table_users WHERE id_user = {id_user}"

    cursor.execute(query_id)
    query_user = cursor.fetchone()

    query_id_address = f"SELECT id_address FROM table_users WHERE id_user = {id_user}"

    cursor.execute(query_id_address)
    id_address = cursor.fetchone()
    connection.close()

    return query_user, id_address


# Seleciona id_address
async def select_address(id_address: int):
    connection,cursor = conect_database(
        host=HOST, 
        user=USER, 
        password=PASSWORD, 
        database=DATABASE
    )

    query = f"SELECT * FROM table_address WHERE id_address = {id_address}"

    cursor.execute(query)
    query_address = cursor.fetchone()
    connection.close()

    return query_address
    

# Adiciona uma nova linha a tabela address
async def insert_new_line_address(cep: str, state_user: str, city: str, address_user: str, address_number: str, complements: str):
    connection,cursor = conect_database(
        host=HOST, 
        user=USER, 
        password=PASSWORD, 
        database=DATABASE
    )

    create_address = f"""
    INSERT INTO table_address
    (id_address, cep, state_user, city, address_user, address_number, complements)
    VALUES
    (default, '{cep}', '{state_user}', '{city}', '{address_user}', '{address_number}', '{complements}');"""
    
    cursor.execute(create_address)
    connection.commit()

    query = f"SELECT LAST_INSERT_ID() FROM table_address;"

    cursor.execute(query)
    result = cursor.fetchone()
    connection.close()

    return result, {'message': 'Address created successfully'}


# Adiciona uma nova linha a tabela user
async def insert_new_line_user(name_user: str, last_name: str, date_birth: str, email: str, cpf: str, cellphone: str, id_address: int, password_user: str, news: bool, info_conditions:bool, share_data:bool):
    connection,cursor = conect_database(
        host=HOST, 
        user=USER, 
        password=PASSWORD, 
        database=DATABASE
    )

    create_user = f"""
    INSERT INTO table_users 
    (name_user, last_name, date_birth, email, cpf, cellphone, id_address, password_user, news, info_conditions, share_data) 
    VALUES 
    ('{name_user}', '{last_name}', '{date_birth}', '{email}', '{cpf}', '{cellphone}', {id_address}, '{password_user}', {news}, {info_conditions}, {share_data});"""
    
    cursor.execute(create_user)

    connection.commit()
    connection.close()

    return {'message': 'User created successfully'}


# Verifica cpf
async def verify_data_overwrite(cpf: str, email: str):
    connection,cursor = conect_database(
        host=HOST, 
        user=USER, 
        password=PASSWORD, 
        database=DATABASE
    )

    query_cpf = f"SELECT cpf FROM table_users WHERE cpf = '{cpf}';"

    cursor.execute(query_cpf)
    result_cpf = cursor.fetchone()

    query_email = f"SELECT email FROM table_users WHERE email= '{email}'"

    cursor.execute(query_email)
    result_email = cursor.fetchone()
    connection.close()

    return bool(result_cpf), bool(result_email)


# Verifica email
async def verify_email(email: str):
    connection,cursor = conect_database(
        host=HOST, 
        user=USER, 
        password=PASSWORD, 
        database=DATABASE
    )

    query = f"SELECT email FROM table_users WHERE email = '{email}';"

    cursor.execute(query)
    result = cursor.fetchone()
    connection.close()

    return result is not None


# Atualização de dados do usuário
async def update_line_users(id_user: int, last_name: str, user: UserUpdate):
    connection,cursor = conect_database(
        host=HOST, 
        user=USER, 
        password=PASSWORD, 
        database=DATABASE
    )
    if any(value is not None for _, value in user):
        update_user = f"UPDATE table_users SET" + ", ".join(f" {field} = '{value}' " for field, value in user if value is not None) + f"WHERE id_user = {id_user}"

        cursor.execute(update_user)
        connection.commit()
    
    if last_name is not None:
        update_last_name = f"UPDATE table_users SET last_name = '{last_name}' WHERE id_user = {id_user}"
        
        cursor.execute(update_last_name)
        connection.commit()

    query = f"SELECT id_address FROM table_users WHERE id_user = {id_user}"

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

    update_news = f"UPDATE table_users SET news = {news} WHERE id_user = {id_user}"

    cursor.execute(update_news)
    connection.commit()
    connection.close()
    
    return {'message': 'User news updated successfully'}


# Atualização de dados de address
async def update_line_address(id_address: int, address: AddressUpdate):
    connection,cursor = conect_database(
        host=HOST, 
        user=USER, 
        password=PASSWORD, 
        database=DATABASE
    )

    if any(value is not None for _, value in address):
        update_address = f"UPDATE table_address SET" + ", ".join(f" {field} = '{value}' " for field, value in address if value is not None) + f"WHERE id_address = {id_address}"

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

    query = f"SELECT id_user FROM table_users WHERE id_user = {id_user}"

    cursor.execute(query)
    result = cursor.fetchone()
    connection.close()

    return bool(result)


# Verifica cpf execeto do usuário que terá o update
async def verify_data_users(id_user: int, cpf: str, email: str):
    connection,cursor = conect_database(
        host=HOST, 
        user=USER, 
        password=PASSWORD, 
        database=DATABASE
    )

    query_cpf = f"SELECT cpf FROM table_users WHERE cpf = '{cpf}' AND id_user <> {id_user}"

    cursor.execute(query_cpf)
    result_cpf = cursor.fetchone()

    query_email = f"SELECT email FROM table_users WHERE email = '{email}' AND id_user <> {id_user}"

    cursor.execute(query_email)
    result_email = cursor.fetchone()
    connection.close()
    
    return bool(result_cpf), bool(result_email)