'''Crie um program que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar,
para cada palavra, quais são vogais.'''
print(f'{'DESAFIO 77':=^45}')
tupla = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON',
         'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR',
         'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
for c in tupla:
    print(f'\nNa palavra {c} temos ', end='')
    for letra in c:
        if letra in 'AEIOU':
            print(letra.lower(), end=' ')
