#Ex 053 -> Palíndromo.
while True:
    frase = str(input('Digite uma frase: ')).strip().upper()
    palavras = frase.split()
    junto = ''.join(palavras)
    inverso = ''
    for c in range(len(junto) - 1, -1, -1):
        inverso = inverso + junto[c]
    print(f'O inverso de {junto} é {inverso}.')
    if junto == inverso:
        print('Temos um palíndromo!')
    else:
        print('A frase digitada não é um palíndromo!')
    continuar = str(input('Deseja informar outra frase? [S/N] -> ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Deseja informar outra frase? [S/N] -> ')).upper().strip()[0]
    if continuar in 'N':
        break