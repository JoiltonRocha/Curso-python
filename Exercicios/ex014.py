#Ex014: Escreva um programa que converta uma temperatura de ºC para ºF.
C = float(input('Informe a temperatura em ºC: '))
F = (C * 1.8) + 32
#OUTRA FÓRMULA:
#F = ((9 * C) / 5) + 32
#Nesse caso, os parenteses são irrelevantes pois o calculo está na ordem correta de precêdencia.
print(f'A temperatura de {C}ºC corresponde a {F}ºF')
