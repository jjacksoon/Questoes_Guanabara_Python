dados = {}
gols = []
aux = []
tabela = []
soma = 0
while True:
    dados['nome'] = str(input('nome: ')).strip().capitalize()
    partidas = int(input('número de partidas jogadas: '))
    for i in range (0,partidas):
        valor = int(input(f'Gols da partida {i+1}: '))
        gols.append(valor)
        soma += valor
    dados['gols'] = gols.copy()
    dados['total'] = soma
    tabela.append(dados.copy())
    gols.clear()
    soma = 0
    op = ' '
    while op not in 'SN':
        op = str(input('Deseja continuar?[S/N]: ')).strip().upper()
    if op == 'N':
        break
    print('-='*30)
print('-='*30)
print('Código    Nome        Total        Gols')
print('-'*60)
for k,v in enumerate(tabela):
    print(f'{k+1 :^5}', end= ' ')
    print(f'{tabela[k]["nome"]:^12}', end=' ')
    print(f'{tabela[k]["total"]:^10}', end=' ')
    print(f'  {tabela[k]["gols"]}', end= ' ')
    print()
print('-'*60)
while True:
    j = ' '
    while j != 999:
        j = int(input('Mostrar dados de qual jogador?[999 - parar]: '))
        print('-'*50)
        for k,v in enumerate(tabela):
            if(j == k+1):
                print(f'--LEVANTAMENTO DO JOGADOR {tabela[k]["nome"]}--')
                for i in range(0, len(tabela[k]["gols"])):
                    print(f'    No jogo {i+1} fez {tabela[k]["gols"][i]} gols.')
        if(j > len(tabela) and j != 999):
            print(f'ERRO! Não existe jogado com o código {j}. Tente novamente.')
    if(j == 999):
        print('<< VOLTE SEMPRE >>')
        break
