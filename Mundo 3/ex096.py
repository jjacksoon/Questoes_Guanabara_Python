def area(larg,comp):
    a = larg*comp
    print(f'A área do terreno {larg} x {comp} é: {a} m²')
    print('\nFIM')


# PROGRAMA PRINCIPAL
print('-='*20)
print(f'{"CONTROLE DE TERRENOS":^40}')
print('-='*20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l,c)
