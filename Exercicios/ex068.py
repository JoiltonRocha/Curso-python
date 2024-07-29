'''Ex68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido
quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''
print(f'{'DESAFIO 68':=^45}')
from random import randint
opções = ('ÍMPAR', 'PAR')
print('VAMOS JOGAR PAR OU ÍMPAR')
while True:
    pc = randint(0, 10)
    print(pc)
    '''jogador = int(input('Digite um número: '))'''
