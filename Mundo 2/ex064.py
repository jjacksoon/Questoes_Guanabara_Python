c = num = soma = 0
num = int(input('\nEntre com o valor [999 para parar]: '))
while (num != 999):
    c += 1
    soma += num
    num = int(input('\nEntre com o valor [999 para parar]: '))
print('\nA soma dos {} números digitados antes de 999 foi {}'.format(c,soma))
print('\n---FIM---')
