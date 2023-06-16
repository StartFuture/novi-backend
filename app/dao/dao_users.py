from datetime import datetime

from parameters import HOST, USER, PASSWORD, DATABASE, PORT
from models.models_user import  AddressUpdate, UserUpdate
from dao.dao import connect_database


# Deleta linha de usuário por id
def delete_user_by_id(id_user: int):
    connection, cursor = connect_database(
        host=HOST,
        port=int(PORT),
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    action = f"DELETE user.* from user where id = {id_user}"

    cursor.execute(action)
    connection.commit()

    query = f"select id from user where id = {id_user}"

    cursor.execute(query)
    result = cursor.fetchone()
    connection.commit()
    connection.close()

    return not bool(result)


# Seleciona todos os usuários
def select_all():
    connection, cursor = connect_database(
        host=HOST,
        port=int(PORT),
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )
    
    query = "SELECT * FROM user"

    cursor.execute(query)
    user_list = cursor.fetchall()
    connection.close()

    return user_list


# Seleciona id_address e id_user
async def select_user(id_user: int):
    connection, cursor = connect_database(
        host=HOST,
        port=int(PORT),
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    query_id = f"SELECT * FROM user WHERE id = {id_user}"

    cursor.execute(query_id)
    query_user = cursor.fetchone()

    query_id_address = f"SELECT id_address FROM user WHERE id = {id_user}"

    cursor.execute(query_id_address)
    id_address = cursor.fetchone()
    connection.close()

    return query_user, id_address


# Seleciona id_address
async def select_address(id_address: int):
    connection, cursor = connect_database(
        host=HOST,
        port=int(PORT),
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    query = f"SELECT * FROM `address` WHERE id = {id_address}"

    cursor.execute(query)
    query_address = cursor.fetchone()
    connection.close()

    return query_address
    

# Adiciona uma nova linha a tabela address
async def insert_new_line_address(cep: str, state_user: str, city: str, address_user: str, address_number: str, complements: str):
    connection, cursor = connect_database(
        host=HOST,
        port=int(PORT),
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    create_address = f"""
    INSERT INTO `address`
    (id, cep, state_user, city, address_user, address_number, complements)
    VALUES
    (default, '{cep}', '{state_user}', '{city}', '{address_user}', '{address_number}', '{complements}');"""
    
    cursor.execute(create_address)
    connection.commit()

    query = f"SELECT LAST_INSERT_ID() FROM `address`;"

    cursor.execute(query)
    result = cursor.fetchone()
    connection.close()

    return result


# Adiciona uma nova linha a tabela user
async def insert_new_line_user(name_user: str, last_name: str, date_birth: str, email: str, cpf: str, cellphone: str, id_address: int, password_user: str, news: bool, info_conditions:bool, share_data:bool):
    connection, cursor = connect_database(
        host=HOST,
        port=int(PORT),
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    create_user = f"""
    INSERT INTO user 
    (id_address, name_user, last_name, date_birth, email, cpf, cellphone, password_user, news, info_conditions, share_data) 
    VALUES 
    ({id_address}, '{name_user}', '{last_name}', '{date_birth}', '{email}', '{cpf}', '{cellphone}', '{password_user}', {news}, {info_conditions}, {share_data});"""
    
    cursor.execute(create_user)

    connection.commit()
    connection.close()

    return {'message': 'User created successfully'}


# Verifica cpf
async def verify_data_overwrite(cpf: str, email: str):
    connection, cursor = connect_database(
        host=HOST,
        port=int(PORT),
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    query_cpf = f"SELECT cpf FROM user WHERE cpf = '{cpf}';"

    cursor.execute(query_cpf)
    result_cpf = cursor.fetchone()

    query_email = f"SELECT email FROM user WHERE email= '{email}'"

    cursor.execute(query_email)
    result_email = cursor.fetchone()
    connection.close()

    return bool(result_cpf), bool(result_email)


# Verifica email
async def verify_email(email: str):
    connection, cursor = connect_database(
        host=HOST,
        port=int(PORT),
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    query = f"SELECT email FROM user WHERE email = '{email}';"

    cursor.execute(query)
    result = cursor.fetchone()
    connection.close()

    return result is not None


# Atualização de dados do usuário
async def update_line_users(id_user: int, last_name: str, user: UserUpdate):
    connection, cursor = connect_database(
        host=HOST,
        port=int(PORT),
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    if any(value is not None for _, value in user):
        update_user = f"UPDATE user SET" + ", ".join(f" {field} = '{value}' " for field, value in user if value is not None) + f"WHERE id = {id_user}"

        cursor.execute(update_user)
        connection.commit()
    
    if last_name is not None:
        update_last_name = f"UPDATE user SET last_name = '{last_name}' WHERE id = {id_user}"
        
        cursor.execute(update_last_name)
        connection.commit()

    query = f"SELECT id_address FROM user WHERE id = {id_user}"

    cursor.execute(query)
    result = cursor.fetchone()
    connection.close()
    result = result['id_address']

    return result


# Atualização do dado news
async def update_line_users_news(id_user: int, news: bool):
    connection, cursor = connect_database(
        host=HOST,
        port=int(PORT),
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    update_news = f"UPDATE user SET news = {news} WHERE id = {id_user}"

    cursor.execute(update_news)
    connection.commit()
    connection.close()
    
    return {'message': 'User news updated successfully'}


# Atualização de dados de address
async def update_line_address(id_address: int, address: AddressUpdate):
    connection, cursor = connect_database(
        host=HOST,
        port=int(PORT),
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    if any(value is not None for _, value in address):
        update_address = f"UPDATE `address` SET" + ", ".join(f" {field} = '{value}' " for field, value in address if value is not None) + f"WHERE id = {id_address}"

        cursor.execute(update_address)
        connection.commit()

    connection.close()

    return {'message': 'Address updated successfully'}


# Verifica a existência do usuário
def verify_user_exist(email: int):
    connection, cursor = connect_database(
        host=HOST,
        port=int(PORT),
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    query = f"SELECT id AS id_user, password_user FROM user WHERE email = '{email}'"

    cursor.execute(query)
    result = cursor.fetchone()
    connection.close()

    return result


# Verifica usuário por id
async def verify_user_exist_by_id(id_user: int):
    connection, cursor = connect_database(
        host=HOST,
        port=int(PORT),
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )
    
    query = f"SELECT id FROM user WHERE id = {id_user}"
    
    cursor.execute(query)
    result = cursor.fetchone()
    connection.close()

    return bool(result)


# Verifica cpf execeto do usuário que terá o update
async def verify_data_users(id_user: int, cpf: str, email: str):
    connection, cursor = connect_database(
        host=HOST,
        port=int(PORT),
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    query_cpf = f"SELECT cpf FROM user WHERE cpf = '{cpf}' AND id <> {id_user}"

    cursor.execute(query_cpf)
    result_cpf = cursor.fetchone()

    query_email = f"SELECT email FROM user WHERE email = '{email}' AND id <> {id_user}"

    cursor.execute(query_email)
    result_email = cursor.fetchone()
    connection.close()
    
    return bool(result_cpf), bool(result_email)