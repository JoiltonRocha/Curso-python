#Ex 051 -> PA
while True:
    soma = cont = 0
    primeirotermo = int(input('Digite o primeiro termo:'))
    razão = int(input('Digite a razão: '))
    décimotermo = primeirotermo + (10 - 1) * razão
    for c in range(primeirotermo, décimotermo + razão, razão):
        cont = cont + 1
        soma = soma + c
        print(f'{c}', end=' -> ')
    print(f'Formaram informados {cont} termos, que somados, toralizam {soma}.')
    continuar = str(input('Deseja informar outros termos? [S/N] -> ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Deseja informar outra PA? [S/N] -> ')).upper().strip()[0]
    if continuar in ('N'):
        break
print(f'FIM!!!')