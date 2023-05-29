from datetime import timedelta, datetime
from typing import Dict
import requests
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, status, HTTPException
import logging

from parameters import JWT_SECRET, JWT_ALGORITHM
LINK_API = "https://api-paises.pages.dev/paises.json"


oauth = OAuth2PasswordBearer(tokenUrl="/auth/login")

# Processar dados de usuário
async def user_data_processing(cpf: str, cellphone: str, email: str):
    if cpf is not None:
        cpf = cpf.replace('.', '').replace('-', '')
    if cellphone is not None:
        cellphone = cellphone.replace('-', '').replace('(', '').replace(')', '').replace(' ', '').replace('+', '')
    if email is not None:
        email = email.lower().strip()
    return cpf, cellphone, email

# Processar username
def username_processing(name_user: str):
    if name_user is not None:
        if len(name_user.strip().split(' ', 1)) > 1:
            name = name_user.strip().split(' ', 1)
            name_user = str(name[0]).lower().strip()
            last_name = str(name[1]).lower().strip()
            return name_user, last_name
        else:
            name = name_user.strip().split(' ', 1)
            name_user = str(name[0]).lower().strip()
            last_name = None
            return name_user, last_name
    else:
        last_name = None
        return name_user, last_name


# Formatar date de dicionário para formato DD/MM/YYYY
def format_date(date):
    return f"{date.year}-{date.month}-{date.day}"


# Processar dado da tabela Address
async def address_data_processing(city:str, address_user:str, complements:str):
    if city is not None:
        city = city.strip().lower()
    if address_user is not None:
        address_user = address_user.strip().lower()
    if complements is not None:
        complements = complements.strip().lower()
    return city, address_user, complements


# Processar dado cep
def cep_data_processing(cep:str):
    if cep is not None:
        cep = cep.replace('-', '')
    return cep

    return cep, city, address_user

# Validação de ddi
def consult_ddi(cellphone: str):    
    ddi = cellphone.replace('+', '')[:2]
    list_ddi = []
    response = requests.get(LINK_API)
    for value in response.json().values():
        list_ddi.append(value['ddi'])
    if ddi in list_ddi:
        return True
    else: 
        return False
    

def decrypt_token(token: str) -> dict[str]:
    print("token = " + token)
    print("algorithms = " + JWT_ALGORITHM)
    print("secret = " + JWT_SECRET)
    result = jwt.decode(access_token=token, key=JWT_SECRET, algorithms=JWT_ALGORITHM)
    print(result)

    return result


def get_user_id(token: str) -> int:
    user = decrypt_token(token=token)
    logging.warning(user)
    if not "sub" in user:
        raise ValueError('Token incorrect')

    return int(user['sub'])


def signJWT(user_id: str) -> dict[str]:
    payload = {
        "sub": user_id,
        "exp": datetime.utcnow() + timedelta(minutes=30),
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    
    return {'access_token': token}


def verify_token(token: str = Depends(oauth)): # transformar em decorator

    try:
        payload = jwt.decode(token, key=JWT_SECRET, algorithms=JWT_ALGORITHM)
        return payload
    except JWTError:
        raise HTTPException(detail={'msg': 'missing token'}, 
                             status_code=status.HTTP_401_UNAUTHORIZED)