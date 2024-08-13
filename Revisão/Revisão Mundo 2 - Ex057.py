#Ex 057 -> Validação de dados.
total = totf = totm = 0
while True:
    sexo = str(input('Informe o sexo [F/M]: ')).upper().strip()[0]
    while sexo not in 'FM':
        sexo = str(input('''Opção inválida. 
    Informe o sexo [F/M]: ''')).upper().strip()[0]
    if sexo in 'FM':
        total = total + 1
        print('Registrado.', end=' ')
        continuar = str(input('Deseja informar outro sexo? [S/N] -> ')).upper().strip()[0]
        if sexo in 'F':
            totf = totf + 1
        if sexo in 'M':
            totm = totm + 1
    while continuar not in 'SN':
        continuar = str(input('Deseja informar outro sexo? [S/N] -> ')).upper().strip()[0]
    if continuar in 'N':
        break
print(f'Foram registrados {total} sexos, sendo {totf} femininos e {totm} masculinos.')