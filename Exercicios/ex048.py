'''Ex48: Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos
de três e que se encontram no intervalo entre 1 e 500.'''
print(f'{'DESAFIO 48':=^45}')
soma = 0 #ACUMULADOR: Geralmente conta mais 1.
cont = 0 #CONTADOR: Geralmente acumula os valores,
for c in range(3, 501, 3):
    if c % 2 != 0:
        soma = soma + c #Pode ser escrito: soma += c
        cont = cont + 1 #Pode ser escrito: cont += 1
print(f'A soma de todos os {cont} números ímpares e múltiplos de três no intervalo entre 1 e 500 é {soma}')
