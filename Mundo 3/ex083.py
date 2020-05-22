exp = str(input('Digite a expressão: ')).strip()
lista = []
for s in exp:
    if s == '(':
        lista.append('(')
    elif s == ')':
        if(len(lista) > 0):
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('sua expressão está válida!')
else:
    print('sua expressão está errada!')