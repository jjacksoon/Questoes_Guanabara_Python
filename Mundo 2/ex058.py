#PROGRAMA DE ADIVINHAÇÃO
cont = 0
cont_errado = 0
from random import randint
nd = 11
print('\n=====PENSEI EM UM NÚMERO DE 1 A 10. TENTE ADIVINHÁ-LO!=====')
np = randint(0,10) #numero pensado
while np != nd:
    nd = int(input('\nDigite o número que acha que pensei: '))
    if(nd > 10):
        print('NÚMERO INVÁLIDO. TENTE NOVAMENTE!')
        cont_errado += 1
    else:
        print('Esse não foi o número pensado. Tente novamente!')
    cont += 1
    if np == nd:
        print('Parabéns. Você acertou. Eu pensei no número {} e você acertou com {} palpites'.format(nd, cont - cont_errado))
print('==FIM==')
