#Ex012: Faça um programa que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
#COMO EU FIZ:
print('====== DESAFIO 12 ======')
p = float(input('O preço normal do produto é R$'))
d = p * 0.05
n = p - d
print(f'O preço do produto na promoção é R${n:.2f}')
#FORMA MELHOR
#preço = float(input('O preço normal do produto é R$'))
#novo = preço - (preço*5/100)
#print(f'O produto que custava {preço:.2f}, com desconto de 5% da promoção fica por R${novo:.2f}')
