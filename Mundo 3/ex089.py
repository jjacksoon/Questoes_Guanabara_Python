import time
boletim  = []
n = []
dados = []                                      #Lista auxiliar para jogar dados ao boletim
while True:
    dados.append(str(input('Nome do aluno: ')).strip().capitalize())
    for i in range(0,2):
        n.append(float(input(f'Nota {i+1}: ')))
    dados.append(n[:])
    media = (n[0] + n[1])/2
    n.clear()
    dados.append(media)
    boletim.append(dados[:])
    dados.clear()
    op = ' '
    while op not in 'SN':
        op = str(input('Deseja continuar?[S/N]: ')).strip().upper()
    if op == 'N':
        break
print('-='*30)
print(f'{"BOLETIM GERAL":^60}')
print('-='*30)
print('CÓDIGO       NOME            MÉDIA')
print('-'*60)
for k,v in enumerate(boletim):
    print(f'{k+1:^5}', end=' ')
    print(f'{boletim[k][0]:^20}', end=' ')
    print(f'{boletim[k][2]:>7.1f}', end=' ')
    print()
print('-'*60)
cd = ' '
while cd != 999:
    cd = int(input('Código do aluno que deseja saber a nota [999 - parar]: '))
    for k,v in enumerate(boletim):
        if(cd == k+1):
            print()
            print(f'    - Nota 1 do(a) aluno(a) {boletim[k][0]}: {boletim[k][1][0]} ')
            print(f'    - Nota 2 do(a) aluno(a) {boletim[k][0]}: {boletim[k][1][1]} ')
            print('-'*60)
    if(cd > len(boletim) and cd != 999):
            print('Aluno não encontrado. Tente novamente!')
    if cd == 999:
        print('Finalizando...\n')
        time.sleep(1)
        print('<< BUSCA ENCERRADA >>')
        break