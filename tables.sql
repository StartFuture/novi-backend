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
    PRIMARY KEY (id_user)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

use novi;

create table table_address (
    id_address int(11) not null AUTO_INCREMENT,
    cep varchar(8),
    state_user varchar(2),
    city varchar(30),
    address_user varchar(255),
    address_number varchar(5),
    complements varchar(255),
    PRIMARY KEY (id_address),
    FOREIGN KEY (id_user) REFERENCES table_users(id_users)    
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


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


create table user_profile(
id_profile int(11)not null auto_increment,
profile_user varchar(20) not null,
id_user int(11) not null,
primary key(id_profile),
foreign key(id_user) references users (id_user)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


create table two_auth(
`id_token` INT(11) NOT NULL AUTO_INCREMENT,
`date_expires` date not null,
`id_user` int(11) not null,
`user_code` char(6), 
primary key(id_token),
FOREIGN KEY (`id_user`) REFERENCES `users` (`id_user`)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;