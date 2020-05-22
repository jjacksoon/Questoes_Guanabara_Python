sexo = 'a'
while sexo != 'M' and sexo != 'F':
    sexo = str(input('\nDigite o sexo da pessoa [M/F]: ')).upper()
    if (sexo != 'M' and sexo != 'F'):
        print('\nOPÇÃO INVÁLIDA. TENTE NOVAMENTE!')
print('\nFIM')