lista = []
p = []
i = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    if(n % 2 == 0):
        p.append(n)
    else:
        i.append(n)
    op = ' '
    while op not in 'SN':
        op = str(input('Deseja continuar? [S/N]: ')).upper()
    if(op == 'N'):
        break
print('=-'*30)
print(f'Lista completa: {lista}')
print(f'Lista com valores PARES: {p}')
print(f'Lista com valores ÍMPARES: {i}')
print('=-'*30)
