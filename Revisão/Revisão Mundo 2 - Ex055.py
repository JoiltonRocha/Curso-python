#Ex 055-> Maior e menor.
maior = 0
menor = 0
while True:
    for c in range(1, 6):
        peso = float(input(f'Digite o peso da {c}ª pessoa: '))
        if c == 1:
            maior = peso
            menor = peso
        else:
            if peso > maior:
                maior = peso
            if peso < menor:
                menor = peso
    print(f'O maior peso lido foi {maior}Kg.')
    print(f'O menor peso lido foi {menor}Kg.')
    continuar = str(input('Deseja continuar? [S/N] -> ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Deseja informar continuar? [S/N] -> ')).upper().strip()[0]
    if continuar in 'N':
        break