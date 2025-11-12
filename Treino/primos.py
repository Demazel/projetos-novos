import math

def main():
    
    print("Bem-vindo ao programa dos primos, um programa no qual voce digita um numero e ele diz se é primo ou não")
    
    n1 = int(input("Digite um número: "))
    
    if n1 < 2:
        print("Numeros menores que 2 nao sao primos")
        return
    
    limite = int(math.sqrt(n1)) + 1
    
    for i in range (2, limite):
        if n1 % i == 0:
            print(f"{n1} nao eh um numero primo")
            return 
        
    print(f"{n1} eh primo")
    
if __name__ == "__main__":
    main()