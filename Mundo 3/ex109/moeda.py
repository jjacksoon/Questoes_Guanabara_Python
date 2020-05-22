def aumenta(valor = 0, aumento = 0, sit = False):
    saldo = valor*(1 + (aumento/100))
    if sit == True:
        return moeda(saldo)
    else:
        return saldo

def diminuir(valor = 0, diminuicao = 0, sit = False):
    saldo = valor *(1 - (diminuicao/100))
    if sit == True:
        return moeda(saldo)
    else:
        return saldo

def dobrar(valor = 0, sit = False):
    saldo = valor*2
    if sit == True:
        return moeda(saldo)
    else:
        return saldo

def metade(valor = 0, sit = False):
    saldo = valor/2
    if sit == True:
        return moeda(saldo)
    else:
        return saldo

def moeda(valor = 0, moeda = 'R$'):
    return (f'{moeda} {valor:.2f}'.replace('.',','))

def resumo (valor, a, d, sit):
    """resumo (valor, a, d)
        => Realiza o resumo da analise com todos os dados pedidos.
            -Para valor: Valor a ser analisado
            -Para a: Valor percentual do aumento
            -Para d: Valor percentual da diminuicao
    """
    print('-'*50)
    print(F'{"RESUMO DO VALOR":^50}')
    print('-'*50)
    print(f'Preço analisado:{moeda(valor):>29}')
    print(f'Dobro do preço:{dobrar(valor,True):>31}')
    print(f'Metade do preço:{metade(valor,True):>29}')
    print(f'{a}% de aumento:{aumenta(valor,a,True):>30}')
    print(f'{d}% de redução:{diminuir(valor,d,True):>30}')
    print('-'*50)
    