lista = [[],[]]
for c in range (1,8):
    n = int(input(f'Digite o {c}º valor: '))
    if(n % 2 == 0):
        lista[0].append(n)
    else:
        lista[1].append(n)
print('-='*30)
lista[0].sort()
lista[1].sort()
print(f'Lista com números PARES: {lista[0]}')
print(f'Lista com números IMPARES: {lista[1]}')