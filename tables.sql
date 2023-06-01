use novi;

create table `address` (
    id BIGINT NOT NULL AUTO_INCREMENT,
    cep varchar(8) NOT NULL,
    state_user varchar(2) NOT NULL,
    city varchar(255) NOT NULL,
    address_user varchar(255) NOT NULL,
    address_number varchar(5) NOT NULL,
    complements varchar(255),
    PRIMARY KEY (id)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

create table `user` (
    id BIGINT NOT NULL AUTO_INCREMENT,
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


create table transport (
    id BIGINT NOT NULL AUTO_INCREMENT,
    details VARCHAR(255) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    transport_style INT(1) NOT NULL,
    PRIMARY KEY(id)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

create table accommodation (
    id BIGINT NOT NULL AUTO_INCREMENT,
    travel_destination INT(2) NOT NULL,
    travel_style INT(2) NOT NULL,
    accommodation_style INT(1) NOT NULL,
    is_country BOOLEAN NOT NULL,
    warm int(1) NOT NULL,
    mild INT(1) NOT NULL,
    cold INT(1) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    details VARCHAR(255) NOT NULL,
    PRIMARY KEY(id)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

create table tour (
    id BIGINT NOT NULL AUTO_INCREMENT,
    night_style INT(1) NOT NULL,
    music_preference INT(1) NOT NULL,
    building_preference INT(1) NOT NULL,
    tradicion_preference INT(1) NOT NULL,
    party_preference INT(1) NOT NULL,
    water_preference INT(1) NOT NULL,
    walk_preference INT(1) NOT NULL,
    historic_preference INT(1) NOT NULL,
    sport_preference INT(1) NOT NULL,
    food_preference INT(1) NOT NULL,
    id_accommodation BIGINT NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    details VARCHAR(255) NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY(id_accommodation) REFERENCES accommodation(id)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

create table travel (
    id BIGINT NOT NULL AUTO_INCREMENT,
    id_user BIGINT,
    id_accommodation BIGINT,
    id_transport_from BIGINT,
    id_transport_return BIGINT,
    date_from DATE NOT NULL,
    date_return DATE,
    quantity_people INT(2) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY(id_user) REFERENCES user(id),
    FOREIGN KEY(id_accommodation) REFERENCES accommodation(id),
    FOREIGN KEY(id_transport_from) REFERENCES transport(id),
    FOREIGN KEY(id_transport_return) REFERENCES transport(id)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

create table traveltour(
    id BIGINT NOT NULL AUTO_INCREMENT,
    id_travel BIGINT,
    id_tour BIGINT,
    PRIMARY KEY(id),
    FOREIGN KEY(id_travel) REFERENCES travel(id),
    FOREIGN KEY(id_tour) REFERENCES tour(id)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


create table travel_options(
  id_options BIGINT not null auto_increment,
  travel_destination int(1) not null,
  travel_style int(1) not null,
  accommodation_style int(1) not null,
  night_style int(1) not null,
  can_leave_country boolean not null,
  transport_style int(1) not null,
  id_user BIGINT not null,
  primary key(id_options),
  foreign key(id_user) references user(id)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

create table travel_activities(
  id_activities BIGINT not null auto_increment,
  water_preference int(1) not null,
  walk_preference int(1) not null,
  historic_preference int(1) not null,
  sport_preference int(1) not null,
  food_preference int(1) not null,
  id_user BIGINT not null,
  primary key(id_activities),
  foreign key(id_user) references user(id)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

create table travel_cultures(
  id_cultures BIGINT not null auto_increment,
  music_preference int(1) not null,
  building_preference int(1) not null,
  tradicion_preference int(1) not null,
  party_preference int(1) not null,
  no_preference boolean not null,
  id_user BIGINT not null,
  primary key(id_cultures),
  foreign key(id_user) references user(id)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


create table weather_option(
  id_weather_option BIGINT not null auto_increment,
  warm int(1) not null,
  mild int(1) not null,
  cold int(1) not null,
  no_preference boolean not null,
  id_user BIGINT not null,
  primary key(id_weather_option),
  foreign key(id_user) references user(id)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;