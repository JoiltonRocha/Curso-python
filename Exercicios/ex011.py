#Ex011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule...
#... a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta...
#...pinta uma área de 2m².
print('====== DESAFIO 11 ======')
larg = float(input('Digite a largura: '))
alt = float(input('Digite a altura: '))
área = larg * alt
tinta = área / 2
print(f'O total da área é {área}m² e é preciso {tinta:.3f}L de tinta para pintá-la.')
