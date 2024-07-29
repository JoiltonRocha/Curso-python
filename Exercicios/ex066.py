'''Ex66: Crie um programa que leira vários números inteiros pelo teclado. O programa só vai
parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos
números foram digitados e qual foi a soma entre eles (desconcidere o flag).'''
print(f'{'DESAFIO 66':=^45}')
cont = soma = 0
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    cont = cont + 1
    soma = soma + num
print(f'FIM. Foram digitados {cont} números e a soma enre eles é {soma}.')
