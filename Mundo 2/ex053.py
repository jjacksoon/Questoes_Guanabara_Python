from time import sleep
p = str(input('Entre com a palavra ou frase: ')).upper().strip().split()
pa = ''.join(p)
tam = len(pa)
print('\nAnalisando...')
sleep(4)
for c in range (0,tam):
    a = pa[c]
for d in range (tam-1,-1,-1):
    b = pa[d]
if(pa[c] == pa[d]):
    print('\nA palavra ou frase é PALINDROMO!')
else:
    print('\nA palavra ou frase não é PALINDROMO!')
print('\nFIM')
 