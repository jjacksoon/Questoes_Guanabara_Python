soma = 0
maior = 0
nome_velho = '' #Variável auxiliar para usar na identificação e impressão do homem mais velho
aux1 = 0
aux2 = 1
c_mulher = 0
for c in range (1,5):
    print('\n-----PESSOA {}-----'.format(c))
    nome = str(input('Entre com o nome da pessoa {}: '.format(c))).upper().strip()
    idade = int(input('Entre com a idade da pessoa {}: '.format(c)))
    sexo = str(input('Entre com o sexo da pessoa {} (M - Masculino e F - Feminino): '.format(c))).upper().strip()
    soma += idade
    if(sexo == 'F' and idade < 20):
        aux1 += 1
    if(sexo == 'F'):
        c_mulher += 1
    if(sexo == 'M' and idade > maior):
        maior = idade
        nome_velho = nome
    elif(sexo =='M' and idade == maior):
        aux2 += 1
print('\nA média de idade do grupo é: {:.2f} anos'.format(soma/4))
if(sexo == 'M' and (aux2 <=4 and aux2 >= 2) or (c_mulher == 3)):
    print('\nNão existe homem mais velho!')
else:
    print('\nO homem mais velho do grupo é {} e ele tem {} anos'.format(nome_velho,maior))
print('\nExistem {} mulheres com menos de 20 anos!'.format(aux1))
print('\nFIM')
