'''Crie um program que simule o funcionamento se um caixa eletrônico. No início, pergunte
ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas
de cada valor serão entregues.
OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''
print(f'{'DESAFIO 71':=^45}')
#COMO EU TENTEI FAZER:
'''cinquenta = vinte = dez = um = resto1 = resto50 = resto20 = resto10 = 0
valor = int(input('Digite o valor a ser sacado: R$ '))
if valor % 50 == 0:
    cinquenta = valor / 50
if valor % 50 > 0:
    resto50 = valor % 50
    cinquenta = (valor - resto50) / 50
if resto50 == 20:
    resto20 = resto50
    vinte = resto20 / 20
if resto50 > 20:
    resto20 = resto50 % 20
    vinte = (resto50 - resto20) / 20
    if resto20 == 10:
        dez = resto20 / 10
    if resto20 % 10 > 0 and resto20 < 10:
        um = resto20
if resto50 < 20 and resto50 > 10:
    resto10 = resto50 % 10
    dez = (resto50 - resto10) / 10
    um = resto10
if resto50 == 10:
    resto10 = resto50
    dez = resto50 / 10
if resto50 < 10:
    um = resto50
if cinquenta > 0:
    print(f'{cinquenta:.0f} notas de R$50,00')
if vinte > 0:
    print(f'{vinte:.0f} notas de R$20,00')
if dez > 0:
    print(f'{dez:.0f} notas de R$10,00')
if um > 0:
    print(f'{um:.0f} notas de R$ 1,00')'''



#Bendito 'while'!
valor = int(input('Digite o valor a ser sacado: R$ '))
total = valor
céd = 50
totcéd = 0
print('-' * 45)
while True:
    if total >= céd:
        total = total - céd
        totcéd = totcéd + 1
    else:
        if totcéd > 0:
            print(f'{totcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('Essas cédulas serão entregues a seguir.')