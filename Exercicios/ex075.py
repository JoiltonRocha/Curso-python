'''Desenvolva um proograma que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
a) Quantas vezes apareceu o valor 9.
b) Em que posição está foi digitado o primeiro valor 3.
c) Quais foram os números pares.'''
contpar = 0
tupla = (int(input('Digite o 1º número: ')),
         int(input('Digite o 2º número: ')),
         int(input('Digite o 3º número: ')),
         int(input('Digite o 4º número: ')))
print('=' * 50)
print(f'Você digitou os números {tupla}')
nove = (tupla.count(9))
if nove == 0:
    print('Não houve ocorrência do número 9.')
else:
    if nove == 1:
        print(f'Houve uma ocorrência do número 9.')
    elif nove > 1:
        print(f'Houveram {nove} ocorrências do número 9.')
if 3 in tupla:
    print(f'A primeira ocorrência do número 3 foi na {tupla.index(3)+1}ª posição.')
else:
    print('Não houve ocorrência do número 3. ')
for n in tupla:
    if n % 2 == 0:
        contpar = contpar + 1
if contpar == 0:
    print('Não houve ocorrência de números pares.')
else:
    if contpar == 1:
        print(f'Houve uma ocorrência de número par. O número {n}.')
    else:
        print(f'Houveram {contpar} ocorrências de números pares:', end=' ')
        for n in tupla:
            if n % 2 == 0:
                print(f'{n} ', end='')
print(f'\n')