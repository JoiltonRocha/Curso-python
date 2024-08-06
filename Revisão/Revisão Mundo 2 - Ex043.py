#Ex 043 -> Cálculo IMC.
while True:
    peso = float(input('Digite seu peso: '))
    alt = float(input('Digite sua altura: '))
    imc = peso / alt ** 2
    if imc < 18.5:
        print(f'O seu imc é {imc:.1f}: Abaixo do peso.')
    elif imc >= 18.5 and imc < 25:
        print(f'O seu IMC é {imc:.1f}: Peso normal.')
    elif imc >= 25 and imc < 30:
        print(f'O seu IMC é {imc:.1f}: Sobrepeso.')
    elif imc >= 30 and imc < 40:
        print(f'O seu peso é {imc:.1f}: Obesidade.')
    else:
        imc >= 40
        print(f'O seu IMC é {imc:.1f}: Obesidade mórbida.')
    continuar = str(input('Deseja calcular outro IMC? [S/N] -> ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Deseja calcular outro IMC? [S/N] -> ')).upper().strip()[0]
    if continuar in 'N':
        break
print('FIM!!!')