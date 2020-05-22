palavra = ('Aprender', 'programar', 'linguagem',
        'python', 'curso', 'gratis', 'estudar',
        'praticar', 'trabalhar', 'mercado', 'programador',
        'futuro')

for p in palavra:
    print(f'\nA palavra {p.upper()} tem ', end='')
    for letra in p:
        if letra.upper() in 'AEIOU':
            print(letra, end=' ')
    
            