def linha(tam = 42):
    return '-'*tam

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


def cabecalho(msg):                      #FUNÇÃO PARA MOSTRAR O CABEÇALHO DA OPÇÃO ESCOLHIDA
    print(linha())
    print(f'{msg.center(42)}')
    print(linha())

def menu(lista):                             #FUNÇÃO PARA MOSTRAR O MENU
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    op = leiaint('Sua opção: ')
    return op