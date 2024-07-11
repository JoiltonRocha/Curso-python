#Ex015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado...
#... e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro ...
#... custa R$60,00 por dia mais R$0,15 por Km rodado.
km = float(input('Quantos km rodados? '))
dias = int(input('Quantos dias alugados? '))
preço = (km * 0.15) + (dias * 60)
print(f'O valor total do aluguel é: R${preço:.2f}')
