'''Ex63: Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n
primeiros elementos de  mma Sequência de Fibonacci.
Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8.'''
print(f'{'DESAFIO 63':=^45}')
num = int(input('Quantos termos você que mostrar? '))
t1 = 0
t2 = 1
print(f'{t1} -> {t2}', end='')
cont = 3
while cont <= num:
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
    cont = cont + 1
print(' -> FIM')
