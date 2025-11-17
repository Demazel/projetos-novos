import pandas as pd
# import eh para chamar a biblioteca para o sistema
# nome da biblioteca
# as bla bla bla - para apelidar a biblioteca

# df quer dizer data frame
df_alunos = pd.read_csv('alunos.csv')
# caso o separador não é ',' - voce arruma com o argumento sep = ''
# caso ele nao reconhe;a os operadores digitados, alteramos com o arg encoding='' geralmente é utf-8
# pd.read_csv - faz com que o pandas leia o arquivo csv para o python
print(df_alunos)

# add novo valor no data frame
# em geral no data frame tem muitos campos
# se o python le o data frame como chave-valor - posso utilizar dicionario para add valores

novo_aluno = {
    "Carimbo de data/hora": '17/11/2025 10:33:42',
    'nome':'luiz',
    'cidade':'iguape',
    'zona':'centro'
}

# add dado
# df_alunos = df_alunos._append(novo_aluno, ignore_index = True)
df_alunos = pd.concat([df_alunos, pd.DataFrame([novo_aluno])], ignore_index= True)
# para adicionar um novo valor, devo chamar o dataframe e atribuir a ele
# a funcao concat da biblioteca (pd.concat) e chamar os atributos
# [meu frame e o novo dado] = [df_alunos, pd.DataFrame([novo_aluno])]
# salvar a info
df_alunos.to_csv('alunos.csv', index = False)

