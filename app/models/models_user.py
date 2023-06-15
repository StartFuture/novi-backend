from typing import Optional
from datetime import date

from pydantic import BaseModel, Field, EmailStr


#Address regex
REGEX_CEP=r'^[0-9]{5}\-?[0-9]{3}$'
REGEX_ADDRESS_NUMBER=r'^[0-9]{0,14}$'

#User regex
REGEX_CPF=r'^[0-9]{3}\.?[0-9]{3}\.?[0-9]{3}\.?\-?[0-9]{2}$'
REGEX_CELLPHONE=r'^\+?[0-9]{2}\s?\(?[0-9]{2}\)?\s?9[0-9]{4}\-?[0-9]{4}$'


#Modelo de entrada de endereço
class Address(BaseModel):
    cep: str = Field(regex=REGEX_CEP)
    state_user: str
    city: str
    address_user: str
    address_number: str = Field(regex=REGEX_ADDRESS_NUMBER)
    complements: Optional[str] = Field(None)


#Modelo de entrada de usuários
class User(BaseModel):
    name_user: str
    date_birth: str = Field(regex=r'^[0-9]{4}\-[0-9]{2}\-[0-9]{2}$')
    email: EmailStr
    cpf: str = Field(regex=REGEX_CPF)
    cellphone: str = Field(regex=REGEX_CELLPHONE)
    password_user: str
    news: bool
    info_conditions: bool
    share_data: bool


#Modelo de update para address
class AddressUpdate(BaseModel):
    cep: Optional[str] = Field(None, regex=REGEX_CEP)
    state_user: Optional[str] = Field(None)
    city: Optional[str] = Field(None)
    address_user: Optional[str] = Field(None)
    address_number: Optional[str] = Field(None, regex=REGEX_ADDRESS_NUMBER)
    complements: Optional[str] = Field(None)


#Modelo de update para usuários
class UserUpdate(BaseModel):
    name_user: Optional[str] = Field(None)
    email: Optional[EmailStr] = None
    cpf: Optional[str] = Field(None, regex=REGEX_CPF)
    cellphone: Optional[str] = Field(None, regex=REGEX_CELLPHONE)
    password_user: Optional[str] = Field(None)


#Modelo para update do dado news
class NewsUpdate(BaseModel):
    news: bool

#Modelo para inserir a avaliação do usuario
class user_review(BaseModel):
    name_user: str
    perfil: Optional[str]
    stars: Optional[int]
    comment: str
