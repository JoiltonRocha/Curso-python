#Ex 058 -> Jogo desafio 028.
from random import randint
tentativa = 0
print('COMPUTADOR: Vamos jogar? Informe um intervalo numérico, lembrando que quanto maior o intervalo, maior a dificuldade.')
inicio = int(input('Informe o número inicial: '))
final = int(input('Informe o número final: '))
computador = randint(inicio, final)
print(f'COMPUTADOR: Ok. Vou pensar em um número entre {inicio} e {final}. tente acertar qual número eu pensei.')
jogador = int(input('Seu palpite -> '))
tentativa = tentativa + 1
while computador != jogador:
    if computador > jogador:
        print('Mais')
    if computador < jogador:
        print('Menos')
    jogador = int(input('Seu palpite -> '))
    tentativa = tentativa + 1
    if computador == jogador:
        print('Parabéns você acertou.')
        break
print(f'Foram nescessários {tentativa} tentativas.')