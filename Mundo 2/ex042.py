# FORMAÇÃO DE TRIÂNGULOS
'''Para construir um triângulo é necessário que a medida de qualquer um dos lados seja menor que a soma das medidas dos
outros dois e maior que o valor absoluto da diferença entre essas medidas'''
from math import fabs

a = float(input('\nEntre com o valor do lado: '))
b = float(input('Entre com o valor do lado: '))
c = float(input('Entre com o valor do lado: '))

if (a < b + c) and (a > fabs(b - c)) or ((b < a + c) and (b > fabs(a - c))) or ((c < a + b) and (c > fabs(a - b))):
    print('\nExiste a formação de um triângulo')
    if(a == b == c):
        print('\nTRIÂNGULO EQUILÁTERO!\n')
    elif(a != b != c != a):
        print('\nTRIÂNGULO ESCALENO!\n')
    else:
        print('\nTRIÂNGULO ISOSCELES!\n')
else:
    print('\nEsses valores não obedecem a condição de formação de um triângulo!')
print(10*'=','FIM',10*'=')
