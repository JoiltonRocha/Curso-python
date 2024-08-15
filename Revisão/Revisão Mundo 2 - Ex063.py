#Ex 063 -> Sequência de Fibonacci.
num = int(input('Informe quantos elementos da Sequêcia de Fibonacci deseja mostrar: '))
termo1 = 0
termo2 = 1
print(f'{termo1} -> {termo2} -> ', end='')
cont = 3
while cont <= num:
    termo3 = termo1 + termo2
    print(f'{termo3} -> ', end='')
    termo1 = termo2
    termo2 = termo3
    cont = cont + 1
print('FIM!')