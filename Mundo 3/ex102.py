def fatorial (num, show = False):
    """Fatorial(n, show = False)
        => Calcula o fatorial de um número.
            - Para n: Número a ser calculado;
            - Para show: Mostrar ou não a conta (Opcional)
            - return: O valor do fatorial de um número n
    """
    
    f = 1
    for c in range (num, 0, -1):
        if show:
            if(c > 1):
                print(f'{c} x ', end='')
            else:
                print(f'{c} = ', end='')
        f *= c
    return f
    

print('-'*20)
#help(fatorial)
print(fatorial(5, show = True))
