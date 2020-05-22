dado = []
pessoa = []
maior = menor = 0
while True:
    dado.append(str(input('Nome da pessoa: ')).strip().capitalize())
    dado.append(float(input('Peso(kg): ')))
    if len(pessoa) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    pessoa.append(dado[:])                      #COPIA DA LISTA DADOS NA LISTA PESSOA
    dado.clear()                                #LIMPEZA PARA RECEBER O PRÓXIMO DADO A SER DIGITADO
    op = ' '
    while op not in 'SN':
        op = str(input('Deseja continuar?[S/N]: ')).upper()
    if op == 'N':
        break
print(f'Total de pessoas cadastradas: {len(pessoa)}')
print(f'O MAIOR peso foi de {maior} kg. Peso de ', end='')
for p in pessoa:
    if p[1] == maior:
        print(f'{p[0]}', end=' ')
print()
print(f'O MENOR peso foi de {menor} kg. Peso de ', end='')
for p in pessoa:
    if p[1] == menor:
        print(f'{p[0]}', end=' ')
