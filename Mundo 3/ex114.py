import requests
try:
    resposta = requests.get('http://www.pudim.com.br')
    print('Consegui acessar o site pudim')
except:
    print('O site pudim não está acessível no momento')