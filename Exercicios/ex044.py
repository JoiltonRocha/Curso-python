'''Ex44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- À vista dinheiro / cheque: 10% de desconto.
- À vista no cartão: 5% de desconto.
- Em até 2x no cartão: preço normal.
- 3x ou mais no cartão: 20% de juros.'''
print('====== DESAFIO 44 ======')
vlr = float(input('Valor do produto:'))
fpgto = int(input('Forma de pagamento:\nÀ vista dinheiro ou cheque digite [1]\nCartão em 1x digite [2]\nCartão em 2x digite [3]\nCartão em 3x ou mais digite [4]\n->'))
if fpgto == 1:
    desc = vlr * 0.10
    vlrd = vlr - desc
    print(f'Pagando dessa forma o produto de {vlr:.2f} fica por {vlrd:.2f}. 10% de desconto.')
elif fpgto == 2:
    desc = vlr * 0.05
    vlrd = vlr - desc
    print(f'Pagando dessa forma o produto de {vlr:.2f} fica por {vlrd:.2f}. 5% de desconto.')
elif fpgto == 3:
    vlrd = vlr
    print(f'Pagando dessa forma você parcela o valor de {vlr:.2f} em até 2x sem acréscimo.')
else:
    fpgto == 4
    desc = vlr * 0.2
    vlrd = vlr + desc
    print(f'Pagando dessa forma você parcela o produto de {vlr:.2f} em até 12x de {vlrd / 12:.2f} ({vlrd:.2f}) um pequeno acréscimo de 20%.')
