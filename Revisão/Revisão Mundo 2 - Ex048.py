#Ex 048 -> Soma números ímpares.
tipo = ['PARES E ÍMPARES', 'ÍMPARES', 'PARES']
while True:
    inicio = int(input('Digite o número inicial: '))
    final = int(input('Digite o número final: '))
    intervalo = int(input('Digite o intervalo: '))
    pi = int(input('''*Escolha uma das opções de filtro para os números desejados:
    [0] PARES E ÍMPARES
    [1] APENAS ÍMPARES
    [2] APENAS PARES
    Sua opção -> '''))
    soma = cont = 0
    for c in range(inicio, final, intervalo):
        if pi == 0:
                cont = cont + 1
                soma = soma + c
        elif pi == 1:
            if c % 2 == 1:
                cont = cont + 1
                soma = soma + c
        elif pi == 2:
            if c % 2 == 0:
                cont = cont + 1
                soma = soma + c
    print(f'A soma dos {cont} números {(tipo[pi])} entre {inicio} e {final - 1} é {soma}.')
    continuar = str(input('Gostaria de informar outro número? [S/N] -> ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Gostaria de informar outro número? [S/N] -> ')).upper().strip()[0]
        if continuar in 'N':
            break
print('FIM!!!')
