p = 0       #PRIMEIRO TERMO                                       #PRIMEIRO TERMO SEMPRE SERÁ ZERO
a1 = 0      
a2 = 1      #SEGUNDO TERMO
f = 0
c = 0
num = int(input('Quantidade de termos: '))
print('{:=^40}'.format('SEQUÊNCIA DE FIBONACCI'))
print(p, end=' ')
while ( c < num - 1):
    a1 = a2
    a2 = f
    f = a1 + a2
    c += 1
    print(f, end=' ')
print('\n{:=^40}'.format('FIM'))
