from time import sleep
def maior(*num):
    print('Analisando os valores passados...')
    sleep(0.5)
    print('-='*30)
    if(len(num) == 0):
        print(f'Não foram informados valores para análise')
        print(f'Não há número maior.')
        print('-='*30)
    else:
        for i in num:
            print (i, end=' ', flush= True)
            sleep(0.3)
        print(f'.Foram informados {len(num)} valores ao todo.')
        print(f'O maior valor informado foi {max(num)}.')
        print('-='*30)

print('-='*30)
maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()
print(f'{"FIM":^60}')