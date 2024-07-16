#Ex30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
print('====== DESAFIO 30 ======')
n = int(input('Digite um número: '))
if n % 2 == 0:
    print(f'{n} é um número par.')
else:
    print(f' {n} é um número ímpar.')
