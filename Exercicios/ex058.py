'''Ex58: Melhore o jogo do DESAFIO 28 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram
nescessários para vencer.'''
print(f'{'DESAFIO 58':=^45}')
import random
from time import sleep
print('Vamos jogar? Escolha um intervalo numérico a partir de 2 dígitos (quanto maior o intervalo, maior a dificuldade):')
computador = jogador = 0
c = 1
while computador == jogador:
    print('PARABÉNS! Você acertou!')
    print('Não foi desssa vez. Continue tentando.')
    n1 = int(input('Número inicial: '))
    n2 = int(input('Número final: '))
    computador = random.randint(n1, n2) #Faz o computador "pensar"
    print(f'Vou pensar em um número entre {n1} e {n2}. Tente adivinhar...')
    jogador = int(input('Qual número você pensou? ')) #Jogador tenta adivinhar
    print('PROCESSANDO...')
    sleep(2)
    if jogador == computador:
    print('PARABÉNS! Você acertou!')
    else:
    print(f'GANHEI! Eu pensei no número {computador} e não no {jogador}')
