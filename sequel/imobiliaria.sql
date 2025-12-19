# para criar a base de dados usamos o comando create database
create database imobiliaria;

# usar database
use imobiliaria;

#se quiser ver todas as databses
show databases;

# para criar uma tabela eh parecido com criar um bd
# create table NOME_DA_TABELA();
create table imoveis(
#NOME_DO_CAMPO DATA_TYPE atributos
id_imoveis int auto_increment primary key,
cidade_imoveis varchar(255) not null,
tipo_imoveis enum('casa','sobrado','terreno','comercial') not null,
valor_imoveis decimal(12,2) not null,
data_anuncio_imoveis date not null
);

# agora vamos popular a tabela
insert into imoveis(cidade_imoveis, tipo_imoveis, valor_imoveis, data_anuncio_imoveis)
values
# cada insercao de dados fica dentro de ()
('Ferraz', 'terreno',80000.00, '2025-12-12'),
('Estrela', 'comercial', 600000.00,'2025-11-26'),
('Praia Grande', 'casa', 150000.50,'2025-11-03');

select * from imoveis;

insert into imoveis(cidade_imoveis, tipo_imoveis, valor_imoveis, data_anuncio_imoveis)
values
('Campinas', 'casa', 680000.00, '2024-03-10'),
('Santos', 'sobrado', 980000.00, '2024-03-04'),
('Campinas', 'terreno', 350000.00, '2024-03-05'),
('Rio de Janeiro', 'comercial', 280000, '2024-03-03'),
('São Paulo', 'casa', 850000.00, '2024-03-01');

# exibição condicionada
select * from imoveis where valor_imoveis < 100000;

# para arrumar um dado da tabela preciso de uma referencia
update imoveis set valor_imoveis = 90000.00 where id_imoveis = 1;
# sempe que eu quero arrumar um dado eu informo o daado correto e depois a referencia

delete from imoveis where valor_imoveis < 300000;

alter table imoveis modify tipo_imoveis enum('apartamento','casa','sobrado','terreno','comercial') not null

