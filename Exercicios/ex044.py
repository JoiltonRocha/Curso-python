'''Ex44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- À vista dinheiro / cheque: 10% de desconto.
- À vista no cartão: 5% de desconto.
- Em até 2x no cartão: preço normal.
- 3x ou mais no cartão: 20% de juros.'''
print(f'{'DESAFIO 44':=^30}')
vlr = float(input('Valor da compra: R$'))
print(f'''FORMAS DE PAGAMENTO:
[1] À vista dinheiro ou cheque
[2] Cartão em 1x
[3] Cartão em 2x
[4] Cartão em 3x ou mais''')
fpgto = int(input('Digite a opção desejada: '))
if fpgto == 1:
    total = vlr - (vlr * 10 / 100)
    print(f'Pagando dessa forma, a compra de R${vlr:.2f} fica por R${total:.2f}. 10% de desconto.')
elif fpgto == 2:
    total = vlr - (vlr * 5 / 100)
    print(f'Pagando dessa forma, a compra de R${vlr:.2f} fica por R${total:.2f}. 5% de desconto.')
elif fpgto == 3:
    total = vlr
    print(f'Pagando dessa forma, você parcela a compra com valor de R${vlr:.2f} em até 2x sem acréscimo.')
elif fpgto == 4:
    total = vlr + (vlr * 20 / 100)
    parcelas = int(input('Digite a quantidade de parcelas: '))
    vlrparcelas = total / parcelas
    print(f'Sua compra será parcelada em {parcelas}x de R${vlrparcelas:.2f} (COM JUROS).')
    print(f'Sua compra de R${vlr:.2f} vai custar R${total:.2f} no final.')
else:
    print('OPÇÃO INCORRETA! Escolha uma opção válida.')
