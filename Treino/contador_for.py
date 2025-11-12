def new():
    
    pares = [str(numero) for numero in range (2 ,101, 2)]
    print(end = ", ".join(pares))

if __name__ == "__main__":
    new()