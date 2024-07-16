#Ex027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida...
#...o primeiro e o último nome separadamente.
#Ex: Ana Maria de Souza
#Ex: primeiro: Ana
#Ex: Último: Souza
print('====== DESAFIO 027 ======')
nome = str(input('Digite seu nome completo: ')).strip()
n = nome.split()
print(f'Seu primeiro nome é: {(n[0])}')
print(f'Seu último nome é: {n[len(n) - 1]}')
