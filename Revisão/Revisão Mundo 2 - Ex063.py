#Ex 063 -> Sequência de Fibonacci.
num = int(input('Informe quantos elementos da Sequência de Fibonacci deseja mostrar: '))
elemento1 = 0
elemento2 = 1
print(f'{elemento1} -> {elemento2} -> ', end='')
cont = 3
mais = num
total = 0
while mais > 0:
    total = total + mais
    while cont <= total:
        elemento3 = elemento1 + elemento2
        print(f'{elemento3} -> ', end='')
        elemento1 = elemento2
        elemento2 = elemento3
        cont = cont + 1
    print('PAUSA')
    mais = int(input('Informe quantos elementos mais deseja mostrar ou, tecle [0] para sair: '))
print(f'FIM! Foram mostrados {total} elementos.')