num = int(input('\nDigite o número: '))
print(15*'=','MENU',15*'=')
print('''1 - conversão em binário 
2 - conversão em octal 
3 - conversão em hexadecimal''')
print(36*'=')
conv = int(input('\nDigite a oção de conversão desejada: '))
if(conv == 1):
    print('\nNúmero {} convertido para binário: {}'.format(num, bin(num)[2:]))
elif (conv == 2):
    print('\nNúmero {} convertido para octal: {}'.format(num, oct(num)[2:]))
elif(conv == 3):
    print('\nNúmero {} convertido para hexadecimal: {}'.format(num, hex(num)[2:]))
else:
    print('\nOPÇÃO INVÁLIDA!')
print('\nFIM')