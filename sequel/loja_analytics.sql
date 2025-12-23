create database	loja_analytics;
use loja_analytics;

show tables;

# quero fazer consultas 
# quero mostrar id_venda, quantidade de venda
select id_venda, quantidade from vendas;

# nome_produto, preco
select nome_produto, preco from produtos;

# vamos relacionar tabelas
# exibir id_venda, nome_produto, preco, quantidade, faturamento
select v.id_venda, p.nome_produto, p.preco, v.quantidade, p.preco * v.quantidade as faturamento
from vendas v join produtos p on v.id_produto = p.id_produto;

# nome do cliente, nome do produto, quanto o cliente gastou
# onde o gasto foi maior que 1000
select c.nome as Nome_do_Cliente, p.nome_produto as Nome_do_Produto, p.preco * v.quantidade as Quanto_o_Cliente_Gastou
from vendas v 
join produtos p on v.id_produto = p.id_produto 
join clientes c on v.id_cliente = c.id_cliente 
where p.preco * v.quantidade > 1000;

# funcoes de agregacao
# count() = contagem
# sum() - soma
# avg () - media
# min () - minimo
# max() - max

select count(*) as total_vendas from vendas;

# contagem comparativa
select count(id_cliente) from vendas;

# faturamento total das vendas
select sum(v.quantidade * p.preco) as faturamento_total_das_vendas
from vendas v 
join produtos p on v.id_produto = p.id_produto;

select avg(preco) as preco_medio from produtos;

# ticket medio
select avg(p.preco * v.quantidade) as ticket_medio
from vendas v
join produtos p on v.id_produto = p.id_produto;

# menor preco e maior preco
select min(preco) as menor_preco, max(preco) as maior_preco 
from produtos;

select * from produtos order by nome_produto desc;







