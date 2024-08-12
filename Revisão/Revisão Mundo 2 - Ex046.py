#Ex 046 -> Contadorgem regressiva.
from time import sleep
while True:
    inicial = int(input('Deseja iniciar a contagem regressiva de quanto: '))
    for c in range (inicial, 0, -1):
        print(c)
        sleep(1)
    print('BUUUUUUUM!!!')
    continuar = str(input('Deseja fazer outra contagem? [S/N] -> ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Deseja fazer outra contagem? [S/N] -> ')).upper().strip()[0]
    if continuar in 'N':
        break
print('FIM!!!')