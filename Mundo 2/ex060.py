cont = 1
f = 1
aux = 1
fatorial = 0
num = int(input('Digite o número: '))
if(num == 0 or num == 1):
    print('\nO fatorial de {} é 1'.format(num))
else:
    while(num != cont):
        aux = num - cont
        cont += 1
        f = f*aux
    fatorial = num*f
    print('\nO fatorial do número {}! é: {} '.format(num,fatorial))
print('---FIM---')