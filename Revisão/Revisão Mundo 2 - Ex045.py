#Ex 045 -> Jokenpô
from random import randint
from time import sleep
while True:
    itens = ('PEDRA', 'PAPEL', 'TESOURA')
    computador = randint(0, 2)
    print('''Suas opções:
    [0] PEDRA
    [1] PAPEL
    [2] TESOURA''')
    jogador = int(input('Qual sua jogada? '))
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ!!!')
    sleep(0.5)
    print('*' * 25)
    print(f'Computador -> {itens[computador]}')
    print(f'Jogador -> {itens[jogador]}')
    print('*' * 25)
    if computador == 0: #COMPUTADOR JOGOU PEDRA.
        if jogador == 0: #JOGADOR JOGOU PEDRA.
            print('EMPATE!')
        elif jogador == 1: #JOGADOR JOGOU PAPEL.
            print('Jogador GANHOU!')
        elif jogador == 2: #JOGADOR JOGOU TESOURA.
            print('Computador GANHOU!')
        else:
            print('Jogada inválida! Escolha uma opção válida.')

    elif computador == 1: #COMPUTADOR JOGOU PAPEL
        if jogador == 0: #JOGADOR JOGOU PEDRA.
            print('Computador GANHOU!')
        elif jogador == 1: #JOGADOR JOGOU PAPEL.
            print('EMPATE!')
        elif jogador == 2: #JOGADOR JOGOU TESOURA.
            print('Jogador GANHOU!')
        else:
            print('Jogada inválida! Escolha uma opção válida.')

    elif computador == 2: #COMPUTADOR JOGOU TESOURA
        if jogador == 0: #JOGADOR JOGOU PEDRA.
            print('Jogador GANHOU!')
        elif jogador == 1: #JOGADOR JOGOU PAPEL.
            print('Computador GANHOU!')
        elif jogador == 2: #JOGADOR JOGOU TESOURA.
            print('EMPATE!')
        else:
            print('Jogada inválida! Escolha uma opção válida.')
    continuar = str(input('Vamos jogar mais uma vez? [S/N] ')).upper().strip()[0]
    while continuar not in 'SN':
        print('Opção inválida.')
        continuar = str(input('Vamos jogar mais uma vez? [S/N] ')).upper().strip()[0]
    if continuar in 'N':
        break
print('FIM!!!')