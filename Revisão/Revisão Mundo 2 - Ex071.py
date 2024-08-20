#Ex 071 -> Simulador de caixa eletrônico.
saque = int(input('Informe o valor do saque: R$'))
total = saque
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total = total - céd
        totcéd = totcéd + 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R${céd:.2f}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
