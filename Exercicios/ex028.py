#Ex028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5...
#... e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa...
#... deverá escrever na tela se o usuário venceu ou perdeu.
#COMO EU FIZ:
import random
from time import sleep
print('====== DESAFIO 28 ======')
print('Vamos jogar? Escolha um intervalo numérico a partir de 2 dígitos (quanto maior o intervalo, maior a dificuldade):')
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
