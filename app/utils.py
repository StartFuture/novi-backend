from datetime import timedelta, datetime
from typing import Dict

from jose import jwt

from parameters import JWT_SECRET, JWT_ALGORITHM

def signJWT(user_id: str, type_jwt: str) -> Dict[str, str]:
    payload = {
        "user_id": user_id,
        "exp": 3,
        "type": type_jwt
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return {'access_token': token}


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
    return f"{date.day}/{date.month}/{date.year}"


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
