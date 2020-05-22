op = 0
maior = 0
op_add = 'S'
n1 = float(input('Digite o valor do primeiro número: '))
n2 = float(input('Digite o valor do segundo número: '))
print('{:=^40}'.format('MENU'))
print('''\n[1] - SOMAR
[2] - MULTIPLICAR
[3] - MAIOR
[4] - NOVOS NÚMEROS
[5] - SAIR DO PROGRAMA''')

op = int(input('\nDIGITE A OPÇÃO DE OPERAÇÃO QUE DESEJA REALIZAR: '))
while(op > 5):
    print('\nOPÇÃO INVÁLIDA. TENTE NOVAMENTE!')
    op = int(input('\nDIGITE A OPÇÃO DE OPERAÇÃO QUE DESEJA REALIZAR: '))
if(op == 1):
    soma = n1 + n2
    print('\nA soma dos números {} e {} é: {}'.format(n1,n2,soma))
elif(op == 2):
    multiplica = n1*n2
    print('\nA multiplicação dos números {} e {} é: {}'.format(n1,n2,multiplica))
elif(op == 3):
    if(n1 > n2):
         maior = n1
    else:
        maior = n2
        print('\nO maior valor entre os dois números digitados é: {}'.format(maior))
elif(op == 4):
    while (op_add == 'S'):
        n = float(input('Digite um novo valor: '))
        op_add = str(input('\nDeseja acrescentar outro valor? [S/N]: ')).upper()
elif(op == 5):
    print('\nPROGRAMA FINALIZADO!')
print('\n---FIM---')
