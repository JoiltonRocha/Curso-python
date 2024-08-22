'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.'''
print(f'{'DESAFIO 74':=^45}')
from random import randint
cont = 0
while cont < 5:
    num = randint()
    cont = cont + 1
print(num)
