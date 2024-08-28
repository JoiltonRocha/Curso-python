'''Crie um programa onde o usuário possa dogitar vários valores numéricos e cadasre-os em uma lista. Caso o número
exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados em ordem crescente.'''
print(f'{'DESAFIO 79':=^45}')
num = list()
while True:
    n = (int(input('Digite um número: ')))
    if n not in num:
        num.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print(f'O Número {n} não pode ser adicionado pois já foi adicionado na posição {num.index(n)}.')
    continuar = str(input('Deseja informar outro número? [S/N] -> ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Deseja informar outro número? [S/N] -> ')).upper().strip()[0]
    if continuar in 'N':
        break
print('=' * 30)
num.sort()
print(f'Você adicionaou os valores {num}')
