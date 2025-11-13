# uma lista eh uma "variavel" que suporta muitos dados

def main():
    
    frutas = []
    # quando eu coloco uma lista apenas com [], eu estou dizendo que ela eh vazia
    
    # o usuario pode add valor a lista
    # pode excluir a lista
    # pode ver a lista
    # e pode sair da lista
    
    
    
    
    # APPEND adiciona um novo elemento na lista
    # POP exclui elemento da lista
    
    
    
    print("------ bem vindo ao varejao gen ------")
    
    print("suas opcoes sao:")
    print('1 - adicionar fruta')
    print('2 - excluir fruta')
    print('3 - ver lista')
    print('4 - sair')
    
    op = int(input('escolha sua opcao: '))
    
    if op > 4 or op < 1:
        print('ERRO: numero invalido, finalizando o sistema')
    else:
        while op > 0:
            
            # caso 1 - add
            if op == 1:
                nova_fruta = input('qual fruta deseja adicionar? ')
                # para eu adicionar um elemento na lista eu deco chamar a lista e dar o atributo append anexando assim, o novo valor
                frutas.append(nova_fruta)
                print('fruta', frutas[-1], 'adicionada com sucesso')
                op = int(input('escolha sua opcao: '))
            
            # caso 2 - excluir
            elif op == 2:
                for posicao, cada_fruta in enumerate(frutas, start=1):
                    print(posicao, ' - ', cada_fruta)
                print('agora voce pode excluir um produto')
                posicao_fruta = int(input('digite a posicao da fruta'))
                frutas.pop(posicao_fruta - 1)
                # o comando pop eh para excluir um item da lista basesado em sua posicao
                print('Fruta excluida com sucesso')
                op = int(input('escolha sua opcao: '))
            
            # caso 3 - ver lista
            elif op == 3:
                for nome_frutas in frutas:
                    print(nome_frutas)
                op = int(input('escolha sua opcao: '))
            
            # caso 4 - sair
            elif op == 4:
                print('finalizando o programa...')
                return

if __name__=="__main__":
    main()