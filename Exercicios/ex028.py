#Ex028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5...
#... e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa...
#... deverá escrever na tela se o usuário venceu ou perdeu.
import random
print('====== DESAFIO 29 ======')
print('Vamos jogar? Digite um intervalo de 5 números e tente acertar qual número vou pensar:')
n1 = int(input('Número inicial: '))
n2 = int(input('Número final: '))
print('...Hum... deixa eu pensar...')
num = random.randint(n1, n2)
print(f'Já sei! {num}!')
n3 = int(input('Qual número você pensou? '))
print('Parabéns, você acertou.' if num == n3 else 'Voce errou, vamos tentar novamente?')
