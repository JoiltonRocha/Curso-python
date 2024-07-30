'''Ex68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido
quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''
print(f'{'DESAFIO 68':=^45}')
from random import randint
opções = ('ÍMPAR', 'PAR')
print('VAMOS JOGAR PAR OU ÍMPAR')
pc = randint(0, 10)
numpc = pc
if pc % 2 == 0:
    pc = 'PAR'
else:
    pc = 'ÍMPAR'
print(numpc)
print(f'Computador escolheu  {pc}')
njogador = int(input('Digite um número: '))
jogador = str(input('Par ou Ímpar? [P/I]')).upper().strip()[0]
if (njogador + numpc) % 2 == 0 and pc in 'PAR':
    pc =