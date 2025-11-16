#para eu ler uma base de dads
#preciso importar o modelo que le 
import csv

#agora eu vou dizer onde esta o arquivo que vou ler
#digo o caminho (path) do arquivo
caminho_arquivo = '/Users/user1/Desktop/projetos-novos/musicas/assents/musicas.csv'

#para criar uma função coloco:
#instrução "def" + "nome da função():"
def ler_musicas():
    print('----- LISTA DE MUSICAS -----')
    try:
        #comando try serve para o sistema 
        #tentar executar uma ou mais instruções
        #se der certo ok, 
        #se não der certo exibe uma mensagem de erro
        with open(caminho_arquivo,'r',encoding='utf-8') as arquivo_musica:
            #o comando with open permite que abra algo 
            #mas par aisso deve informar:
            #1- onde está
            #2- o modo abertura(ler=r; adicionar=a; reescerver=w)
            #3- não obrigatorio - colocar como quer ler (codificação)
            #depois dar um apelido para essa instrução
            leitor = csv.reader(arquivo_musica)
            #leitor p/ o sistema, le csv, adicionei metodo reader p/ ler o arquivo
            next(leitor)
            #o comando next pula a primeira linha do arquivo(cabeçalho)
            
            #agora quero exibir linha por linha do que o leitor viu
            for cada_linha in leitor: 
                if cada_linha:
                    titulo,artista,ano,genero,duracao_segundos = cada_linha
                    #tenho que falar todos os cabeçalhos do meu arquivo
                    print(titulo,'|',artista,'|',ano, '|', genero)

    except FileNotFoundError:
        print('erro')