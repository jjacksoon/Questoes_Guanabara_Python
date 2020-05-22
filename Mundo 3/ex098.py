from time import sleep
def contador(i,f,p):
    print(f'Contagem de {i} até {f} passo {p}: ',end='')
    if(p < 0):
        p = p*(-1)
    if p == 0:
        p = 1
    if(i < f):
        for v in range(i,f+1,p):
            print(f'{v}', end=' ', flush= True)
            sleep(0.5)
        print('FIM')
    else:
        for v in range(i,f-1,-p):
            print(f'{v}', end=' ', flush= True)
            sleep(0.5)
        print('FIM')

def linha():
    print('-='*30)


linha()
contador(1,10,1)
linha()
contador(10,0,2)
linha()
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Valor inicial: '))
f = int(input('Valor final: '))
p = int(input('Valor passo: '))
linha()
contador(i,f,p)
linha()