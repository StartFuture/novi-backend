from typing import Optional
from datetime import date

from pydantic import BaseModel, Field, EmailStr


#Modelo de entrada de endereço
class Address(BaseModel):
    cep: str = Field(regex=r'^[0-9]{5}\-?[0-9]{3}$')
    state_user: str = Field(regex=r'^[A-Z]{2}$')
    city: str = Field(regex=r'^[a-zA-Z\s]{3,255}$')
    address_user: str = Field(regex=r'^[a-zA-Z\s]{5,255}$')
    address_number: str = Field(regex=r'^[0-9]{1,7}$')
    complements: Optional[str] = Field(None, regex=r'^[0-9a-zA-Z\s]{5,255}$')

#Modelo de entrada de usuários
class User(BaseModel):
    name_user: str = Field(regex=r'^[a-zA-Z\s]{3,255}')
    date_birth: str = Field(regex=r'^[0-9]{4}\-[0-9]{2}\-[0-9]{2}$')
    email: EmailStr
    cpf: str = Field(regex=r'^[0-9]{3}\.?[0-9]{3}\.?[0-9]{3}\.?\-?[0-9]{2}$')
    cellphone: str = Field(regex=r'^\+?[0-9]{2}\s?\(?[0-9]{2}\)?\s?9[0-9]{4}\-?[0-9]{4}$')
    password_user: str = Field(min_length=8)
    news: bool
    info_conditions: bool
    share_data: bool

#Modelo de update para address
class AddressUpdate(BaseModel):
    cep: Optional[str] = Field(None, regex=r'^[0-9]{5}\-?[0-9]{3}$')
    state_user: Optional[str] = Field(None, regex=r'^[A-Z]{2}$')
    city: Optional[str] = Field(None, regex=r'^[a-zA-Z\s]{3,255}$')
    address_user: Optional[str] = Field(None, regex=r'^[a-zA-Z\s]{5,255}$')
    address_number: Optional[str] = Field(None, regex=r'^[0-9]{1,7}$')
    complements: Optional[str] = Field(None, regex=r'^[0-9a-zA-Z\s]{5,255}$')

#Modelo de update para usuários
class UserUpdate(BaseModel):
    name_user: Optional[str] = Field(None, regex=r'^[a-zA-Z\s]{5,255}$')
    email: Optional[EmailStr] = None
    cpf: Optional[str] = Field(None, regex=r'^[0-9]{3}\.?[0-9]{3}\.?[0-9]{3}\.?\-?[0-9]{2}$')
    cellphone: Optional[str] = Field(None, regex=r'^\+?[0-9]{2}\s?\(?[0-9]{2}\)?\s?9[0-9]{4}\-?[0-9]{4}$')
    password_user: Optional[str] = Field(None, min_length=8)

#Modelo para update do dado news
class NewsUpdate(BaseModel):
    news: bool
