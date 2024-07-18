'''Ex39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''
from datetime import date
print('====== DESAFIO 39 ======')
print('*' * 30)
print('SERIÇO DE ALISTAMENTO MILITAR')
print('*' * 30)
anonasc = int(input('Ano de nascimento: '))
anoatual = date.today().year
idade = anoatual - anonasc
if idade == 18:
    print(f'Quem nasceu em {anonasc}, hoje ({anoatual}) está com {idade} anos, idade certa para o Alistamento Militar.')
elif idade < 18:
    diferença = 18 - idade
    print(f'Quem nasceu em {anonasc}, hoje ({anoatual}) está com {idade} anos, falta {diferença} anos para o Alistamento Militar.')
else:
    idade > 18
    diferença = idade - 18
    print(f'Quem nasceu em {anonasc}, hoje ({anoatual}) está com {idade} anos, passou {diferença} anos do prazo de Alistamento Militar.')
print('*Utilizamos a data do dispositivo atual para fazer os cálculos. Verifique se a data do seu dispositivo está correta')
