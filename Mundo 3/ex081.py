lista = []
cont = 0
while True:
    n = int(input('Digite um numero: '))
    lista.append(n)
    cont += 1
    op = ' '
    while op not in 'SN':
        op = str(input('Deseja continuar? [S/N]: ')).upper()
    if op == 'N':
        break
lista.sort(reverse = True)
print('-='*30)
print(f'Você digitou {cont} números!')
print(f'Lista em ordem decrescente: {lista}')
if(lista.count(5)> 0):
    print('O númeto 5 foi digitado na lista e encontra-se nas posições', end=' ')
else:
    print('O número 5 não encontra-se na lista')
for c,v in enumerate(lista):
    if(lista[c] == 5):
        print(c, end=' ')
print()
print('-='*30)
