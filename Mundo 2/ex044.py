print('{:=^40}'.format('LOJAS JSN'))                            #Centralizado com 40 espaços
preco = float(input('\nValor do produto: '))
print('{:=^40}'.format('FORMAS DE PAGAMENTO'))
print('''1 - À vista (dinheiro ou cartão)
2 - À vista no cartão
3 - Em até 2x no cartão
4 - 3x ou mais no cartão''')
op = int(input('\nDIGITE A OPÇÃO DE PAGAMENTO: '))
if (op == 1):
    valor = 0.9 * preco
    print('Você vai pagar R${} pela compra de R${}\n'.format(valor,preco))
elif (op == 2):
    valor = 0.95 * preco
    print('Você vai pagar R${} pela compra de R${}\n'.format(valor,preco))
elif (op == 3):
    print('Você vai pagar R${} em 2x no cartão!\n'.format(preco))
elif (op == 4):
    n = int(input('Quantas parcelas?: '))
    valor = 1.2 * preco
    parcela = valor/n
    print('Com {} parcelas, você vai pagar R${} por parcela e o valor total será de R${}\n'.format(n, parcela, valor))
else:
    print('\nOPÇÃO INVÁLIDA. TENTE NOVAMENTE!!')
