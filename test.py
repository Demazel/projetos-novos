import numpy as np
# numpy é a biblioteca numerica que o sistema vai usar

dados_idade = np.array([23, 21, 25, 30, 22, 21, 33, 45, 32, 24, 19, 10])

# a funcao np.array - criar conjunto de dados

print(np.sum(dados_idade))
print(len(dados_idade))

# media
print(np.mean(dados_idade))

# mediana
print(np.median(dados_idade))


import pandas as pd

df_idades = pd.DataFrame({"Idades":dados_idade})
print(df_idades)

print('media')
print(df_idades["Idades"].mean())
print(df_idades["Idades"].median())
print(df_idades["Idades"].mode()[0])
# para tirar a media no pandas preciso chamar o dataframe, a lista e usar o comando media - mean
