def leiaint(num):
    numero = input(num)         #O QUE FOI RECEBIDO DO PROGRAMA PRINCIPAL FOI UMA STRING
    if(numero.isnumeric()):
        return numero
    else:
        print ('Erro. Digite um número inteiro válido!')
        return leiaint(num)

n = leiaint('Digite um valor: ')
print(f'Você digitou o número {n}')