use labsql8;

# Tarefa 1. Obtenha todos os pedidos de produtos que custam mais de US$ 25, exibindo o OrderID, ProductID, Quantity e Total.
select orderid as OrderID, productid as Product, quantity as Quantity, Total
from orders 
where total > 25;

# Tarefa 2. Liste cada cliente e a quantidade total de produtos solicitados, ordenados pela maior quantidade total.
select c.customername as Cliente, sum(o.quantity) as Total_produtos_selecionados
from orders o
join customers c on o.CustomerID = c.CustomerID
group by Cliente
order by Total_produtos_selecionados desc;
 
# Tarefa 3. Exiba o nome de cada produto, seu total de vendas e classifique-o como "High Revenue" (Receita Alta) se o total de vendas exceder US$ 300, caso contrário, "Low Revenue" (Receita Baixa).
 select p.productname as Nome_Produto, o.total as Total,
 case
	when o.total > 300 then "High Revenue"
    else "Low Revenue"
end as Receita
 from orders o
 join products p on o.ProductID = p.ProductID;
 
# Tarefa 4. Encontre clientes que fizeram pelo menos dois pedidos em dezembro de 2023, com cada pedido totalizando mais de US$ 100. Exiba seus nomes e o número de pedidos qualificados.
select count(o.orderid) as Pedidos, c.customername
from orders o
join customers c on o.CustomerID = c.CustomerID
where o.OrderDate between '2023-12-01' and '2023-12-31' and total > 100
group by c.CustomerName having count(c.CustomerName) >=2 ;
 
# Tarefa 5. Liste cada pedido com os três primeiros caracteres do nome do cliente, o nome do produto e o valor total do pedido.
select left(c.CustomerName,3) as char_cliente, p.ProductName, o.Total
from Orders o
join Customers c on o.CustomerID = c.CustomerID
join Products p on o.ProductID = p.ProductID;





