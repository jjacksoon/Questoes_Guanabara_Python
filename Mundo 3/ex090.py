aluno = {}
boletim = []
while True:
    aluno['nome'] = str(input('Nome do aluno: ')).strip().capitalize()
    aluno['media'] = float(input(f'Média do {"nome"}: '))
    if aluno['media'] >= 7:
        aluno['situacao'] = 'APROVADO'
    elif 5 < aluno['media'] < 7:
        aluno['situacao'] = 'RECUPERAÇÃO'
    else:
        aluno['situacao'] = 'REPROVADO'
    boletim.append(aluno.copy())
    op = ' '
    while op not in 'SN':
        op = str(input('Deseja continuar?[S/N]: ')).upper()
    if op == 'N':
        break
print('-='*20)
for i in boletim:
    print(f'O nome é: {i["nome"]}')
    print(f'A média é {i["media"]}')
    print(f'A situação é {i["situacao"]}')
    print('-='*20)