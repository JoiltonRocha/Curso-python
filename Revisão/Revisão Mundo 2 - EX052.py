#Ex 052 -> Números primos.
while True:
    num = int(input('Digite um número para descobrir se ele é primo ou não: '))
    total = 0
    for c in range(1, num + 1):
        if num % c == 0:
            print('\033[33m', end='')
            total = total + 1  # Pode ser escrito: total += 1
        else:
            print('\033[31m', end='')
        print(f'{c} ', end='')
    print(f'\n\033[mO número {num} foi divisível {total} vezes.')
    if total == 2:
        print('E por isso ele É PRIMO!')
    else:
        print('E por isso ele NÃO É PRIMO!')
    continuar = str(input('Deseja informar outro número? [S/N] -> ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Deseja informar outro número? [S/N] -> ')).upper().strip()[0]
    if continuar in 'N':
        break
