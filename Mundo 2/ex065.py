n = cont = soma = maior = menor = 0
op = 'S'
while(op == 'S'):
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
    if(cont == 1):
        maior = menor = num
    else:
        if(num > maior):
            maior = num
        if(num < menor):
            menor = num
    op = str(input('Deseja continuar? [S/N]: ')).strip().upper()
media = soma/cont
print('\nA média entre os {} números digitados foi {}!'.format(cont, media))
print('O maior valor digitado foi {} e o menor foi {}'.format(maior,menor))