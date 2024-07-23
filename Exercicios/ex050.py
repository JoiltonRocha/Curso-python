'''Ex50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles
que forem pares. Se o valor digitado for ímpar, desconsidere-o.'''
print(f'{'DESAFIO 50':=^45}')
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c}º número:'))
    if num % 2 == 0:
        soma = soma + num # Pode ser escrito assim: soma += num
        cont = cont + 1 # Pode ser escrito assim: cont += 1
print(f'Foram digitados {c} números pares e a soma deles é {soma}.')

