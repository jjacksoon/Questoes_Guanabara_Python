cont = soma = 0
while True:
    n = int(input('\nDigite o número (999 - parar): '))
    if(n == 999):
        break
    cont += 1
    soma += n
print(f'\nForam digitados {cont} números e a soma deles foi {soma}')
