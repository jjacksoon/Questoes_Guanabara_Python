tabela = ('Arroz', 10,
        'Feijão', 20,
        'Macarrão', 30,
        'Melancia', 4.50)
print('-='*23)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-='*23)
for c in range(0, len(tabela)):
    if c % 2 == 0:
        print(f'{tabela[c]:.<35}', end=' ')
    else:
        print(f'R${tabela[c]:.2f}')
print('-'*47)