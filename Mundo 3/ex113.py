def leiaint(msg):
    try:
        inteiro = int(input(msg))     
        return inteiro
    except (ValueError, TypeError):
        print('Erro. Por favor, digite um número inteiro valido.')
        return leiaint(msg)
    except KeyboardInterrupt:
        print('O usuário preferiu não digitar esse valor')
        return 0

def leiafloat(msg):
    try:
        real = float(input(msg))      
        return real
    except (ValueError, TypeError):
        print('Erro. Por favor, digite um número real valido.')
        return leiafloat(msg)
    except KeyboardInterrupt:
        print('O usuário preferiu não digitar esse valor')
        return 0

i = leiaint('Digite um valor inteiro: ')
r = leiafloat('Digite um valor real: ')
print(f'O número inteiro digritado foi {i} e o número real foi {r}')

