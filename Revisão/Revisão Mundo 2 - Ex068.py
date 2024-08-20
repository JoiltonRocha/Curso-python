#Ex 068 -> Jogo do Par ou Ímpar.
from random import randint
print('VAMOS JOGAR PAR OU ÍMPAR')
v = 0
while True:
    computador = randint(1, 10)
    jogador = int(input('Digite o seu número: '))
    total = computador + jogador
    tipo = str(input('Par ou Ímpar [P/I] -> ')).upper().strip()[0]
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar [P/I] -> ')).upper().strip()[0]
    print(f'Você jogou {jogador} e o computador {computador}, totalizando {total}, ', end='')
    print('QUE É PAR.' if total % 2 == 0 else 'QUE É ÍMPAR.')
    if tipo in 'P':
        if total % 2 == 0:
            v = v + 1
            print('Você VENCEU! Pode jogar novamente.')
        else:
            break
    elif tipo in 'I':
        if total % 2 != 0:
            v = v + 1
            print('Você VENCEU! Pode jogar novamente.')
        else:
            break
    print('+-' * 30)
if v == 0:
    print(f'GAME OVER! Sem vitória.')
else:
    if v == 1:
        print(f'GAME OVER! Você venveu {v} apenas uma vez.')
    elif v > 1:
        print(f'GAME OVER! Você venceu {v} vezes consecutivas.')
