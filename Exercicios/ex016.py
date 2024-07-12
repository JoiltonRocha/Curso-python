#Ex016: Crie um programa que leia um número real qualquer pelo teclado e mostre na tela...
#...a sua porção inteira.
#COMO EU FIZ
print('====== DESAFIO 016 ======')
num = float(input('Digite um número: '))
int = int(num)
print(f'A parte inteira do número "{num}" é "{int}".')
#USANDO MODOLOS
#import math
#num = float(input('Digite um número: '))
#print(f'A parte inteira do número "{num}" é "{math.trunc(num)}".')
#IMPORTANDO APENAS A FUNÇÃO "TRUNC".
#from math import trunc
#num = float(input('Digite um número: '))
#print(f'A parte inteira do número "{num}" é "{trunc(num)}".')
