# link da API = endpoint
# endpoint eh um link para os metodos get e post
# ex: https://api.open-meteo.com/v1/forecast

# sempre que eu uso api em python devo chamar a biblioteca de requisicoes = pip install requests

# sempre que queremos mostrar graficos, podemos usar a biblioteca matplotlib = pip install matplotlib

import requests
import matplotlib.pyplot as plt

# criar uma funcao chamada de buscar_clima

def buscar_clima(latitude, longitude):
    # deve infomar o endpoint
    endpoint = 'https://api.open-meteo.com/v1/forecast'
    # informar os parametros para o sistema em formato de dicionario. Dicionario trabalha com chave: valor
    parametros = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "temperature_2m",
        "timezone": "America/Sao_Paulo"         
    }
    resposta = requests.get(endpoint, params=parametros)
    # sempre que queremos obter a resposta usamos o comando requests.get para pegar os valores e colocamo os atributos requests.get(endpoint, params=dicionario)
    
    # para o sistema usar o metodo post - para mostrar as informacoes
    dados = resposta.json()
    # o sistema transforma os dados em json para poder manipular eles
    return dados

latitude = float(input("Qual a latitude? "))
longitude = float(input("Qual a longitude? "))

dados = buscar_clima(latitude, longitude)
# vamos comecar a exibbir informacoes para o usuario

horas = dados['hourly']['time']
temperatura = dados["hourly"]["temperature_2m"]

plt.plot(horas, temperatura)
# plt.plot cria um grafico, onde informo como parametro primeio o eixo x e depois o eixo y
plt.title("Temperatura por hora")
# para ver o grafico
plt.show()