n1 = float(input('\nEntre com o valor da nota 1: '))
n2 = float(input('Entre com o valor da nota 2: '))
media = (n1 + n2)/2
print('Tirando a nota {} e {}, a média do aluno é {:.1f}'.format(n1,n2,media))
if(media < 5.0):
    print('\nO aluno está REPROVADO!\n')
elif(7 > media >= 5.0):
    print('\nO aluno está de RECUPERAÇÃO!\n')
else:
    print('\nO aluno está APROVADO!\n')
