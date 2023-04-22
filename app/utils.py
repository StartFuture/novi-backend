def user_data_processing(cpf: str, cellphone: str):
    if cpf is not None:
        cpf = cpf.replace('.', '').replace('-', '')
    if cellphone is not None:
        cellphone = cellphone.replace('-', '').replace('(', '').replace(')', '').replace(' ', '')
    return cpf, cellphone

def username_processing(name_user: str):
    if name_user is not None:
        if len(name_user.split(' ', 1)) > 1:
            name = name_user.strip().split(' ', 1)
            name_user = str(name[0]).lower().strip()
            last_name = str(name[1]).lower().strip()
            return name_user, last_name
        else:
            name = name_user.strip().split(' ', 1)
            name_user = str(name[0]).lower().strip()
            last_name = None
            return name_user, last_name

def date_english_mode(date_birth: str):
    date = date_birth.strip().replace('/', '')
    date_year = date[4:8]
    date_month = date[2:4]
    date_day = date[:2]
    date_birth = str(date_year + date_month + date_day)
    return date_birth

def address_data_processing(cep: str, city:str, address_user:str):
    if cep is not None:
        cep = cep.replace('-', '')
    if city is not None:
        city = city.lower()
    if address_user is not None:
        address_user = address_user.lower()
    return cep, city, address_user