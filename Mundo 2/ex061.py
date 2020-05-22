print('='*40)
print('{:^40}'.format('10 TERMOS DE UMA P.A'))
print('='*40)
c = 1
a1 = int(input('Entre com o primeiro termo da PA: '))
r =  int(input('Entre com a razão: '))
while(c != 11):
    an = a1 + (c-1)*r
    print('a{} = {}'.format(c,an), end='; ')
    c += 1
print('\nFIM')