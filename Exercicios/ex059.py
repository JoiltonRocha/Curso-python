'''Ex59: Crie um programa que leia dois valores e mostre um menu na tela:
[1] Somar.
[2] Multiplicar.
[3] Maior.
[4] Novos números.
[5] Sair do programa.
Seu programa deverá realizar a operação solicitada em cada caso.'''
print(f'{'DESAFIO 59':=^45}')
opção = 0
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
while opção != 5:
    print('''O que deseja fazer?
    [1] Somar.
    [2] Multiplicar.
    [3] Maior.
    [4] Novos números.
    [5] Sair do programa.''')
    opção = int(input('Opção: '))
    if opção == 1:
        r = n1 + n2
        print(f'O resultado da soma entre {n1} e {n2} é {r}.')
    if opção == 2:
        r = n1 * n2
        print(f'O resultado da multiplicação entre {n1} e {n2} é {r}.')
    if opção == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}.')
        elif n2 > n1:
            print(f'{n2} é maior que {n1}.')
        else:
            print(f'{n1} é igual a {n2}')
    if opção == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    if opção == 5:
        print('Você escolheu sair.')
    if opção >= 6:
        print('''Opção inválida. Tente novamente.
        [1] Somar.
        [2] Multiplicar.
        [3] Maior.
        [4] Novos números.
        [5] Sair do programa.''')
