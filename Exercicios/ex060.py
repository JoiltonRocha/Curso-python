'''Ex60: Faça um programa que leia um número qualquer e mostre seu fatorial.
Ex: 5! = 5x4x3x2x1=120'''
print(f'{'DESAFIO 60':=^45}')
#Opção 01:
num = int(input('Digite um número para calcular seu Fatorial: '))
cont = 1
result = 1
while cont <= num:
    result = result * cont
    cont = cont + 1
print(f' O Fatorial de {num} é {result}.')

#Opção 02 (usando módulo):
'''from math import factorial
n = int(input('Digite um número para calcular seu Fatorial: '))
f = factorial(n)
print(f'O Fatorial de {n} é {f}'''


#Opção 03:
'''n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
    c = c - 1
print(f'{f}')'''
