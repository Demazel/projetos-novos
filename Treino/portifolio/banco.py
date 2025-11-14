def main():
    
    conta = 0
    
    while True:
        
        print("Bem-Vindo ao Banco")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Ver saldo")
        print('4 - Sair')
        
        u = int(input("Selecione a opcao desejada: "))
    
        if u == 1:
            d = int(input('qual valor voce deseja depositar: '))
            
            if d <= 0:
                print('valor invalido')
            else:    
                conta += d
        
        elif u == 2:
            s = int(input('qual valor voce deseja sacar:'))
        
            if s > conta:
                print('Saldo insuficiente')
            elif s <= 0:
                print('valor invalido')
            else:
                conta -= s
    
        elif u == 3:
            print(f'voce possui R$ {conta}')
        
        elif u == 4:
            print("Saindo do programa")
            break
                      
if __name__=="__main__":
    main()