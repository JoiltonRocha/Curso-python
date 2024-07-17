#Ex32: Faça um programa que leia um ano e mostre se ele é BISSESTO.
print('====== DESAFIO ======')
import calendar
ano = int(input('Digite um ano: '))
if calendar.isleap(ano):
    print(f'{ano} é um ano bissesto.')
else:
    print(f'{ano} não é um ano bissesto.')
