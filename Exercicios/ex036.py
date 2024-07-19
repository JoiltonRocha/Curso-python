#Ex36:Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa.
#O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exeder 30% do salário ou então o...
#...empréstimo será negado.
print('====== DESAFIO 36 ======')
casa = float(input('Qual o valor da casa? R$'))
salário = float(input('Qual o valor do salário? R$'))
prazo = int(input('Qual o prazo para pagamento em anos? '))
parcela = casa / (prazo * 12)
percentual = (parcela * 100) / salário
print('*' * 50)
if percentual > 30:
    print(f'Valor da casa: R${casa:.2f}\nPrazo para pagamento: {prazo} anos\nParcelas R${parcela:.2f}\nEssa parcela representa {percentual:.1f}% do salário. De acordo com o Banco Central, o limite é de 30%.')
else:
    print(f'Empréstimo aprovado!\nValor da casa: R${casa:.2f}\nPrazo para pagamento: {prazo} anos\nParcelas: R${parcela:.2f}.')
