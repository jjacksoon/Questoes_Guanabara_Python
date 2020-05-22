import random
from time import sleep
op_j = str(input('\nEntre com sua opção (pedra, papel ou tesoura): ')).strip().lower()
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
lista = ['pedra','papel','tesoura']
op_c = random.choice(lista)
print('-='*20)
print('Opção do jogador: {}'.format(op_j))
print('Opção do computador: {}'.format(op_c))
print('-='*20)
if (op_j == op_c):
    print('EMPATE!\n')
elif(op_j == 'pedra' and op_c == lista[1]):
    print('VOCÊ PERDEU!\n')
elif(op_j == 'pedra' and op_c == lista[2]):
    print('VOCÊ GANHOU!\n')
elif(op_j == 'papel' and op_c == lista[0]):
    print('VOCÊ GANHOU!\n')
elif(op_j == 'papel' and op_c == lista[2]):
    print('VOCÊ PERDEU!\n')
elif(op_j == 'tesoura' and op_c == lista[0]):
    print('VOCÊ PERDEU!\n')
elif(op_j == 'tesoura' and op_c == lista[1]):
    print('VOCÊ GANHOU!\n')
else:
    print('\nNão houve vencedor!')
    print('\nOPÇÃO INVÁLIDA!! TENTE NOVAMENTE.')
