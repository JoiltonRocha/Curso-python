'''Ex64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai
parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números
foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''
print(f'{'DESAFIO 64':=^45}')
num = 0
cont = 0
soma = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    cont = cont + 1
    soma = soma + num
    num = int(input('Digite um número [999 para parar]: '))
print(f'FIM. Foram digitados {cont} números e a soma deles é {soma}.')