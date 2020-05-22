soma = qtd = total = p = maior = 0
menor = 9999
barato = caro = ' '
print('{:=^40}'.format('MERCADINHO'))
while True:
    produto = str(input('\nNome do produto: ')).strip().upper()
    preco = float(input('Preço: R$'))
    op = ' '
    while op not in 'SN':
        op = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    soma += preco
    if(preco > 1000):
        qtd += 1
    if(preco > maior):
        maior = preco
        caro = produto
    if(preco < menor):
        menor = preco
        barato = produto
    if(op =='N'):
        break
print(40*'-=')
print(f'O total em compras foi: R${soma}')
print(f'Houveram {qtd} produtos comprados com valor superior a R$1000.00')
print(f'O produto mais barato foi {barato} que custou R$ {menor}')
print(40*'-=')
        