tupla = (int(input('Digite um valor: ')),
        int(input('Digite um valor: ')),
        int(input('Digite um valor: ')),
        int(input('Digite um valor: ')), )
par = 0
print(f'\nVocê digitou os valores {tupla}')
if(tupla.count(9) == 0):
    print('\nO valor 9 não aparece na tupla digitada!')
else:
    print(f'\nO valor 9 aparece na tupla {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'\nO valor 3 foi digitado a primeira vez na posição {tupla.index(3)+1}')
else:
    print('\nO número 3 não aparece na tupla digitada!')
print('\nOs valores pares digitados foram: ',end='')
for c in tupla:
    if(c % 2 == 0):
        print(c, end=' ')
