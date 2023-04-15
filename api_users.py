from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import Optional
from datetime import date
import sqlite3

banco = sqlite3.connect('banco_de_dados.db')
cur = banco.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS address(id_address INTEGER PRIMARY KEY, cep INTEGER, state TEXT,
            city TEXT, street TEXT, number INTEGER, complemento TEXT NULL)''')

cur.execute ('''CREATE TABLE IF NOT EXISTS users (id_user INTEGER PRIMARY KEY, name TEXT, last_name TEXT,
             email TEXT UNIQUE, cpf INTEGER UNIQUE, date_birth TEXT, cellphone INTEGER,
             id_address INTEGER, FOREIGN KEY (id_address) REFERENCES address (id_address), password TEXT,
             news INTEGER, info_conditions INTEGER)''')

banco.commit()


pattern = r'^[a-zA-Z\s][Ç,ç]?$'
email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

class Address(BaseModel):
    cep: Field(min_Length=8, max_length=8, regex=r'^[0-9]{5}\-?[0-9]{3}$')
    state: Field(min_length=2, max_length=2, regex=pattern)
    city: Field(min_length=3, max_length=8, regex=r'')
    address: Field()
    number_address: Field(min_length=1, max_length=6, regex=r'[0-9]')
    complemento: Optional[Field(max_length=30)] = None

class User(BaseModel):
    name_user: str = Field(min_lenght=3, max_length=25, regex=pattern)
    data_entrada: date = Field(mLength=8, regex=r'^[0-3][0-9]\/?[0-1]?[0-9]\/?[1-2][9,0][0-9]{2}$')
    email: str = Field(min_lenght=3, max_lenght=25, regex=email_pattern)
    cpf: str = Field(mLenght=11, regex=r'^[0-9]{3}\.?[0-9]{3}\.?[0-9]{3}\.?\-?[0-9]{2}$').replace('.', '').replace('-', '')
    cellphone: str = Field(mlenght=11, regex=r'^\+?[0-9]{2}9[0-9]{4}\-?[0-9]{4}$').replace()
    password: str = Field(min_Lenght=8)
