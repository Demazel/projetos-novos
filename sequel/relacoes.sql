create database relacoes;
use relacoes;

create table clientes(
id_cliente int auto_increment primary key,
nome_cliente varchar (255) not null,
cidade_cliente varchar(255) not null
);

create table produtos(
id_produto int auto_increment primary key,
nome_produto varchar (255) not null, 
preco_produto decimal (10,2) not null
);

create table pedidos(
id_pedido int auto_increment primary key,
id_cliente int not null,
id_produto int not null,
quantidade int not null,
data_pedido date not null,

# sempre que vamos criar um relacionamento, devemos dizer onde está
constraint fk_cliente foreign key (id_cliente) references clientes(id_cliente),
constraint fk_produto foreign key (id_produto) references produtos(id_produto)
# eu uso o comando CONSTRAINT para dar um nome para a chave
# uso o comando FOREIGN KEY (campo na tabela atual) e REFERENCES tabela_referencia(campo_referencia) 
);

INSERT INTO clientes VALUES
(1, 'Ana Silva', 'São Paulo'),
(2, 'Bruno Costa', 'Rio de Janeiro'),
(3, 'Carla Mendes', 'Belo Horizonte'),
(4, 'Daniel Rocha', 'Curitiba'),
(5, 'Eduarda Lima', 'Porto Alegre'),
(6, 'Felipe Santos', 'Campinas'),
(7, 'Gabriela Alves', 'São Paulo'),
(8, 'Henrique Pires', 'Niterói'),
(9, 'Isabela Torres', 'Recife'),
(10, 'João Martins', 'Fortaleza'),
(11, 'Karen Souza', 'Manaus'),
(12, 'Lucas Nogueira', 'Brasília'),
(13, 'Mariana Farias', 'Salvador'),
(14, 'Nathan Ribeiro', 'Goiânia'),
(15, 'Olivia Barros', 'Florianópolis'),
(16, 'Paulo Azevedo', 'Vitória'),
(17, 'Renata Cunha', 'Natal'),
(18, 'Samuel Teixeira', 'São Luís'),
(19, 'Tatiana Lopes', 'Aracaju'),
(20, 'Victor Moraes', 'Belém');
 
 
INSERT INTO produtos VALUES
(1, 'Notebook', 3500.00),
(2, 'Mouse', 80.00),
(3, 'Teclado', 150.00),
(4, 'Monitor 24"', 900.00),
(5, 'Headset', 200.00),
(6, 'Impressora', 1200.00),
(7, 'Webcam', 250.00),
(8, 'HD Externo', 450.00),
(9, 'SSD 1TB', 650.00),
(10, 'Pen Drive 64GB', 60.00),
(11, 'Cadeira Gamer', 1100.00),
(12, 'Mesa Escritório', 800.00),
(13, 'Roteador Wi-Fi', 300.00),
(14, 'Fonte 600W', 500.00),
(15, 'Placa de Vídeo', 2800.00),
(16, 'Memória RAM 16GB', 400.00),
(17, 'Processador', 1500.00),
(18, 'Cooler CPU', 180.00),
(19, 'Estabilizador', 220.00),
(20, 'Notebook Stand', 120.00);
 
INSERT INTO pedidos VALUES
(1, 1, 1, 1, '2024-01-10'),
(2, 1, 2, 2, '2024-01-15'),
(3, 2, 4, 1, '2024-01-18'),
(4, 3, 3, 1, '2024-01-20'),
(5, 4, 5, 1, '2024-01-22'),
(6, 5, 6, 1, '2024-01-25'),
(7, 6, 2, 3, '2024-01-28'),
(8, 7, 7, 1, '2024-02-01'),
(9, 8, 8, 1, '2024-02-03'),
(10, 9, 9, 1, '2024-02-05'),
(11, 10, 10, 4, '2024-02-07'),
(12, 11, 11, 1, '2024-02-10'),
(13, 12, 12, 1, '2024-02-12'),
(14, 13, 13, 1, '2024-02-15'),
(15, 14, 14, 1, '2024-02-18'),
(16, 15, 15, 1, '2024-02-20'),
(17, 16, 16, 2, '2024-02-22'),
(18, 17, 17, 1, '2024-02-25'),
(19, 18, 18, 1, '2024-02-27'),
(20, 19, 2, 1, '2024-03-01');

insert into pedidos(id_cliente, id_produto, quantidade, data_pedido)
values
(6,15,3,'2025-12-17'),
(9,3,3,'2025-12-16');

# quero mostrar:
# nome_cliente | Id_pedido | Nome_produto | preco | quantidade | faturamento
select c.nome_cliente, v.id_pedido as Id_pedido, p.nome_produto as Nome_produto, p.preco_produto as preco, v.quantidade, p.preco_produto * v.quantidade as faturamento
from pedidos v
join produtos p on v.id_produto = p.id_produto 
join clientes c on v.id_cliente = c.id_cliente;

# join é o comando para mostrar varias tabelas em uma só
# inner join ou join - dados correspondentes

# nome_cliente | nome_produto | id_pedido

select c.nome_cliente, coalesce(p.nome_produto, 'SEM PRODUTO COMPRADO'), v.id_pedido
from clientes c
left join pedidos v on c.id_cliente = v.id_cliente
left join produtos p on v.id_pedido = p.id_produto;

# mostre o faturamento total por cliente

select c.nome_cliente, sum(v.quantidade * p.preco_produto) as faturamento 
from clientes c
left join pedidos v on c.id_cliente = v.id_cliente
left join produtos p on p.id_produto = v.id_produto
group by c.nome_cliente;

# mostre apenas os clientes que nao fizeram pedidos

select c.nome_cliente from clientes c
left join pedidos v on c.id_cliente = v.id_cliente
where v.id_produto is null;







