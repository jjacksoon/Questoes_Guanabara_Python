altura = float(input('\nAltura em metros(m): '))
peso = float(input('Peso: '))
imc = peso/(altura**2)
print('O IMC dessa pessoa é: {:.1f}\n'.format(imc))
if (imc < 18.5):
    print('Abaixo do peso!\n')
elif (25 > imc >= 18.5):
    print('Peso ideal!\n')
elif (30 > imc >= 25):
    print('Sobrepeso!\n')
elif (40 >= imc >= 30):
    print('Obesidade!\n')
else:
    print('Obsesidade mórbida!\n')
