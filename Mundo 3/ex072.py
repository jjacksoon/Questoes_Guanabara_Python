numero = ('zero', 'um', 'dois', 'três', 'quatro',
            'cinco', 'seis', 'sete', 'oito',
            'nove','dez', 'onze', 'doze', 'treze',
            'catorze', 'quinze', 'desesseis', 'desessete',
            'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if(0 <= n <= 20):
        break
    print('Número inválido. Tente novamente.', end=' ')
print(f'\nVocê digitou o número {numero[n]}')       
