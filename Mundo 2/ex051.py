print('='*40)
print('{:^40}'.format('10 TERMOS DE UMA P.A'))
print('='*40)
a1 = int(input('Entre com o primeiro termo da PA: '))
r =  int(input('Entre com a razão: '))
for c in range (1,11):
    an = a1 + (c-1)*r
    print('a{} = {}'.format(c,an), end='; ')
print('\nFIM')