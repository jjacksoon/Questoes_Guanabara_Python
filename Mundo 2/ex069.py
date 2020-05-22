soma = homem = mulher = 0
while True:
        print('{:-^40}'.format('CADASTRO DE PESSOA'))
        idade = int(input('Idade da pessoa: '))
        s = ' '
        while(s not in 'MF'):
            s = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if(idade > 18):
            soma += 1
        if(s == 'M'):
            homem += 1
        if(s == 'F' and idade < 20):
            mulher += 1        
        op = ' '
        while(op not in 'SN'):
            op = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if(op == 'N'):
            break
print('\nPROGRAMA FINALIZADO!')
print(20*'-=')
print(f'Existem {soma} pessoas maiores de 18 anos!')
print(f'{homem} Homens foram cadastrados!')
print(f'{mulher} mulheres têm menos de 20 anos!')
print(20*'-=')
