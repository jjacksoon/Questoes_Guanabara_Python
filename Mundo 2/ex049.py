n = int(input('Digite o número: '))
print(5*'=','TABUADA DO NUMERO {}'.format(n),5*'=')
for c in range(0,11):
    print('{} x {:2} = {:2}'.format(n,c,c*n))
print('FIM')
