#Ex: 38 -> Maior, menor ou igual.
continuar = ''
comp = igualdade = n1Mn2 = n1mn2 = 0
while continuar in 'S':
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro número: '))
    if num1 == num2:
        print(f'{num1} é igual a {num2}.')
        comp = comp + 1
        igualdade = igualdade + 1
    elif num1 < num2:
        print(f'{num1} é menor que {num2}.')
        comp = comp + 1
        n1mn2 = n1mn2 + 1
    else:
        print(f'{num1} é maior que {num2}.')
        comp = comp + 1
        n1Mn2 = n1Mn2 + 1
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
print('-' * 50)
print(f'Você escolheu sair. Foram feitas {comp} comparações, das Quais:')
if igualdade > 0:
    print(f'* Os dois valores iguais: {igualdade}.')
if n1mn2 > 0:
    print(f'* O primeiro maior que o segundo: {n1mn2}.')
if n1Mn2 > 0:
    print(f'* O prdimeiro menor que o segundo: {n1Mn2}.')