#Ex 070 -> Estatísticas em produtos.
total = tot1000 = nomecaro = 0
while True:
    print(F'{'PRODUTO':*^30}')
    produto = str(input('Produto: '))
    preço = float(input('Preço: R$ '))
    total = total + preço
    if preço > 1000:
        tot1000 = tot1000 + 1
    if preço == 1:
        nomecaro = produto
    else:
        if preço > nomecaro:
            nomecaro = produto
print('Compra finalizada.')
