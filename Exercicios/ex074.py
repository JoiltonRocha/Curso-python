'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.'''
print(f'{'DESAFIO 74':=^45}')
from random import randint
cont = maior = menor = 0
print('Os valores sorteados foram: ', end='')
while cont < 5:
    num = randint(0, 10)
    cont = cont + 1
    tupla = (num)
    print(f'{tupla} ', end='')
    if cont == 1:
        menor = num
        maior = num
    else:
        if num < menor:
            menor = num
        if num > maior:
            maior = num
print(f'\nO maior número sorteado foi {maior}')
print(f'O menor número sorteado foi {menor}')
