'''Ex50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles
que forem pares. Se o valor degitado for ímpar, desconsidere-o.'''
print(f'{'DESAFIO 50':=^45}')
s = 0
for c in range(0, 6):
    n = int(input('Digite um número:'))
    if n % 2 == 0:
        s += n
print(f'A soma dos números pares digitados é {s}')

