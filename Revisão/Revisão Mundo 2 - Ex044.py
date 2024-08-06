#Ex 044 -> Preço por forma de pagamento.
while True:
    preço = float(input('Informe o valor do produto: '))
    print('''FORMAS DE PAGAMENTO:
    [1] À vista dinheiro ou cheque
    [2] Cartão em 1x
    [3] Cartão em 2x
    [4] Cartão em 3x ou mais''')
    fpgto = str(input('Informe a forma de pagamento: '))
    while fpgto not in '1234':
        print('Opção inválida.')
        print('''FORMAS DE PAGAMENTO:
        [1] À vista dinheiro ou cheque
        [2] Cartão em 1x
        [3] Cartão em 2x
        [4] Cartão em 3x ou mais''')
        fpgto = str(input('Informe a forma de pagamento: '))
    if fpgto == '1':
        total = preço - (preço * 10 / 100)
        print(f'Pagando dessa forma, a compra de R${preço:.2f} fica por R${total:.2f}. 10% de desconto.')
    elif fpgto == '2':
        total = preço - (preço * 5 / 100)
        print(f'Pagando dessa forma, a compra de R${preço:.2f} fica por R${total:.2f}. 5% de desconto.')
    elif fpgto == '3':
        total = preço
        print(f'Pagando dessa forma, você parcela a compra com valor de R${preço:.2f} em até 2x sem acréscimo.')
    elif fpgto == '4':
        total = preço + (preço * 20 / 100)
        parcelas = int(input('Quantidade de parcelas (entre 3x e 12x): '))
        vlrparcelas = total / parcelas
        print(f'Sua compra será parcelada em {parcelas}x de R${vlrparcelas:.2f} (COM JUROS).')
        print(f'Sua compra de R${preço:.2f} vai custar R${total:.2f} no final.')
    continuar = str(input('Deseja informar outra compra? [S/N] -> ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Deseja informar outra compra? [S/N] -> ')).upper().strip()[0]
