'''Desenvolva um proograma que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
a) Quantas vezes apareceu o valor 9.
b) Em que posição está foi digitado o primeiro valor 3.
c) Quais foram os números pares.'''
tupla = (int(input('Digite o 1º número: ')),
         int(input('Digite o 2º número: ')),
         int(input('Digite o 3º número: ')),
         int(input('Digite o 4º número: ')))
print(f'Você digitou os números {tupla}')
nove = (tupla.count(9))
if nove == 0:
    print('Não houve ocorrência do número 9.')
else:
    if nove == 1:
        print(f'Houve uma ocorrência do número 9.')
    elif nove > 1:
        print(f'Houveram {tupla.count(9)} ocorrências do número 9.')
if 3 in tupla:
    print(f'A primeira ocorrência do número 3 foi na posição {tupla.index(3)}')
else:
    print('Não houve ocorrência do número 3. ')
for c in tupla:
    if c % 2 == 0:
        totc = (len(c))
        print(f'Total: {totc}')
        print(f'{c}, ', end='')

