#Ex 070 -> Estatísticas em produtos.
total = totmil = menorpreço = cont = 0
barato = ''
while True:
    print(F'{'PRODUTO':*^45}')
    produto = str(input('Produto: '))
    preço = float(input('Preço: R$ '))
    total = total + preço
    cont = cont + 1
    if preço > 1000:
        totmil = totmil + 1
    if cont == 1:
        menorpreço = preço
        barato = produto
    else:
        if preço < menorpreço:
            menorpreço = preço
            barato = produto
    continuar = str(input('Deseja informar outro produto? [S/N] -> ')).upper().strip()[0]
    while continuar not in 'SN':
        print('Escolha [S] para sim ou [N] para não.')
        continuar = str(input('Deseja informar outro produto? [S/N] -> ')).upper().strip()[0]
    if continuar in 'N':
        break
print('*' * 45)
print('Compra finalizada.')
print(f'Total da compra -> R${total:.2f}')
print(f'Produto com preço maior que R$1.000,00 -> ')
print(f'Produto mais barato -> {barato}.')
print(f'Valor do produto mais barato -> {menorpreço:.2f}.')
