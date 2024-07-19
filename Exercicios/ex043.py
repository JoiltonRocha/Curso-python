'''Ex43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC  e mostre seu status, de acordo com a tabela abaixo:
 - Abaixo de 18.5Kg: Abaixo do peso.
 - Entre 18.5 e 25Kg: Peso ideal.
 - 25 até 30Kg: Sobrepeso.
 - 30 até 40Kg: Obesidade.
 - Acima de 40Kg: Obesidade mórbida.'''
print('====== DESAFIO 43 ======')
print('*' * 30)
print('CÁLCULO DE IMC')
print('*' * 30)
alt = float(input('Altura: '))
peso = float(input('Peso: '))
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
