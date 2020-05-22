while True:
    print(50*'-')
    n = int(input('Digite o número para mostrar a TABUADA: '))
    print(50*'-')
    if(n < 0):
        break
    print(f'====TABUADA DO NÚMERO {n}====')
    for c in range (0,11):
        print(f'{n} x {c} = {n*c}')
print('\nPROGRAMA TABUADA ENCERRADO COM SUCESSO. Volte sempre!')
print('\n---FIM---')
