#Ex008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
#km, hm, dam, m dm, cm, mm.
print('====== DESAFIO 08 ======')
mt = float(input('Digite uma distância em metros: '))
print(f'A medida de {mt}m corresponde a:\n{mt/1000}km\n{mt/100}hm\n{mt/10}dam\n{mt*10:.0f}dm\n{mt*100:.0f}cm\n{mt*1000:.0f}mm')
