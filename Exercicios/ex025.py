#Ex025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA"  no nome.
print('====== DESAFIO 025 ======')
nome = str(input('Digite seu nome completo: '))
print(f'Seu nome tem Silva? {'SILVA' in nome.upper()}')
