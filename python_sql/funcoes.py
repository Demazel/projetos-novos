import mysql.connector
# getpass eh um modulo para mascarar a senha
import getpass
from datetime import date

# inserir no sistema as credencicias do banco de dados
user_host = input('iforme o host')
user_user = input('informe o usuario')
user_password = getpass.getpass('informe a senha')
user_db = input('Informe o banco de dados')


conexao = mysql.connector.connect(
    host = user_host,
    user = user_user,
    password = user_password,
    database = user_db
)

# para executar a conexao com o banco de dados
cursor = conexao.cursor()


def mostrar_tabela(nome_tabela):
    print(f'tabela {nome_tabela}')
    cursor.execute(f'select * from {nome_tabela}')
    # para coletar os resultados
    resultados = cursor.fetchall()
    
    # vamos obter as colunas
    colunas = [desc[0] for desc in cursor.description]
    
    # exibir os nomes das colunas
    print(' | '.join(colunas))
    # id | nome | blablabla | 
    # ----------------------------------
    print('-'*50)
    
    # exibir os dados (as linhas)
    for linha in resultados:
        print(" | ".join(str(item) for item in linha))
        # | id | nome | blablabla | 
        # ----------------------------------
        # | '1' | 'nome_cliente | 'bla bla bla' |
        # | '2' | 'nome_cliente | 'bla bla bla' |
        # | '3' | 'nome_cliente | 'bla bla bla' |
        # | '4' | 'nome_cliente | 'bla bla bla' |
        
        # o comando description coleta os cabecalhos de uma tabela
        # o comando fetchall() coleta as linhas 
        
def inserir_products():
    product_id = int(input('informe o id'))  # palceholder 1
    nome = input('infrome o nome do produto') # placeholder 2
    price = float(input('informe o preco do produto')) # placeholder 3
    
    # criar script de sql
    sql = "insert into products (productid, productname, price) values (%s, %s, %s)"
    # o %s representa um placeholder
    
    # executar o script
    cursor.execute(sql,(product_id, nome, price))
    
    # cofirmar tudo o que fizemos
    conexao.commit()
    print('dados inseridos')
    
    
def inserir_customers():
    py_customerid = int(input('informe o id'))  # palceholder 1
    py_customername = input('infrome o nome do produto') # placeholder 2
    
    sql = "insert into customers (customerid, customername) values (%s, %s)"
    
    cursor.execute(sql,(py_customerid, py_customername))

    conexao.commit()
    print('dados inseridos')
    
def inserir_orders():
    py_orderid = int(input('informe o orderid'))
    py_orderdate = date.today()
    py_customerid = int(input('informe o customerid'))
    product_id = int(input('informe o productid'))
    py_quantity = int(input('insira a quantidade'))
    py_total = float(input('insira o valor total'))
    
    sql = "insert into orders (orderid, orderdate, customerid, productid, quantity, total) values (%s, %s, %s, %s, %s, %s)"
    
    cursor.execute(sql,(py_orderid, py_orderdate, py_customerid, product_id, py_quantity, py_total))
    
    conexao.commit()
    print('dados inseridos')