'''Ex48: Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos
de três e que se encontram no intervalo entre 1 e 500.'''
print(f'{'DESAFIO 48':=^45}')
s = 0
for c in range(3, 500, 3):
    if c % 2 != 0:
        s += c
        print(c)

