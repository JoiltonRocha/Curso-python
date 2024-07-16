#Ex31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço...
#...da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
print('====== DESAFIO 31 ======')
d = int(input('Qual a distância em Km da viagem? '))
if d <= 200:
    vlr = float(d * 0.50)
else:
    vlr = float(d * 0.45)
print(f'O valor da passagem é R${vlr:.2f}')
