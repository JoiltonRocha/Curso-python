'''Ex59: Crie um programa que leia dois valores e mostre um menu na tela:
[1] Somar.
[2] Multiplicar.
[3] Maior.
[4] Novos números.
[5] Sair do programa.
Seu programa deverá realizar a operação solicitada em cada caso.'''
print(f'{'DESAFIO 59':=^45}')
opção = 0
while opção != 5:
    n1 = int(input('Digite o primeiro valor: '))
    n2 = int(input('Digite o segundo valor: '))
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
        else:
            print(f'{n2} é maior que {n1}.')
    if opção == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
        print('''O que deseja fazer?
        [1] Somar.
        [2] Multiplicar.
        [3] Maior.
        [4] Novos números.
        [5] Sair do programa.''')
        opção = int(input('Opção: '))
    if opção == 5:
        print('Você escolheu sair.')