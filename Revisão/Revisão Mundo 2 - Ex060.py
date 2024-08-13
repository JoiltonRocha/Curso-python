#Ex 060 -> Calculo do fatorial.

#COM WHILE -> Opção 01:
'''num = int(input('Digite um número para calcular seu fatorial: '))
c = num
f = 1
print(f'{num}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
    c = c - 1
print(f)'''

#COM WHILE -> Opção 02:
'''num = int(input('Digite um número para calcular seu Fatorial: '))
cont = result = 1
while cont <= num:
    result = result * cont
    cont = cont + 1
print(f' O Fatorial de {num} é {result}.')'''

#COM FOR:
'''num = int(input('Digite um número para calcular seu fatorial: '))
c = num
f = 1
print(f'{num}! = ', end='')
for c in range(num, 0, -1):
    print(c, end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
    c = c - 1
print(f)'''

#COM MÓDULO:
'''from math import factorial
num = int(input('Digite um número para calcular seu Fatorial: '))
f = factorial(num)
print(f'O Fatorial de {num} é {f}')'''
