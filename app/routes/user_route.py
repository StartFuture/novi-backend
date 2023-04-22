from fastapi import APIRouter, status, HTTPException

import dao.db #import select_all, insert_new_line_user, insert_new_line_address, verify_cpf, verify_email, update_line_users
from models.user_model import  Address, User, UserUpdate
import utils #import user_data_processing, username_processing, date_english_mode, address_data_processing

user = APIRouter()

#Lista usuários
@user.get('/')
async def read_data():
    querry = dao.select_all()
    return querry


#Criação de Usuário
@user.post('/user', status_code=status.HTTP_201_CREATED)
async def write_data(address: Address, user: User):
   
    #Processando dados
    address.cep, address.city, address.address_user = utils.address_data_processing(address.cep, address.city, address.address_user)
    user.name_user, last_name = utils.username_processing(user.name_user)
    user.cpf, user.cellphone = utils.user_data_processing(user.cpf, user.cellphone)
    user.date_birth = utils.date_english_mode(user.date_birth)
    cpf_verify = await dao.db.verify_cpf(user.cpf)
    email_verify = await dao.db.verify_email(user.email)

    
    #Verificando Erros
    if cpf_verify is not False:
        print('error cpf_verify ->', cpf_verify)
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f'Cannot create user. CPF {user.cpf} alredy exist')
    if email_verify is not False:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f'Cannot create user. email: {user.email} alredy exist')
    if user.info_conditions is False:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f'Cannot create user due to authorization of the terms')


    #Criando linha na tabela address e escapando id_address(result)
    result, message = await dao.db.insert_new_line_address(
        cep= address.cep,
        state_user= address.state_user,
        city= address.city,
        address_user= address.address_user,
        address_number= address.address_number,
        complements= address.complements
    )

    #Criando linha na tabela users
    await dao.db.insert_new_line_user(
        name_user= user.name_user,
        last_name= last_name,
        date_birth= user.date_birth,
        email= user.email,
        cpf= user.cpf,
        cellphone= user.cellphone,
        id_address= result['LAST_INSERT_ID()'],
        password_user= user.password_user,
        news= user.news,
        info_conditions= user.info_conditions,
    )


    return {'message': f'User {user.name_user}, created successfully'}

@user.patch('/user/{id_user}', status_code=status.HTTP_200_OK)
async def update_data(id_user: int, address: Address, user: UserUpdate):

    #Processando dados
    address.cep, address.city, address.address_user = utils.address_data_processing(address.cep, address.city, address.address_user)
    user.name_user, last_name = utils.username_processing(user.name_user)
    user.cpf, user.cellphone = utils.user_data_processing(user.cpf, user.cellphone)
    

    #atualizando usuário
    result, message = await dao.db.update_line_users(
        name_user= user.name_user,
        last_name= last_name,
        email= user.email,
        cpf= user.cpf,
        cellphone= user.cellphone,
        password_user= user.password_user,
        news= user.news,
    )
    print('result teste - ', result)

    #atualizando address
    dao.db.insert_new_line_address(
        cep= address.cep,
        state_user= address.state_user,
        city= address.city,
        address_user= address.address_user,
        address_number= address.address_number,
        complements= address.complements,
        id_address= result['id_address']
    )


    return {'message': f'User {user.name_user}, updated successfully'}
