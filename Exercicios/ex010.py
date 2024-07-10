#Ex010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre...
#...quantos Dólares ela pode comprar. Considere US$1,00 = R$3,27.
print('====== DESAFIO 10 ======')
real = float(input('Digite um valor: R$'))
dólar = real / 3.27
print(f'O total em dólares é US${dólar:.2f}')
