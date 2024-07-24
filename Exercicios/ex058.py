'''Ex58: Melhore o jogo do DESAFIO 28 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram
nescessários para vencer.'''
print(f'{'DESAFIO 58':=^45}')
from random import randint
from time import sleep
print('Vamos jogar? Escolha um intervalo numérico a partir de 2 dígitos (quanto maior o intervalo, maior a dificuldade):')
n1 = int(input('Número inicial: '))
n2 = int(input('Número final: '))
computador = randint(n1, n2)
print(f'Ok! Vamos começar... vou pensar em um número entre {n1} e {n2}. Tente adivinhar...')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual número você acha que eu pensei? '))
    print('PROCESSANDO...')
    sleep(0.5)
    palpites = palpites + 1 # Pode ser escrito: palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Pensei em um número maior... Tente novamente.')
        else:
            print('Pensei em um número menor... Tente novamente.')
print(f'Acertou com {palpites} tentativas.')
