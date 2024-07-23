'''Ex54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre
quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''
print(f'{'DESAFIO 54':=^45}')
from datetime import date
anoatual = date.today().year
totmaior = 0
totmenor = 0
for c in range(1, 8):
    anonasc = int(input(f'Digite o ano de nascimento da {c}ª pessoa: '))
    idade = anoatual - anonasc
    if idade >= 21:
        totmaior = totmaior + 1 #Pode ser escrito: totmaior += 1
    else:
        totmenor = totmenor + 1 #Pode ser escrito: totmenor += 1
print(f'Total de pessoas maiores de idade: {totmaior}.\nTotal de pessoas menores de idade: {totmenor}.')
