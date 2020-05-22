from random import sample
'''A função SAMPLE retorna uma quantidade de valores k entre um intervalo de números definidos
para sorteio'''
tupla = tuple(sample(range(10),5)) #Definindo uma tupla com 5 valores aleatórios entre 0 e 9
print('='*50)
print(f'O valores sorteados foram: {tupla}')
print(f'O MAIOR valor sorteado foi {max(tupla)}')
print(f'O MENOR valor sorteado foi {min(tupla)}')
print('='*50)
