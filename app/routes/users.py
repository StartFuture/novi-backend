from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.responses import JSONResponse
import requests

from dao import dao_users
from models.models_user import  Address, User, UserUpdate, AddressUpdate, NewsUpdate
import utils


router = APIRouter()


@router.delete("/delete_user", status_code=status.HTTP_200_OK)
def delete(token: str = Depends(utils.verify_token)):
    query_result = dao_users.delete_user_by_id(id_user=token["sub"])
    if query_result:
        return {'message': 'user delete.'}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="wrong input")


@router.get('/read_user', status_code=status.HTTP_302_FOUND)
async def read_user_data(token: str = Depends(utils.verify_token)):

    query_user, id_address = await dao_users.select_user(token["sub"])

    if query_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User not exist')
    
    id_address = int(id_address['id_address'])
    query_user['date_birth'] = utils.format_date(query_user['date_birth'])
    
    query_address = await dao_users.select_address(id_address)
    data = {'user': query_user, 'address': query_address}
    return JSONResponse(content=data)


@router.post('/create_user', status_code=status.HTTP_201_CREATED)
async def write_data(address: Address, user: User):
    
    #Verificação de CEP
    address.cep = utils.cep_data_processing(address.cep)
    request =requests.get('https://viacep.com.br/ws/{}/json/'.format(address.cep))
    address_data = request.json()
    if 'erro' not in address_data:
        address.state_user = address_data['uf']
        address.city = address_data['localidade']
        address.address_user = address_data['logradouro']
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Cannot create user. CEP {address.cep} not exist')

    #Processando dados    
    address.city, address.address_user, address.complements = await utils.address_data_processing(address.city, address.address_user, address.complements)
    user.name_user, last_name = utils.username_processing(user.name_user)
    user.cpf, user.cellphone, user.email = await utils.user_data_processing(user.cpf, user.cellphone, user.email)
    cpf_verify, email_verify = await dao_users.verify_data_overwrite(user.cpf, user.email)
    ddi_verify = utils.consult_ddi(user.cellphone)


    #Verificando Erros
    if not ddi_verify:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'cannot create user. ddi {user.cellphone} is invalid')
    if cpf_verify:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f'Cannot create user. CPF {user.cpf} alredy exist')
    if email_verify:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f'Cannot create user. email: {user.email} alredy exist')
    if not user.info_conditions:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f'Cannot create user due to authorization of the terms')


    #Criando linha na tabela address e escapando id_address(result)
    result = await dao_users.insert_new_line_address(
        cep= address.cep,
        state_user= address.state_user,
        city= address.city,
        address_user= address.address_user,
        address_number= address.address_number,
        complements= address.complements
    )

    #Criando linha na tabela users
    await dao_users.insert_new_line_user(
        name_user= user.name_user,
        last_name= last_name,
        date_birth= user.date_birth,
        email= user.email,
        cpf= user.cpf,
        cellphone= user.cellphone,
        id_address= result['LAST_INSERT_ID()'],
        password_user= utils.get_pwd_hash(user.password_user),
        news= user.news,
        info_conditions= user.info_conditions,
        share_data= user.share_data
    )

    return JSONResponse(content={'message': f'User {user.name_user}, created successfully'})


@router.patch('/update_user', status_code=status.HTTP_200_OK)
async def update_data(address: AddressUpdate, user: UserUpdate, news_update: NewsUpdate, token: str = Depends(utils.verify_token)):

    #Verificação de CEP
    if address.cep is not None:
        address.cep = utils.cep_data_processing(address.cep)
        request =requests.get('https://viacep.com.br/ws/{}/json/'.format(address.cep))
        address_data = request.json()
        if 'erro' not in address_data:
            address.state_user = address_data['uf']
            address.city = address_data['localidade']
            address.address_user = address_data['logradouro']
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Cannot create user. CEP {address.cep} not exist')

    #Processando dados
    address.city, address.address_user, address.complements = await utils.address_data_processing(address.city, address.address_user, address.complements)
    user.name_user, last_name = utils.username_processing(user.name_user)
    user.cpf, user.cellphone, user.email = await utils.user_data_processing(user.cpf, user.cellphone, user.email)
    verify_cpf, verify_email = await dao_users.verify_data_users(token["sub"], user.cpf, user.email)
    verify_user = await dao_users.verify_user_exist_by_id(token["sub"])

    #Verificando Erros
    if not verify_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User not found')
    if verify_cpf:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f'Cannot create user. CPF {user.cpf} alredy exist')
    if verify_email:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f'Cannot create user. Email {user.email} alredy exist')
    
    #atualizando usuário
    result = await dao_users.update_line_users(
        id_user= token["sub"],
        last_name= last_name,
        user= user
    )
    await dao_users.update_line_users_news(
        id_user= token["sub"],
        news= news_update.news
    )

    #atualizando address
    await dao_users.update_line_address(
        id_address= result,
        address= address
    )

    return JSONResponse(content={'message': f'User {user.name_user}, updated successfully'})
