
matriz = [[],[],[]]
for i in range(3):
    for j in range(3):
        matriz[i].append(int(input(f'Digite o valor [{i},{j}]: ')))
print('-='*15)
for i in range(3):
    for j in range(3):
        print(f'[{matriz[i][j]:^5}]', end=' ')
    print()
