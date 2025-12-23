create database sql11;
use sql11;

CREATE TABLE Customers (
CustomerID INT PRIMARY KEY,
CustomerName VARCHAR(100),
Email VARCHAR(100),
City VARCHAR(50)
);

CREATE TABLE Products (
ProductID INT PRIMARY KEY,
ProductName VARCHAR(100),
Category VARCHAR(50),
Price VARCHAR(20)
);

CREATE TABLE Orders (
OrderID INT PRIMARY KEY,
CustomerID INT,
ProductID INT,
OrderDate VARCHAR(20),
Quantity INT,
Total VARCHAR(20)
);

INSERT INTO Customers VALUES
(1, 'Ana Silva', 'ana@email.com', 'São Paulo'),
(2, 'ana silva', 'ana@email.com', 'São Paulo'), 
(3, 'Carlos Souza', NULL, 'Rio de Janeiro'),
(4, 'Mariana Lima', 'mariana@email.com', NULL),
(5, 'JOÃO PEREIRA', 'joao@email.com', 'Curitiba');

INSERT INTO Products VALUES
(1, 'Notebook Dell', 'Eletrônicos', '3500.00'),
(2, 'notebook dell', 'Eletrônicos', '3500'),
(3, 'Mouse Logitech', 'Periféricos', NULL),
(4, 'Teclado Mecânico', 'Periféricos', '450.50');

INSERT INTO Orders VALUES
(1, 1, 1, '2024-01-10', 1, '3500'),
(2, 2, 1, '10/01/2024', 1, '3500'),
(3, 3, 3, '2024-02-05', 2, NULL),
(4, 4, 4, NULL, 1, '450.50');

# manipular um texto para comparações
# lower() - transforma tudo em letras minusculas
# having - where das comparações ou agregações

# contagem de nomes duplicados
create view vw_contagem_nomes1 as 
select lower(CustomerName) as Nomes, 
coalesce(email, "sem email cadastrado"), 
coalesce(city, "sem cidade cadastrada"),
count(*) as Total
from customers 
group by lower(CustomerName), email, city;

select * from vw_contagem_nomes1;

insert into customers value
(10,"ana silva", "ana@email.com", "Rio de Janeiro"); 

# relatório com o email de todos os clientes

create view vw_email_cadastrados as 
select * from customers where email is not null;

select * from vw_email_cadastrados;

select * from products;

describe products; # ISSO AQUI É IMPORTANTE

# cast - moldar
create view vw_produtos as
select productid, productname, category,
cast(price as decimal(10,2)) as Preco
from products where  price is not null;

select * from vw_produtos;

# exibir todos os produtos sem duplicatas e sem valores nulos, com os preços em decimal

create view vw_tarefa2 as
select lower(productname) as Nomes, cast(price as decimal(10,2)) as Preco, category,
count(*) as Total
from products 
where price is not null
group by Nomes, Preco, category;

select * from vw_tarefa2;

# quero exibit a tabela:
# id_pedido | nome_cliente | cidade | produto | categoria | data_compra | quantidade | faturamento
# regras:
# preco em decimal
# converter as datas para datas 
# sem duplicatas
# sem nulos 

# minha tarefa
select o.orderid, lower(c.customername) as Nomes, c.city, p.productname, p.category, cast(o.orderdate as date) as DataCompra, o.quantity, cast(p.price as decimal(10,2))*o.quantity as faturamento
from orders o
join products p on o.productid = p.productid
join customers c on o.customerid = c.customerid
where o.orderdate and cast(p.price as decimal(10,2))*o.quantity and c.city is not null;

# correto
select distinct o.orderid as id_pedido, 
c.customername as nome_cliente,
c.city as cidade,
p.productname as produtos,
p.category as categoria,
#cast(o.orderdate as date) as data_compra,
CASE
    WHEN o.OrderDate LIKE '%/%'
        THEN STR_TO_DATE(o.OrderDate, '%d/%m/%Y')
        ELSE STR_TO_DATE(o.OrderDate, '%Y-%m-%d')
    END AS data_compra,
o.quantity as quantidade,
cast(p.price as decimal(10,2))*o.quantity as faturamento
from orders o
join customers c on o.customerid = c.customerid
join products p on p.productid = o.productid
where o.orderdate is not null 
and cast(p.price as decimal(10,2))*o.quantity is not null;



