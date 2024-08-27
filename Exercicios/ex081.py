'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
a) Quantos números foram digitados.
b) A lista de valores, ordenando de forma decrescente.
c) Se o valor 5 foi digitado e está ou não na lista.'''
print(f'{'DESAFIO 81':=^45}')
cont = 0
num = list()
while True:
    num.append(int(input('Digite um número: ')))
    cont = cont + 1
    continuar = str(input('Deseja informar outro número? [S/N] -> ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Deseja informar outro número? [S/N] -> ')).upper().strip()[0]
    if continuar in 'N':
        break
print(f'{'FIM!':=^45}')
print(f'-> Foram digitados {cont} números.')
num.sort(reverse=True)
print(f'-> A lista em ordem decrescente é {num}')
if 5 in num:
    print('-> O "5" está na lista.')
else:
    print('-> O "5" não foi encontrado na lista.')
