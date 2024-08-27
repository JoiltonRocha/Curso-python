'''Crie um programa onde o usuário possa dogitar vários valores numéricos e cadasre-os em uma lista. Caso o número
exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados em ordem crescente.'''
print(f'{'DESAFIO 79':=^45}')
num = list()
while True:
    num.append(int(input('Digite um número: ')))
    if num 
    continuar = str(input('Deseja informar outro número? [S/N] -> ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Deseja informar outro número? [S/N] -> ')).upper().strip()[0]
    if continuar in 'N':
        break
