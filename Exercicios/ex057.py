'''Ex57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto.'''
print(f'{'DESAFIO 57':=^45}')
sexo = 1
while sexo != 0:
    sexo = str(input('Digite o sexo [M/F]:')).upper()
    if sexo = M or F:
        print('Aceito!')
    else:
        print('Opção inválida. Escolha uma das opções.')
print('FIM')