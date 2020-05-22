def voto (ano_nascimento):
    from datetime import date
    i = date.today().year - ano
    if(i < 16):
        return f'Com idade {i} VOTO NEGADO'
    elif(16 <= i < 18 or i >= 65):
        return f'Com idade {i}: VOTO OPCIONAL'
    else: 
        return f'Com idade {i}: VOTO OBRIGATÓRIO'


ano = int(input('ano nascimento: '))
print('-='*30)
print(voto(ano))