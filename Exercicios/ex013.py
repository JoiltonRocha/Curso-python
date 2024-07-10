#Ex013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo...
#...salário com 15% de aumento.
#COMO EU FIZ:
print('====== DESAFIO 13 ======')
s = input('Digite o salário: R$')
a = float(s) * 0.15
ns = float(s) + a
print(f'O salário com ajuste é R${ns:.2f}')
#FORMA MELHOR
#salário = float(input('Digite o salário: R$'))
#novo = salário + (salário*15/100)
#print(f'O salário com 15% de aumento é R${novo:.2f}')
