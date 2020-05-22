def ficha(n = '<desconhecido>',g = 0):
    print(f'O jogador {n} fez {g} gols.')

#PROGRAMA PRINCIPAL
nome = str(input('Nome: ')).strip().capitalize()
gols = input('Gols: ')
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome == '':
    ficha(g =gols)
else:
    ficha(nome, gols)
