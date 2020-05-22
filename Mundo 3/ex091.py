import random, time, operator
resultado = {}
ordem = []
i = 1
for j in range (1,5):
    resultado[j] = random.randint(1,6)
    print (f'O jogador {j} tirou o número {resultado[j]}')
    resultado.copy()
    time.sleep(1)
'''ORDEM DOS ITENS DO DICIONÁRIO LEVANDO EM CONSIDERAÇÃO OS SEUS VALORES NA POSIÇÃO 1'''
ordem = sorted(resultado.items(), key= operator.itemgetter(1), reverse= True) 
print()
print ('===RANKING DOS JOGADORES===')
for k in ordem:
    print(f'{i}º LUGAR - Jogador {k[0]} com {k[1]}')
    time.sleep(1)
    i += 1