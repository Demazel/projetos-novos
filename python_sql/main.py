# INTEGRACAO DE MYSQL COM SCRIPTS EM PYTHON

from funcoes import *
# para usar mysql com python - mysql.connector

while True:
    print('1- ver produtos')
    print('2- ver costumers')
    print('3- ver orders')
    print('4- cadastrar products')
    print('5- cadastrar customers')
    print('6- cadastrar orders')
    
    opcao = input('informe a opcao desejada')
    
    if opcao == '1':
        mostrar_tabela('products')
    elif opcao == '2':
        mostrar_tabela('customers')
    elif opcao == '3':
        mostrar_tabela('orders')
    elif opcao == '4':
        inserir_products()
    elif opcao == '5':
        inserir_customers()
    elif opcao == '6':
        inserir_orders()
    else:
        print('tchau')
        break
    
# desligar o banco de dado ao finalizar o sistema
cursor.close()
conexao.close()