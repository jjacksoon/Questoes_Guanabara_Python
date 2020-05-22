tabela = ('Flamengo','Santos','Palmeiras','Grêmio','Atlético-PR',
        'São Paulo','Internacional','Corinthians','Fortaleza','Goiás',
        'Bahia','Vasco','Atlético-MG','Fluminense','Botafogo','Ceará',
        'Cruzeiro','CSA','Chapecoense','Avaí')

print(f'\nLISTA DE TIMES DO BRASILEIRÃO: {tabela}')
print('='*30)
print(f'\nOs CINCO primeiros colocados são: {tabela[:5]}')
print('='*30)
print(f'Os QUATRO ÚLTIMOS colocados são: {tabela[-4:]}')
print('='*130)
print(f'Os elementos em ORDEM ALFABÉTICA são: {sorted(tabela)}')
print('='*130)
posição = tabela.index('Chapecoense')
print(f'CHAPECOENSE ENCONTRA-SE NA {tabela.index("Chapecoense")+1}º posição')