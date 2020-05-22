s = 0
for c in range (1,7):
    n = int(input('Entre com o {}º valor: '.format(c)))
    if(n % 2 == 0):
        s += n
print('-='*15)
print('          A soma é: {}'.format(s))
print('-='*15)
