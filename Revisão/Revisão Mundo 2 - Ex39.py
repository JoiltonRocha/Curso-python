#Ex: 039 -> Alistamento militar.
from datetime import date
diferença = 0
idade = ''
while True:
    print(f'{' SERVIÇO MILITAR ':*^90}')
    anonasc = int(input('Digite o ano de nascimento: '))
    sexo = str(input('Informe o sexo [M/F]: ')).upper().strip()[0]
    anoatual = date.today().year
    anoalistamento = anonasc + 18
    idade = anoatual - anonasc
    while sexo not in 'MF':
        sexo = str(input('Informe o sexo [M/F]: ')).upper().strip()[0]
    if sexo in 'F':
        print('ATENÇÃO! No Brasil o alistamento militar não é obrigatório para pessoas do sexo feminino.')
    if idade == 18:
        print(f'Quem nasceu em {anonasc} hoje tem {idade} anos. Essa é idade certa para o alistamento militar.')
    if idade < 18:
        diferença = 18 - idade
        if diferença == 1:
            print(f'Quem nasceu em {anonasc} tem {idade} anos em {anoatual}. Falta {diferença} ano para atingir a idade para o alistamento militar.')
        else:
            print(f'Quem nasceu em {anonasc} hoje tem {idade} anos. Faltam {diferença} anos para atingir a idade para o alistamento militar.')
        print(f'Seu alistamento será em {anoalistamento}.')
    if idade > 18:
        diferença = idade - 18
        if diferença == 1:
            print(f'Quem nasceu em {anonasc} hoje tem {idade} anos. Passou {diferença} ano da idade para o alistamento militar.')
        else:
            print(f'Quem nasceu em {anonasc} hoje tem {idade} anos. Passaram-se {diferença} anos da idade para o alistamento militar.')
        print(f'Seu alistamento foi em {anoalistamento}.')
    print('*' * 90)
    continuar = str(input('Continuar? [S/N]')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Continuar? [S/N]')).upper().strip()[0]
    if continuar in 'N':
        break
