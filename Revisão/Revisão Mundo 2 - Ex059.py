#Ex 059 -> Criando menu de opções.
from time import sleep
num1 = int(input('Informe um número: '))
num2 = int(input('Informe outro número: '))
while True:
    opção = int(input('''* * * OPÇÕES: * * * 
[1] Somar 
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
Opção desejada: '''))
    while opção < 1 or opção >= 6:
        print('*' * 30)
        print('Escolha uma opção válida.')
        print('*' * 30)
        print('''* * * OPÇÕES: * * *
[1] Somar 
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa''')
        opção = int(input('Opção desejada: '))
    if opção == 4:
        num1 = int(input('Informe um número: '))
        num2 = int(input('Informe outro número: '))
    if opção == 1:
        print(f'A soma entre {num1} e {num2} é {num1 + num2}.')
    if opção == 2:
        print(f'O produto entre {num1} e {num2} é {num1 * num2}.')
    if opção == 3:
        if num1 == num2:
            print('Os dois números são iguais.')
        elif num1 > num2:
            print(f'Entre {num1} e {num2} o maior é {num1}.')
        else:
            print(f'Entre {num1} e {num2} o maior é {num2}.')
    if opção == 5:
        break
print('Finalizando...')
sleep(1)
print('Calculadora finalizada.')
