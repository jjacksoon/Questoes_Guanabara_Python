maior = 0
menor = 9999
for c in range (0,5):
    p = float(input('\nEntre com o peso da {}º pessoa em kg: '.format(c+1)))
    if (p > maior):
        maior = p
    elif (p < menor):
        menor = p
print ('\nMaior peso é {} kg'.format(maior))
print ('\nMenor peso é {} kg'.format(menor))
print('\nFIM')
