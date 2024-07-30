'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar
se o usuário vai continuar. No final, mostre:
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$1.000,00.
C) Qual é o nome do produto mais barato.'''
print(f'{'DESAFIO 70':=^45}')
total = mil = preçob = 0
barato = ''
while True:
    print(F'{'PRODUTO E PREÇO':*^40}')
    produto = str(input('Digite o nome do produto: '))
    preço = float(input('Digite o preço do produto: '))
    total = total + preço
    if preço > 1000:
        mil = mil + 1
    if preço <preçob:
        preçob = preço
        barato = produto
    print('-' * 40)
    continuar = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if continuar not in 'SN':
        while continuar not in 'SN':
            continuar = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    print('=' * 40)
    if continuar in 'N':
        break
print(f'TOTAL: R${total:.2f}')
if mil < 1:
    print('Nenhum produto custou mais de R$1.000,00.')
else:
    print(f'Produto com preço superior a R$1.000,00: {mil}')
print(f'O produto mais barato foi {barato} que custou R${preçob:.2f}')
