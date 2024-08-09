#Ex 050 -> Soma de números.
cont = soma = 0
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
        for c in range(inicio, final, intervalo):
            cont = cont + 1
            soma = soma + c
        print(f'A soma dos {cont} números {(tipo[pi])} entre {inicio} e {final - 1} é {soma}.')
