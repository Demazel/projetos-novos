create database zoologico;

show databases;

use zoologico;

CREATE TABLE animal (
id_animal INT AUTO_INCREMENT PRIMARY KEY, # nome, numero, auto incrementar e chave primaria 
nome_animal VARCHAR(255) NOT NULL, # not null significa que nao pode ser nulo
especie_animal VARCHAR(255) NOT NULL,
sexo_animal ENUM('M','F'), # enum de enunciar
data_nasc_animal DATE, #0000/00/00
recinto_animal VARCHAR(255) not null,
tratador_animal VARCHAR(255)
);

create table recinto (
id_recinto int auto_increment primary key,
nome_recinto varchar(255) not null,
tipo_recinto enum('savana', 'aquario', 'insetario', 'floresta', 'lago', 'outro'),
localizacao_recinto varchar(255) not null,
capacidade_recinto int not null
);

# para alterar uma tabela, seja ela interia ou parte
alter table recinto modify tipo_recinto enum('savana', 'aquario', 'insetario', 'floresta', 'lago', 'outro');
alter table recinto modify capacidade_recinto bigint not null;
# int suporta ate 10 caracteres 0123456789

alter table recinto change localizacao_recinto local_recinto varchar(255) not null;


create table tratador (
id_tratador int auto_increment primary key,
nome_tratador varchar(255) not null,
cpf_tratador bigint unique not null,
animal_tratador varchar(255) not null,
recinto_tratador enum('savana', 'aquario', 'insetario', 'floresta', 'lago', 'outro'),
turno_tratador enum('manhã', 'tarde', 'noite'),
status_tratador enum('Ativo', 'Inativo')
);

select * from tratador;

create table alimentacao(
id int
);

drop table alimentacao;

show tables;

