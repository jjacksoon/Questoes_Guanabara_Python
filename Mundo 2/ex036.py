valor = float(input('Qual o valor da casa?: R$'))
salario = float(input('Entre com o valor do seu salário: R$'))
anos = int(input('Quantos anos vai passar pagando?: '))
prestacao = valor/(anos*12)
print ('\nO valor da prestação será R${:.2f}!'.format(prestacao))
if(prestacao <= 0.3*salario):
    print('\nParabéns. Emprestimo concedido!')
else:
    print('\nInfelizmente seu emprestimo não foi autorizado.')
print('FIM')
