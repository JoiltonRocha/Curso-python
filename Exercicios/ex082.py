'''Crie um programa que vai ler vários valores e colocar em uma lista.
Depois disso, crie duas listas extras que vão contar apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mosotre os conteúdo das três listas geradas.'''
print(f'{'DESAFIO 82':=^45}')
valores = list()
pares = list()
impares = list()
while True:
    n = int(input('Digite um número: '))
    valores.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    continuar = str(input('Deseja informar outro número? [S/N] -> ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Deseja informar outro número? [S/N] -> ')).upper().strip()[0]
    if continuar in 'N':
        break
print(f'{'FIM!':=^45}')
print(f'LISTA: {valores}')
print(f'PARES da LISTA: {pares}')
print(f'ÍMPARES da LISTA: {impares}')

#COMO O PROFESSOR FEZ:
'''valores = list()
pares = list()
impares = list()
while True:
    valores.append(int(input('Digite um valor: ')))
    continuar = str(input('Deseja informar outro número? [S/N] -> ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Deseja informar outro número? [S/N] -> ')).upper().strip()[0]
    if continuar in 'N':
        break
for indice, valor in enumerate(valores):
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
print(f'{'FIM!':=^45}')
print(f'LISTA: {valores}')
print(f'PARES da LISTA: {pares}')
print(f'ÍMPARES da LISTA: {impares}')'''
