# revisao 1 - dados - pandas - sql - excel

# contexto de armazenamento de dados
# criar variaveis
# ja inserido no sistema

nome = "python" # string
cidade = input("informe o nome da sua cidade") # string

idade = 31 # int
ano = int(input("informe o ano que voce nasceu")) #int

altura = 1.73 # float - decimal 
altura1 = float(input("qual sua altura"))

# listas (armazenar diversos dados em uma variavel)
# dicionarios (guardar chaves e valores)
# combinacao de lista com dicionario (crio uma ideia de tabela)

# lista
frutas = ["banana", "maca", "laranja"]
print(frutas[1])

nova_fruta = input("informe o nome da nova fruta")
# que para adicionar um novo valor em uma lista eu uso o metodo append
frutas.append(nova_fruta)

# quero apagar um registro da lista
frutas.pop(-1)

# dicionario
pessoa = {
    "nome":"luiz",
    "idade":31,
    "cidade":"iguape"
}

print(pessoa["nome"])

# -------------- caso 1 - criando um dataset com listas e dicionarios -----------------

alunos = {
    "nome":["Samuel", "Robson","Carrie", "Eric", "Rafael", "Batista", "Sabrina", "Henrique", "Luiz"],
    "idade":[20,21,22,23,24,25,26,27]
}
print(alunos["nome"][3])

# parte 2 conceitos