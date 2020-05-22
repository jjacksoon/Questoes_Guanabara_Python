def aumenta(valor = 0,aumento = 0):
    saldo = valor*(1 + (aumento/100))
    return saldo

def diminuir(valor = 0, diminuicao = 0):
    saldo = valor *(1 - (diminuicao/100))
    return saldo

def dobrar(valor = 0):
    saldo = valor*2
    return saldo

def metade(valor = 0):
    saldo = valor/2
    return saldo

def moeda(valor = 0):
    return (valor)

def resumo (valor, a, d):
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
    print(f'Dobro do preço:{dobrar(valor):>31}')
    print(f'Metade do preço:{metade(valor):>29}')
    print(f'{a}% de aumento:{aumenta(valor,a):>30}')
    print(f'{d}% de redução:{diminuir(valor,d):>30}')
    print('-'*50)
