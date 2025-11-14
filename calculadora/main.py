from funcoes import *
# * = all

def menu():
    print('Gen - Calc')
    print('1 - Somar')
    print('2 - Substrair')
    print('3 - Multiplicar')
    print('4 - Dividir')
    print('5 - Potencia')
    print('6 - Raiz')
    print('Qualquer outro numero - sair')
    

# Vou criar a funcao principal de todo o sistema
if __name__=='__main__':
# garante que o codigo so rode quando voce executar o main.py
    menu()
    opcao = input('Escolha uma opcao: ')
    
    num_menu = ['1', '2', '3', '4', '5', '6']
    
    if opcao not in num_menu:
        print('saindo do sistema...')
    else:   
        num1 = float(input('digite o numero 1: '))
        num2 = float(input('digite o numero 2: '))
    
        if opcao == "1":
            print(soma(num1, num2))
        elif opcao == "2":
            print(subtracao(num1, num2))
        elif opcao == "3":
            print(multiplicacao(num1, num2))
        elif opcao == "4":
            print(divisao(num1, num2))
        elif opcao == "5":
            print(potencia(num1, num2))
        elif opcao == "6":
            print(raiz(num1, num2))
        else:
            print('saindo do sistema...')