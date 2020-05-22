from datetime import date
ano = int(input('\nEntre com o ano de nascimento da pessoa: '))
atual = date.today().year
idade = atual - ano
if(idade < 18):
    a = 18 - idade
    aa = atual + a
    print('\nNão é ano de alistamento!. Falta(m) {} ano(s)!\n'.format(a))
    print('O ano do alistamento será {}'.format(aa))
elif (idade == 18):
    print('\nÉ ano de alistamento!\n')
else:
    a = idade - 18
    aa = atual - a
    print('\nPassaram-se {} anos da data prevista!. Seu ano de alistamento foi {}\n'.format(a,aa))
