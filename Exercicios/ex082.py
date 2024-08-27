'''Crie um programa que vai ler vários valores e colocar em uma lista.
Depois disso, crie duas listas extras que vão contar apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mosotre os conteúdo das três listas geradas.'''
print(f'{'DESAFIO 82':=^45}')
cont = 0
valores = pares = impares = list()
while True:
    valores.append(int(input('Digite um número: ')))
    cont = cont + 1
    continuar = str(input('Deseja informar outro número? [S/N] -> ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Deseja informar outro número? [S/N] -> ')).upper().strip()[0]
    if continuar in 'N':
        break
for c in range(0, len(valores)):
    if valores[c] % 2 == 0:
        pares = pares.append(valores[c])
    else:
        impares = impares.append(valores[c])
print(f'LISTA: {valores}')
print(f'PARES: {pares}')
print(f'ÍMPARES: {impares}')