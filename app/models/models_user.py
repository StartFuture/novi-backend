from typing import Optional
from datetime import date

from pydantic import BaseModel, Field, EmailStr


#Address regex
REGEX_CEP=r'^[0-9]{5}\-?[0-9]{3}$'
REGEX_STATE=r'^[A-Z]{2}$'
REGEX_CITY=r'^[a-zA-Z\s]{3,255}$'
REGEX_ADDRESS_USER=r'^[a-zA-Z\s]{5,255}$'
REGEX_ADDRESS_NUMBER=r'^[0-9]{1,7}$'
REGEX_COMPLEMENTS=r'^[0-9a-zA-Z\s]{5,255}$'

#User regex
REGEX_NAME=r'^[a-zA-Z\s]{3,255}$'
REGEX_CPF=r'^[0-9]{3}\.?[0-9]{3}\.?[0-9]{3}\.?\-?[0-9]{2}$'
REGEX_CELLPHONE=r'^\+?[0-9]{2}\s?\(?[0-9]{2}\)?\s?9[0-9]{4}\-?[0-9]{4}$'


#Modelo de entrada de endereço
class Address(BaseModel):
    cep: str = Field(regex=REGEX_CEP)
    state_user: str = Field(regex=REGEX_STATE)
    city: str = Field(regex=REGEX_CITY)
    address_user: str = Field(regex=REGEX_ADDRESS_USER)
    address_number: str = Field(regex=REGEX_ADDRESS_NUMBER)
    complements: Optional[str] = Field(None, regex=REGEX_COMPLEMENTS)


#Modelo de entrada de usuários
class User(BaseModel):
    name_user: str = Field(regex=REGEX_NAME)
    date_birth: str = Field(regex=r'^[0-9]{4}\-[0-9]{2}\-[0-9]{2}$')
    email: EmailStr
    cpf: str = Field(regex=REGEX_CPF)
    cellphone: str = Field(regex=REGEX_CELLPHONE)
    password_user: str = Field(min_length=8)
    news: bool
    info_conditions: bool
    share_data: bool


#Modelo de update para address
class AddressUpdate(BaseModel):
    cep: Optional[str] = Field(None, regex=REGEX_CEP)
    state_user: Optional[str] = Field(None, regex=REGEX_STATE)
    city: Optional[str] = Field(None, regex=REGEX_CITY)
    address_user: Optional[str] = Field(None, regex=REGEX_ADDRESS_USER)
    address_number: Optional[str] = Field(None, regex=REGEX_ADDRESS_NUMBER)
    complements: Optional[str] = Field(None, regex=REGEX_COMPLEMENTS)


#Modelo de update para usuários
class UserUpdate(BaseModel):
    name_user: Optional[str] = Field(None, regex=REGEX_NAME)
    email: Optional[EmailStr] = None
    cpf: Optional[str] = Field(None, regex=REGEX_CPF)
    cellphone: Optional[str] = Field(None, regex=REGEX_CELLPHONE)
    password_user: Optional[str] = Field(None, min_length=8)


#Modelo para update do dado news
class NewsUpdate(BaseModel):
    news: bool

#Modelo para inserir a avaliação do usuario
class user_review(BaseModel):
    name_user: str
    perfil: Optional[str]
    stars: Optional[int]
    comment: str
