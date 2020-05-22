from time import sleep
def ajuda(f):
        print(f'Acessando o manual do {f.upper()}')
        print('~'*30)
        sleep(0.5)
        help(f)

def titulo(msg):
    tam = len(msg) + 4
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)

funcao = ' '
while True:
    titulo('SISTEMA DE AJUDA PYHELP')
    funcao = str(input('digite uma função: ')).strip()
    if(funcao.upper() == 'FIM'):
        break
    else: 
        ajuda(funcao)
titulo('ATÉ LOGO')