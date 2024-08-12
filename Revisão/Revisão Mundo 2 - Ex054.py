#Ex 054 -> Maioridade.
from datetime import date
somamais = somamin = soma = 0
while True:
    anoatual = date.today().year
    anonasc = int(input('Digite o ano de nascimento: '))
    idade = anoatual - anonasc
    if idade >= 18:
        somamais = somamais + 1
    else:
        somamin = somamin + 1
    soma = soma + 1
    continuar = str(input('Deseja informar outro ano de nascimento? [S/N] -> ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Deseja informar outro ano de nascimento? [S/N] -> ')).upper().strip()[0]
    if continuar in 'N':
        break
print(f'Foram informados {soma} anos de nascimento. Dos quais:')
if somamais > 0:
    print(f'{somamais:2} -> Com idade igual ou maior que 18 anos.')
if somamin > 0:
    print(f'{somamin:2} -> Com idade menor que 18 anos.')



