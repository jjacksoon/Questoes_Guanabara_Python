valores = []
while True:
    n = int(input('Digite um valor: '))
    if valores.count(n) == 0:
        valores.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado. Não vou adicionar!')
    op = ' '
    while op not in 'SN':
        op = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if op == 'N':
        break
valores.sort()          #ORDENA A LISTA EM ORDEM CRESCENTE
print('-='*30)
print(f'Você digitou os valores {valores}')
