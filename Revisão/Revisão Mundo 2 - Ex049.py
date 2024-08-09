#Ex 049 -> Tabuada.
while True:
    n = int(input('Digite um número para ver sua tabuada: '))
    for c in range (1, 11):
        print(f'{n} x {c:2} = {n * c:3}')
    continuar = str(input('Deseja informar outro número? [S/N] -> ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Deseja informar outro número? [S/N] -> ')).upper().strip()[0]
    if continuar in 'N':
        break
print('FIM!!!')
