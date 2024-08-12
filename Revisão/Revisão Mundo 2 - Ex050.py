#Ex 050 -> Soma de números.
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
    cont = soma = 0
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
    continuar = str(input('Deseja informar outros números? [S/N] -> '))
    if continuar in 'N':
        break
