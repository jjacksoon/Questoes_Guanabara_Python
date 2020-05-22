dados = {}
lista = []
lm = []
lacima = []
soma = 0
while True:
    dados['nome'] = str(input('Nome da pessoa: ')).strip().capitalize()
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()
    dados['sexo'] = sexo
    dados['idade'] = int(input('Idade: '))
    lista.append(dados.copy())
    op = ' '
    while op not in 'SN':
        op = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if op == 'N':
        break
for k,v in enumerate(lista):
    soma += lista[k]['idade']
    if(lista[k]['sexo'] == 'F'):
        lm.append(lista[k]['nome'])
media = soma/len(lista)
for k,v in enumerate(lista):
    if(lista[k]['idade'] > media):
        lacima.append(lista[k])
print('=-'*30)
print(f'- Número de pessoas cadastradas: {len(lista)}')
print(f'- A média de idade do grupo é: {media:.2f} anos')
print(f'- Mulheres cadastradas: ', end= '')
for k in lm:
    print (k, end= ' ')
print()
print('- Lista de pessoas que estão acima da média: ')
for k,v in enumerate(lacima):
    print(f'    Nome = {lacima[k]["nome"]}, Sexo = {lacima[k]["sexo"]}; Idade = {lacima[k]["idade"]}')
print('=-'*40)
