from datetime import date
ano = int(input('\nEntre com o ano de nascimento do atleta: '))
atual = date.today().year
idade = atual - ano
print('O atleta tem {} anos!'.format(idade))
if (idade <= 9):
    print('Categoria: MIRIM\n')
elif(idade <= 14):
    print('Categoria: INFANTIL\n')
elif(idade <= 19):
    print('Categoria: JÚNIOR\n')
elif (idade <= 25):
    print('Categoria: SÊNIOR\n')
else: 
    print('Categoria: MASTER\n')
