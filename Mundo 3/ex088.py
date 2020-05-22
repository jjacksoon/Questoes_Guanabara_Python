from random import randint
from time import sleep
aux = 0
palpite = []
jogo = []
qtd = int(input('Quantos jogos você deseja fazer?: '))
while(aux < qtd):
    for c in range(0,6):
        palpite.append(randint(1,60))
        palpite.sort()
    jogo.append(palpite[:])
    palpite.clear()
    aux += 1
print('-='*20)
print(f'       PALPITES PARA SUAS {qtd} APOSTAS')
print('-='*20)
print()
for c,v in enumerate(jogo):
    print(f'    Jogo {c+1}: {v}')
    sleep(1)
print(f'\n{"<BOA SORTE!>":=^40}')
