def nota(*n, sit = False):
    """nota(*n, sit = False)
        => Funcao para analisar notas e situacao de varios alunos.
            - Para n: uma ou mais notas dos alunos (aceita varios)
            - Para sit: valor opcional, indicando se deve ou nao adicionar a situacao
            - return: dicinario com varias informacoes sobre a situacao da turma
    """
    notas = {}
    notas['total'] = len(n)
    notas['maior'] = max(n)
    notas['menor'] = min(n)
    notas['media'] = sum(n)/len(n)
    if(sit == True):
        if(notas['media'] >= 7):
            notas['situação'] = 'APROVADO'
        elif (5 < notas['media'] < 7):
            notas['situação'] = 'RECUPERAÇÃO'
        else:
            notas['situação'] = 'REPROVADO'
    return notas

resp = nota(5.5, 9.5, 10, 6.5, sit = True)
print(resp)
# help(nota)

