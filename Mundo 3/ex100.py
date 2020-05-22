from random import randint
from time import sleep
def sorteia(lista):
    print(f'Sorteando 5 valores: ', end='')
    for i in range(0,5):
        lista.insert(i, randint(0,10))
        print(f'{lista[i]}', end=' ', flush= True)
        sleep(0.5)

def somapar(lista):
    print(f'Somando o valores pares de {lista}, temos: ', end ='')
    s = 0
    for v in lista:
        if(v % 2 == 0):
            s += v
    print(s)


numeros = []
print('-='*30)
sorteia(numeros)
print()
somapar(numeros)