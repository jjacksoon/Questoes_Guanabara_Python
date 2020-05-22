from random import randint
soma = vencer = 0
print(20*'-=')
print('{:^40}'.format('VAMOS JOGAR PAR OU ÍMPAR!'))
print(20*'-=')
while True:
    n_j = int(input('\nDigite um valor: '))
    n_m = randint(0,10)   
    soma = n_j + n_m
    op_j = ' '     
    while(op_j not in 'PI'):                                    #ESTABELECIMENTO DE UM INTERVALOR DE VALORES PARA ESCOLHA DA MÁQUINA
        op_j = str(input('\nPar ou ímpar?[P/I]: ')).strip().upper()[0]
    if(op_j == 'P'):
        if(soma % 2 == 0):
            print(f'Você jogou {n_j} e o computador {n_m}. Total de {soma} DEU PAR!')
            print('Você VENCEU!')
            vencer += 1
        else:
            print('\nVocê PERDEU!')    
            break
    elif(op_j == 'I'):
        if(soma % 2 == 1):
            print('Você VENCEU!')
            vencer += 1
        else:
            print('Você PERDEU!')
            break
    print('\nVamos jogar novamente...')
print('\n---GAME OVER!---')
print(f'Você jogou {n_j} e o computador {n_m}. Total de {soma} DEU ÍMPAR!')
print(f'Você venceu {vencer} vezes')

