def main():
    print("Bem-vindo a calculadora")
    
    numero1 = int(input("digite um numero:"))
    
    numero2 = int(input("digite outro numero:"))
    
    print("As opercoes sao 1 para adicao, 2 para subtracao, 3 para multiplicacao e 4 para divisao")
    
    operacao = int(input("escolha o numero da operacao:"))
    
    if operacao == 1:
        soma = numero1+numero2
        print(f"a soma entre os numeros {numero1} e {numero2} eh igual a", soma)
        
    elif operacao == 2:
        subtacao = numero1-numero2
        print(f"a subtracao entre os numeros {numero1} e {numero2} eh igual a",subtacao)
    
    elif operacao == 3:
        multiplicacao = numero1*numero2
        print(f"a multiplicacao entre os numeros {numero1} e {numero2} eh igual a", multiplicacao)
    
    elif operacao == 4:
        if numero2 == 0:
            print("erro: nenhum nuemro eh divisivel por zero")
        else:
            divisao = (numero1/numero2)
            print(f"a divisao entre os numeros {numero1} e {numero2} eh igual a",divisao)
    else:
        print("voce nao sdelecionou uma opcao valida")
    
if __name__ == "__main__":
    main()