matriz = [[],[],[]]
soma = soma3 = maior = 0
for i in range(3):
    for j in range(3):
        matriz[i].append(int(input(f'Digite o valor [{i},{j}]: ')))
        if(j==2):
            soma3 += matriz[i][2]
maior = max(matriz[1])
print('-='*15)
for i in range(3):
    for j in range(3):
        print(f'[{matriz[i][j]:^5}]', end=' ')
        if(matriz[i][j] % 2 == 0):
            soma += matriz[i][j] 
    print()

print('-='*20)
print(f'\nA soma de todos os número pares digitados é: {soma}')
print(f'A soma de todos os número da 3º COLUNA é: {soma3}')
print(f'O maior valor da segunda coluna é {maior}')