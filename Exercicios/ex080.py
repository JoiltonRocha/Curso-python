'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição
correta de inserção (sem usar o sort()).
No final, mostre a lista ordenada na tela.'''
print(f'{'DESAFIO 80':=^45}')
num = list()
for c in range(0, 5):
    num.append(int(input('Digite um número: ')))
    