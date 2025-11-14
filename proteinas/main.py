from funcoes import *

while True:
    menu()
    opcao = int(input('escolha a opcao: '))

    if opcao == 1:
        menu_objetivo()
        objetivo = int(input('Qual seu objetivo? '))
        peso = float(input('qual seu peso(kg)? '))

        resultado_proteinas = calc_proteinas(peso,objetivo)
        print(f'voce preicsa de {round(resultado_proteinas,2)}')

    elif opcao == 2:
        peso = float(input('\nqual seu peso(kg)? '))
        altura = float(input('\nqual a sua altura em metros? '))
        
        if altura <= 0 or peso <= 0:
            print('\npeso ou altura invalidos')
        
        else:
            valor_imc = calc_imc(peso, altura)
            resultado_imc = imc(valor_imc)
            print(f'\nseu imc eh de {round(valor_imc,2)}, e voce esta {resultado_imc}')
    
    else:
        print('tchau')
        break