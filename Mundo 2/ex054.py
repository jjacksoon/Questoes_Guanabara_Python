from datetime import date
from time import sleep
s1 = 0          #Total de maiores de idade
s2 = 0          #total de menores de idade
ano = date.today().year
for c in range (0,7):
    p = int(input('Ano de nascimento da pessoa {}: '.format(c+1)))
    idade = ano - p
    if (idade >= 21):
        s1 += 1
    else:
        s2 += 1
print('\nAnalisando...')
sleep(3)
print('\nMAIORES DE IDADE: {}'.format(s1))
print('\nMENORES DE IDADE: {}'.format(s2))
print('\nFIM')