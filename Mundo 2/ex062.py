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
op = str(input('\nDeseja mostrar mais algum(ns) termo(s)?[S/N]: ')).upper()
if(op == 'S'):
    qtd = int(input('Quantos termos deseja?: '))
    novo = c + qtd                                                              #NOVA QUANTIDADE DE TERMOS A SEREM MOSTRADOS
    print('---Novos termos pedidos:--- ')
    while(c != novo):
        an = a1 + (c-1)*r
        print('a{} = {}'.format(c,an), end='; ')
        c += 1   
else:
    print('\nPROCESSO FINALIZADO. PARABÉNS!')
print('\nFIM')
