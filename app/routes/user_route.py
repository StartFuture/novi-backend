from fastapi import APIRouter, status, HTTPException

from dao.db import select_all, insert_new_line_user, insert_new_line_address, verify_cpf, verify_email, update_line_users
from models.user_model import  Address, User, UserUpdate
from utils import user_data_processing, username_processing, date_english_mode, address_data_processing

user = APIRouter()

#Lista usuários
@user.get('/')
async def read_data():
    querry = select_all()
    return querry


#Criação de Usuário
@user.post('/user', status_code=status.HTTP_201_CREATED)
async def write_data(address: Address, user: User):
   
    ####### TENTAR CRIAR DOIS DEFS, um para address e outro para usuário.
    #Processando dados
    address.cep, address.city, address.address_user = address_data_processing(address.cep, address.city, address.address_user)
    user.name_user, last_name = username_processing(user.name_user)
    user.cpf, user.cellphone = user_data_processing(user.cpf, user.cellphone)
    user.date_birth = date_english_mode(user.date_birth)
    cpf_verify = verify_cpf(user.cpf)
    email_verify = verify_email(user.cpf)

    print(user.cellphone)
    
    #Verificando Erros
    if cpf_verify is not None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f'Cannot create user. CPF {user.cpf} alredy exist')
    if email_verify is not None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f'Cannot create user. email: {user.email} alredy exist')
    if user.info_conditions is False:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f'Cannot create user due to authorization of the terms')
    
    #Criando tabela e escapando id_address(result)
    result = await insert_new_line_address (
        cep= address.cep,
        state_user= address.state_user,
        city= address.city,
        address_user= address.address_user,
        address_number= address.address_number,
        complements= address.complements
    )
    print(result)
    #Criando tabela
    await insert_new_line_user(
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
async def update_data(address: Address, user: UserUpdate):
    update_line_users(
        name_user= user.str,
        last_name= user.str,
        
        
        
    )
    return {'message': f'User {user.name_user}, created successfully'}