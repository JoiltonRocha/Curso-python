#Ex36:Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa.
#O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exeder 30% do salário ou então o...
#...empréstimo será negado.
print('====== DESAFIO 36 ======')
casa = float(input('Qual o valor da casa? R$'))
salário = float(input('Qual o valor do salário? R$'))
prazo = int(input('Qual o prazo para pagamento em anos? '))
if casa / (prazo * 12) > 30 / 100 * salário:
    print('Empréstimo negado.')
else:
    print('Empréstimo aprovado!')