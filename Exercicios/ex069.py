'''Ex69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o
prigrama deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos.'''
print(f'{'DESAFIO 69':=^45}')
totp18 = totm = totf20 = 0
while True:
    print(f'{'CADASTRE UMA PESSOA':-^40}')
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()[0]
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()[0]
    if idade > 18:
        totp18 = totp18 +1
    if sexo in ('M'):
        totm = totm + 1
    if sexo in 'F' and idade < 20:
        totf20 = totf20 + 1
    if sexo not in 'MF':
    print('-' * 40)
    continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if continuar not in 'SN':
        while continuar not in 'SN':
            continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    print('=' * 40)
    if continuar in 'N':
        break
print(f'{'CADASTRO FINALIZADO!':*^65}')
print(f'* Total de pessoas cadastradas com idade superior a 18 anos: {totp18}  *')
print(f'* Total de homens cadastrados: {totm}                                *')
print(f'* Total de mulheres cadastradas com idade inferior a 20 anos: {totf20} *')
print('*' * 65)