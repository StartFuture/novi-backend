use novi;

create table `address` (
    id BIGINT not null AUTO_INCREMENT,
    cep varchar(8) NOT NULL,
    state_user varchar(2) NOT NULL,
    city varchar(255) NOT NULL,
    address_user varchar(255) NOT NULL,
    address_number varchar(5) NOT NULL,
    complements varchar(255),
    PRIMARY KEY (id)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

create table user (
    id BIGINT not null AUTO_INCREMENT,
    id_address BIGINT,
    name_user varchar(255) NOT NULL,
    last_name varchar(255) NOT NULL,
    date_birth date NOT NULL,
    email varchar(30) NOT NULL UNIQUE,
    cpf varchar(11) NOT NULL UNIQUE,
    cellphone varchar(30) NOT NULL,
    password_user varchar(255) NOT NULL,
    news boolean,
    info_conditions boolean,
    share_data boolean,
    PRIMARY KEY (id),
    FOREIGN KEY (id_address) REFERENCES `address`(id)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*
create table ratings_comments(
id_review int(11) not null auto_increment,
img blob,
id_user int(11) not null,
name_user varchar(255) not null,
perfil varchar(20) not null,
stars int(5),
user_comment varchar(400),
primary key(id_review),
FOREIGN KEY (id_user) REFERENCES users (id_user)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;
*/

create table perfil(
id_perfil int(11) not null auto_increment,
perfil_user varchar(20) not null,
id_user int(11) not null,
primary key(id_perfil),
foreign key(id_user) references user (id_user)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

create table table_destinations (
    id_destination int(11) not null AUTO_INCREMENT,
    continent varchar(9),
    country varchar(255),
    state_destination varchar(2),
    city varchar(255),
    journey varchar(255),
    PRIMARY KEY (id_destination)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;
