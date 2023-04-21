import os

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

def select_all():
    connection,cursor = conect_database(host=HOST, user=USER, password=PASSWORD, database=DATABASE)
    query = """SELECT * FROM users;"""
    cursor.execute(query)
    user_list = cursor.fetchall()
    return user_list


async def insert_new_line_user(name_user: str, last_name: str, date_birth: str, email: str, cpf: str, cellphone: str, id_address: int, password_user: str, news: bool, info_conditions:bool):
    connection,cursor = conect_database(host=HOST, user=USER, password=PASSWORD, database=DATABASE)   
    create_user = f"""
    INSERT INTO users 
    (name_user, last_name, date_birth, email, cpf, cellphone, id_address, password_user, news, info_conditions) 
    VALUES 
    ('{name_user}', '{last_name}', '{date_birth}', '{email}', '{cpf}', '{cellphone}', '{id_address}', '{password_user}', {news}, {info_conditions});"""
    cursor.execute(create_user)

    connection.commit()
    connection.close()
    return {'message': 'User created successfully'}

async def insert_new_line_address(cep: str, state_user: str, city: str, address_user: str, address_number: str, complements: str):
    connection,cursor = conect_database(host=HOST, user=USER, password=PASSWORD, database=DATABASE)
    # if cep is None:
    #     cep = ''
    # if state_user is None:
    #     state_user = ''
    # if city is None:
    #     city = ''
    # if address_user is None:
    #     address_user = ''
    # if address_number is None:
    #     address_number = ''
    # if complements is None:
    #     complements = ''
    create_address = f"""
    INSERT INTO address
    (id_address, cep, state_user, city, address_user, address_number, complements)
    VALUES
    (default, '{cep}', '{state_user}', '{city}', '{address_user}', '{address_number}', '{complements}');"""
    cursor.execute(create_address)
    connection.commit()
    query = f"""SELECT LAST_INSERT_ID() FROM address;"""
    cursor.execute(query)
    result = cursor.fetchone()
    connection.close()

    return result

async def update_line_users(id_user: str,name_user: str, last_name: str, email: str, cpf: str, cellphone: str, id_address: int, password_user: str, news: bool):
    connection,cursor = conect_database(host=HOST, user=USER, password=PASSWORD, database=DATABASE)
    update_user = f"""
    UPDATE users 
    SET 
    name_user='{name_user}',
    last_user='{last_name}',
    email='{email}', 
    cpf='{cpf}', 
    cellphone='{cellphone}', 
    password_user='{password_user}', 
    news={news}
    WHERE user_id = {id_user}"""
    cursor.execute(update_user)
    connection.commit()
    connection.close()

def verify_cpf(cpf: str):
    connection,cursor = conect_database(host=HOST, user=USER, password=PASSWORD, database=DATABASE)
    query = f"""SELECT cpf FROM users WHERE cpf = '{cpf}';"""
    cursor.execute(query)
    result = cursor.fetchone()
    connection.close()
    return result is not None

def verify_email(email: str):
    connection,cursor = conect_database(host=HOST, user=USER, password=PASSWORD, database=DATABASE)
    query = f"""SELECT cpf FROM users WHERE email = '{email}';"""
    cursor.execute(query)
    result = cursor.fetchone()
    connection.close()
    return result is not None
