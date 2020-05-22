dados = {}
gols = []
soma = 0
dados['nome'] = str(input('nome: ')).strip().capitalize()
partidas = int(input('número de partidas jogadas: '))
for i in range (0,partidas):
    valor = int(input(f'Gols da partida {i+1}: '))
    soma += valor
    gols.append(valor)
dados['gols'] = gols
dados['total'] = soma
print('-='*30)
print(dados)
print('-='*30)
for k,v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {dados["nome"]} jogou {partidas} partidas:')
print()
for p,v in enumerate(gols):
    print(f'    => Na partida {p+1}, fez {v} gols')
print(f'\nFoi um total de {soma} gols')