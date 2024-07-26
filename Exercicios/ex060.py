'''Ex60: Faça um programa que leia um número quelquer e mostre seu fatorial.
Ex: 5! = 5x4x3x2x1=120'''
print(f'{'DESAFIO 60':=^45}')
num = int(input('Digite um número: '))
cont = 1
result = 1
while cont <= num:
    result = result * cont
    cont = cont + 1
print(result)