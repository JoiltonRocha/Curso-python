'''Ex57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores
'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.'''
print(f'{'DESAFIO 57':=^45}')
sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor informe seu sexo [M/F]:')).upper().strip()[0]
print(f'Sexo {sexo} registrado com sucesso!')
