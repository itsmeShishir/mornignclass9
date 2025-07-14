# Structure Query language -> Sql 1. sql, no-sql -> realtion ->  

# database -> table -> row and columns

# How to create DataBase Table
CREATE DATABASE BlogApp;

# use 
use BlogApp;

# Comment -> 
# Data types -> int, varchar, longtext, text, float, datetime, 
# varchar(0-255) -> 
# how to create table in sql?


create table users(
	id INT PRIMARY Key AUTO_INCREMENT,
    username varchar(255) UNIQUE not null,
    email varchar(255) not null,
    created_at datetime default CURRENT_TIMESTAMP
);

create table category(
	id int PRIMARY Key AUTO_INCREMENT,
    category_name varchar(255), 
    created_at datetime default CURRENT_TIMESTAMP
);

create table blog(
    id INT PRIMARY Key AUTO_INCREMENT,
    title varchar(255) not null,
    description text not null,
    user_id INT not null, 
    category_id INT not null,
    created_at datetime default CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (category_id) REFERENCES category(id)
);

# we need to add value in the table -> insert
# value , values 
INSERT into users (username, email) VALUE
("hari", "hari@gmail.com");

INSERT into users (username, email) VALUES
("ram", "ram@gmail.com"),
("sita", "sita@gmail.com"),
("laxman", "laxman@gmail.com");

# Column delete/add/modify , table ko column update, -> Alter table 
alter table category add COLUMN short_description text not null;
alter table category drop column short_description;
alter table category change category_name title varchar(100);
# Delete table 

create table tag(
id int PRIMARY KEY AUTO_INCREMENT,
title varchar(255)
);

# Drop table ->
drop table tag;
