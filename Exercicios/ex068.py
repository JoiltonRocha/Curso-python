'''Ex68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido
quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''
print(f'{'DESAFIO 68':=^45}')
from random import randint
opções = ('ÍMPAR', 'PAR')
print('VAMOS JOGAR PAR OU ÍMPAR')
v = 0
while True:
    print('-' * 40)
    pc = randint(1, 10)
    jogador = int(input('Digite um número: '))
    total = pc + jogador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador, {pc}. Total {total}.')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    print('-' * 40)
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v = v + 1
        else:
            print(f'Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 != 0:
            print('Você VENCEU!')
            v = v + 1
        else:
            print('Você PERDEU!')
            break
    print('-' * 40)
    print('Vamos jogar novamente?')
print(f'GAME OVER! Você venceu {v} vezes.')
