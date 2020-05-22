from datetime import date
dados = {}
dados['nome'] = str(input('Nome: ')).strip().capitalize()
ano = int(input('Ano de nascimento: '))
idade = date.today().year - ano
dados['idade'] = idade
dados['nct'] = int(input('Nº da Carteira de Trabalho [0 - não possui CTPS]: '))
if(dados['nct'] != 0):
    dados['ano'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: '))
    dados['aposentadoria'] = (dados['ano'] + 35) - ano
    dados.copy()
    print(dados)
    print('-='*50)
    print(f'- Nome: {dados["nome"]}')
    print(f'- Idade: {dados["idade"]}')
    print(f'- Número CTPS: {dados["nct"]}')
    print(f'- Contratação foi em {dados["ano"]}')
    print(f'- Salário: {dados["salario"]}')
    print(f'- Aposentadoria será com {dados["aposentadoria"]} anos')
    print()
else:
    dados.copy()
    print(dados)
    print('-='*50)
    print(f'- Nome: {dados["nome"]}')
    print(f'- Idade: {dados["idade"]}')
    print(f'- Número CTPS: {dados["nct"]}')
    print()