def menu():
    print('\nBem-vindo ao protein-cal-gen')
    print("Escolha um opcao:")
    print("1 - calcular proteinas")
    print("2 - calcular IMC")
    print("qualquer outro numero - sair")

# funcao para saber o objetivo do usuario
def menu_objetivo():
    print("Qual sua meta?")
    print("1 - Perde peso")
    print("2 - Manter peso")
    print("3 - Ganhar peso")

def calc_proteinas(peso, objetivo):
    if objetivo == 1:
        return peso * 2
    elif objetivo == 2:
        return peso * 1.6
    elif objetivo == 3:
        return peso *1.8
    else:
        return None
    # o comando none eh para nao fazer nada

def calc_imc(peso, altura):
    return peso / (altura**2)

def imc(valor_imc):
    if valor_imc < 18.5:
        return 'abaixo do peso'
    elif valor_imc < 24.9:
        return "com o peso normal"
    elif valor_imc < 29.9:
        return 'em sobre peso'
    else:
        return "obeso"