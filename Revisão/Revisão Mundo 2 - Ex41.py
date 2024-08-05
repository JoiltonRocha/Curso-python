#Ex 041 -> Categoria Natação.
mirim = infantil = junior = senior = master = cont = 0
from datetime import date
while True:
    anonasc = int(input('Digite o ano de nascimento: '))
    anoatual = date.today().year
    idade = anoatual - anonasc
    if idade <= 9:
        print(f'IDADE: {idade} anos -> CATEGORIA: Mirim.')
        mirim = mirim + 1
        cont = cont + 1
    elif idade > 9 and idade <= 14:
        print(f'IDADE: {idade} anos -> CATEGORIA: Infantil.')
        infantil = infantil + 1
        cont = cont + 1
    elif idade >14 and idade <= 19:
        print(f'IDADE: {idade} anos -> CATEGORIA: Sênior.')
        senior = senior + 1
        cont = cont + 1
    elif idade >= 20:
        print(f'IDADE {idade} anos -> CATEGOTRIA: Master.')
        master = master + 1
        cont = cont + 1
    continuar = str(input('Deseja informar outro atleta [S/N]?')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Deseja informar outro atleta [S/N]?')).upper().strip()[0]
    if continuar in 'N':
        break
print(f'FIM!!!')
print(f'Foram informados {cont} atletas. DOS QUAIS:')
if mirim > 0:
    print(f'MIRIM: {mirim}.')
if infantil > 0:
    print(f'INFANTIL: {infantil}.')
if junior > 0:
    print(f'JUNIOR: {junior}.')
if senior > 0:
    print(f'MASTER: {master}.')