# vamos tentar descobrir ips de sites
# socket - comunicação entre maquinas

import socket 
site = input('digite o nome do site - google.com: ')
try:
    ip = socket.gethostbyname(site)
    # tudo na internet tem um hostname
    print(ip)
except socket.gaierror:
    # se nao funcionar ele me diz o erro
    print('deu erro')