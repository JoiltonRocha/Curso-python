#Ex: 037 -> Base numérica.
while True:
    num = int(input('Digite um número: '))
    base = ('Binário', 'Octal', 'Hexadecimal')
    opção = str(input('''Base de conversão: 
    - [1] Binário
    - [2] Octal
    - [3] Hexadecimal
    Opção: '''))
    while opção not in '123':
        print('Opção inválida. Escolha uma das opções.')
        opção = str(input('''Base de conversão: 
        - [1] Binário
        - [2] Octal
        - [3] Hexadecimal
        Opção: '''))
    if opção == '1':
        conversão = bin(num)[2:]
        base = 'BINÁRIO'
    elif opção == '2':
        conversão = oct(num)[2:]
        base = 'OCTAL'
    elif opção == '3':
        conversão = hex(num)[2:]
        base = 'HEXADECIMAL'
    print(f'O número {num} convertido para {base} é {conversão}.')
    continuar = str(input('Deseja continuar? [S/N] -> ')).upper().strip()[0]
    while continuar not in 'SN':
        print('Opção inválida.')
        continuar = str(input('Deseja continuar? [S/N] -> ')).upper().strip()[0]
    if continuar in 'N':
        break
print('FIM!!!')
