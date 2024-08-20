#Ex 069 -> Analise de dados do grupo.
totp18 = totM = totF20 = totalgeral = 0
while True:
    print(f'{'CADASTRE UMA PESSOA':*^45}')
    idade = int(input('Informe a idade: '))
    sexo = str(input('Informe o sexo [F/M]: ')).upper().strip()[0]
    while sexo not in 'FM':
        sexo = str(input('Informe o sexo [F/M]: ')).upper().strip()[0]
    totalgeral = totalgeral + 1
    if idade >= 18:
        totp18 = totp18 + 1
    if sexo in 'M':
        totM = totM + 1
    if sexo in 'F' and idade < 20:
        totF20 = totF20 + 1
    continuar = str(input('Deseja cadastrar outra pessoa [S/N]: ')).upper().strip()[0]
    while continuar not in 'SN':
        print('Escolha "S" para sim ou "N" para não.')
        continuar = str(input('Deseja cadastrar outra pessoa [S/N]: ')).upper().strip()[0]
    if continuar in 'N':
        break
print(f'TOTAL DE PESSOAS CADASTRADAS: {totalgeral}.')
if totp18 == 0:
    print('-> Nenhuma pessoa cadastrada com mais de 18 anos.')
else:
    if totp18 == 1:
        print('-> Uma pessoa cadastrada com mais de 18 anos.')
    else:
        print(f'-> {totp18} pessoas cadastradas com mais de 18 anos.')
if totM == 0:
    print('-> Nenhum homem cadastrado.')
else:
    if totM == 1:
        print('-> Apenas um homem cadastrado.')
    else:
        print(f'-> {totM} homens cadastrados.')
if totF20 == 0:
    print('-> Nenhuma mulher cadastrada com menos de 20 anos.')
else:
    if totF20 == 1:
        print('-> Uma mulher com mais de 18 anos cadastrada.')
    else:
        print(f'-> {totF20} mulheres cadastradas com menos de 20 anos.')
