#Ex017: Faça um programa que leia o comprimento do cateto oposto e o cateto adjacente de um...
#...triâgulo retângulo, calcule e mostre o comprimento de hipotenusa.
print('====== DESAFIO 017 ======')
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
#O quadrado da hipotenusa é igual a soma dos quadrados dos catetos.
hi = (co ** 2 + ca ** 2) ** (1/2)
print(f'A hipotenusa vai medir {hi:.2f}')
#USANDO MODOLOS
#from math import hypot
#co = float(input('Comprimento do cateto oposto: '))
#ca = float(input('Comprimento do cateto adjacente: '))
#hi = hypot(co, ca)
#print(f'A hipotenusa vai medir {hi:.2f}')
