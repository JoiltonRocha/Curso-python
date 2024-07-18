#Ex37: Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher...
#...qual será a base de conversão:
#-1 Para binário
#-2 Para octal
#-3 Para hexadecimal
print('====== DESAFIO 37 ======')
n = int(input('Digite o número que deseja converter: '))
base = int(input('Digite [1] para transformar em binário\nDigite [2] para transformar em octal\nDigite [3] para transformar em hexadecimal\n->'))
if base == 1:
    conversão = bin(n)[2:]
elif base == 2:
    conversão = oct(n)[2:]
elif base == 3:
    conversão = hex(n)[2:]
else:
    print('Opção inválida')
print(f'O número {n} convertido para a base {base} é {conversão}')
