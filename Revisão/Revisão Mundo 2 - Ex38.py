#Ex: 38 -> Maior, menor ou igual.
continuar = ''
comp = igualdade = n1Mn2 = n1mn2 = 0
while continuar in 'S':
    print('-' * 35)
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro número: '))
    if num1 == num2:
        print(f'Os dois valores são iguais.')
        comp = comp + 1
        igualdade = igualdade + 1
    elif num1 < num2:
        print(f'O primeiro valor é menor.')
        comp = comp + 1
        n1mn2 = n1mn2 + 1
    else:
        print(f'O primeiro valor é maior.')
        comp = comp + 1
        n1Mn2 = n1Mn2 + 1
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
print('-' * 50)
print(f'Você escolheu sair. Foram feitas {comp} comparações, das Quais:')
if igualdade > 0:
    print(f'* {igualdade}: Os dois valores iguais.')
if n1mn2 > 0:
    print(f'* {n1mn2}: O primeiro menor que o segundo.')
if n1Mn2 > 0:
    print(f'* {n1Mn2}: O prdimeiro maior que o segundo.')