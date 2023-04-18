create table users (
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
    PRIMARY KEY (id_user)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

create table address (
    id_address int(11) not null AUTO_INCREMENT,
    cep varchar(255),
    state_user varchar(255),
    city varchar(255),
    address_user varchar(255),
    address_number varchar(255),
    complements varchar(255),
    PRIMARY KEY (id_address)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;