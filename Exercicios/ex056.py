'''Ex56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do
programa, mostre:
> A média de idade do grupo.
> Qual é o nome do homem mais velho.
> Quantas mulheres têm menos de 20 anos.'''
print(f'{'DESAFIO 56':=^45}')
for c in range(1, 5):
    str(input('Digite o nome: '))
    str(input('Digite a idade: '))
    str(input('Digite o sexo mulher [M] ou homem [H]: '))
media = idade / 4
print(f'A média de idades dessas quatro pessoas é {media}')
    if 