def main():
    # Peça ao usuário para digitar um número inteiro positivo N.
    # Calcule e mostre a soma de todos os números de 1 até N
    
    n = int(input("digite um numero:"))
    
    if n < 1:
        print(f"o numero {n} nao pode ser menor que 1")
        return
    
    soma = 0
    
    for i in range (1, n + 1):
        soma += i
        print(soma)
          
if __name__ == "__main__":
    main()