'''Ex41: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento...
...de um atleta e mostre sua categoria de acordo com a idade:
- Até 9 anos: MIRIM.
- Até 14 anos: INFANTIL.
- Até 19 anos: JUNIORS.
- Até 20 anos: SÊNIOR.
- Acima: MASTER.'''
from datetime import date
print('====== DESAFIO 41 ======')
print('*' * 35)
print('CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
print('*' * 35)
anonasc = int(input('Qual o ano de nascimento? '))
anoatual = date.today().year
idade = anoatual - anonasc
if idade <= 9:
    print(f'Com {idade} anos sua categoria é: MIRIM.')
elif idade >= 10 and idade <= 14:
    print(f'Com {idade} anos sua categoria é: INFANTIL.')
elif idade >= 15 and idade <= 19:
    print(f'Com {idade} anos sua categoria é: JUNIOR.')
elif idade == 20:
    print(f'Com {idade} anos sua categoria é: SÊNIOR.')
else:
    print(f'Com {idade} anos sua categoria é: MASTER.')
