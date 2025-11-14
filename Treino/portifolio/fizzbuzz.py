# Autor: Henrique
# Projeto: FizzBuzz

# Caso definindo um limite e colocando os resultados em lista

def main():
    
    limite = int(input('Até quanto você quer contar? '))
    r = []
    
    for c in range(1, limite + 1):
        if c % 5 == 0 and c % 3 == 0:
            r.append('FizzBuzz')
        elif c % 5 == 0:
            r.append('Buzz')
        elif c % 3 == 0:
            r.append('Fizz')
        else:
            r.append(str(c))
    print(', '.join(r))
    
# Caso escolhendo um número

def other():
    
    n = int(input("Digite um número: "))
    
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(f"{n} não é nem Fizz, nem Buzz e nem Fizzbuzz")

# Caso usando WHILE

def enquanto():
    
    numero = 1

    while numero <= 100:
        if numero % 5 == 0 and numero % 3 == 0:
            print("FizzBuzz")
        elif numero % 3 == 0:
            print("Fizz")
        elif numero % 5 == 0:
            print("Buzz")
        else:
            print(numero)
        numero = numero + 1
    print("")
    print("")
    print(" ---------- FIM -----------")
    
    
# Caso usando FOR
   
def por():
     
    for i in range(1, 101):
        if i % 5 == 0 and i % 3 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
    print("")
    print("")
    print(" ---------- FIM -----------")         
                
if __name__ == "__main__":
    main()
    other()
    enquanto()
    por()