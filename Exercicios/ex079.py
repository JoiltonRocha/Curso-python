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
        print('Número duplicado não pode ser adicionado.')
    continuar = str(input('Deseja informar outro número? [S/N] -> ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Deseja informar outro número? [S/N] -> ')).upper().strip()[0]
    if continuar in 'N':
        break
print('=' * 30)
num.sort()
print(f'Você adicionaou os valores {num}')