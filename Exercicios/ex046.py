'''Ex46: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos
de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.'''
print(f'{'DESAFIO 46':=^45}')
from time import sleep
for c in range(10, 0, -1):
    sleep(1)
    print(c)
print('BUUUUUUM!!!')