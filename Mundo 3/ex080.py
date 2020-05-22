v = [] 
for c in range (5):
    n = int(input('Digite um valor: '))
    if(c == 0 or n > v[-1]):
        v.append(n)    
        print('adicionado ao final da lista') 
    else:
        for pos,valor in enumerate(v):
            if(n < valor):
                v.insert(pos,n)
                print(f'adicionado na posição {pos} da lista')
                break
print()
print(f'Os valores digitados em ordem foram: {v}')
