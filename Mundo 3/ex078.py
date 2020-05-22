lista = []
for c in range(0,5):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))
print('-='*20)
print(f'Lista digitada: {lista}')
print(f'\nmaior valor: {max(lista)} nas posições', end=' ')
for c,v in enumerate(lista):
    if(v == max(lista)):
        print(c, end=' ')
print(f'\nmenor valor: {min(lista)} nas posições', end=' ')
for c,v in enumerate(lista):
    if(v == min(lista)):
        print(c, end=' ')
print()
print('-='*20)