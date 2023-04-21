from typing import Optional
from datetime import date

from pydantic import BaseModel, Field

pattern = r'^[a-zA-Z\s]+$'
email_pattern = r'^[a-zA-Z\.]+@[a-zA-Z\.]+\.*[a-zA-Z]$'


#Modelo de entrada de endereço
class Address(BaseModel):
    cep: Optional[str] = None, Field(min_length=8, max_length=9, regex=r'^[0-9]{5}\-?[0-9]{3}$')
    state_user: Optional[str] = None, Field(min_length=2, max_length=2, regex=r'^[A-Z]{2}$')
    city: Optional[str] = None, Field(min_length=3, max_length=255, regex=r'^[a-zA-Z\s]{3,255}$')
    address_user: Optional[str] = None, Field(min_length=5, max_length=255, regex=r'^[a-zA-Z\s]{5,255}$')
    address_number: Optional[str] = None, Field(min_length=1, max_length=7, regex=r'^[0-9]{1,7}$')
    complements: Optional[str] = None, Field(min_length=1 ,max_length=45, regex=r'^[0-9a-zA-Z\s]{5,255}$')


#Modelo de entrada para usuários
class User(BaseModel):
    name_user: str = Field(min_length=3, max_length=255, regex=pattern)
    date_birth: str = Field(regex=r'^[0-9]{2}\/[0-9]{2}\/[0-9]{4}$')
    email: str = Field(min_length=3, max_length=80, regex=email_pattern)
    cpf: str = Field(min_length=11, max_length=14, regex=r'^[0-9]{3}\.?[0-9]{3}\.?[0-9]{3}\.?\-?[0-9]{2}$')
    cellphone: str = Field(min_length=11, max_length=15, regex=r'^\(?[0-9]{2}\)?\s?9[0-9]{4}\-?[0-9]{4}$')
    password_user: str = Field(min_length=8)
    news: bool
    info_conditions: bool


#Modelo de update para usuários
class UserUpdate(User):
    name_user: Optional[str] = Field(None, min_length=3, max_length=25, regex=pattern)
    email: Optional[str] = Field(None, min_length=3, max_length=80, regex=email_pattern)
    cpf: Optional[str] = Field(None, min_length=11, max_length=14, regex=r'^[0-9]{3}\.?[0-9]{3}\.?[0-9]{3}\.?\-?[0-9]{2}$')
    cellphone: Optional[str] = Field(None, min_length=11, max_length=15, regex=r'^\(?[0-9]{2}\)?\s?9[0-9]{4}\-?[0-9]{4}$')
    password_user: Optional[str] = Field(None, min_lenght=8)
    news: bool
