from ex115 import interface

def arquivoexiste(nome):
    try:
        file = open(nome, 'rt') #O paramentro rt significa que estou abrindo para leitura de arquivo em modo texto
        file.close()
    except FileNotFoundError: #Se o arquivo não for encontrado
        return False
    else:
        return True

def criararquivo(nome):
    try:
        file = open(nome, 'wt+') #O parametro wt+ significa "ESCREVA UM ARQUIVO DE TEXTO E (+) CASO ELE NÃO EXISTA, CRIE-0"
        file.close()
    except: 
        print('Houve um erro na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerarquivo(nome):
    try:
        file = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        interface.cabecalho('PESSOAS CADASTRADAS')
        for linha in file:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        file.close()
        
def cadastrar(nome, n = 'desconhecido', idade = 0):
    try:
        file = open(nome,'at')               #ABRINDO ARQUIVO PARA ADICIONAR ELEMENTOS AO FINAL
    except:
        print('Houve um erro na abertura do arquivo')
    else:
        try:
            file.write(f'{n};{idade}\n')
        except:
            print('Houve um erro na hora de escrever os dados')
        else:
            print(f'Novo registro de {n} adicionado')
            file.close()


