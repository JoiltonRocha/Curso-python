#Ex 048 -> Soma números ímpares.
soma = cont = 0
tipo = ['PARES E ÍMPARES', 'ÍMPARES', 'PARES']
while True:
    inicio = int(input('Digite o número inicial: '))
    final = int(input('Digite o número final: '))
    intervalo = int(input('Digite o intervalo: '))
    pi = int(input('''*Escolha uma das opções de filtro paras os números desejados:
    [0] PARES E ÍMPARES
    [1] APENAS ÍMPARES
    [2] APENAS PARES
    Sua opção -> '''))
    if pi == 0:
        for c in range (inicio, final, intervalo):
            cont = cont + 1
            soma = soma + c
        print(f'A soma dos {cont} números {(tipo[pi])} entre {inicio} e {final} é {soma}.')
    elif pi == 1 or pi == 2:
        for c in range(inicio, final, intervalo):
            if c % 2 == pi:
                cont = cont + 1
                soma = soma + c
        print(f'A soma dos {cont} números {(tipo[pi])} entre {inicio} e {final} é {soma}.')
    continuar = str(input('Gostaria de informar outro número? [S/N] -> ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Gostaria de informar outro número? [S/N] -> ')).upper().strip()[0]
    if continuar in 'N':
        break
print('FIM!!!')
