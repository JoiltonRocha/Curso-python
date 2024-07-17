#Ex34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1.250,00, calcule um aumento de 10%.
#Para salários inferiores ou iguais, o aumento é de 15%.
print('====== DESAFIO 34 ======')
s = float(input('Qual o valor do salário? R$'))
if s <= 1250:
    print(f'Você recebeu um aumento de 15%. Seu novo salário é de R${(s * 0.15) + s:.2f}.')
else:
    print(f'Você recebeu um aumento de 10%. Seu novo salário é de R${(s * 0.10) + s:.2f}.')