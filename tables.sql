create database novi;

use novi;

create table table_users (
    id_user int(11) not null AUTO_INCREMENT,
    name_user varchar(255),
    last_name varchar(255),
    date_birth date,
    email varchar(30),
    cpf varchar(11),
    cellphone varchar(30),
    id_address varchar(255),
    password_user varchar(255),
    news boolean,
    info_conditions boolean,
    share_data boolean,
    PRIMARY KEY (id_user)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

create table table_address (
    id_address int(11) not null AUTO_INCREMENT,
    cep varchar(8),
    state_user varchar(2),
    city varchar(30),
    address_user varchar(255),
    address_number varchar(5),
    complements varchar(255),
    PRIMARY KEY (id_address)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;