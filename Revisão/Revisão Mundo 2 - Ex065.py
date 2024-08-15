#Ex 065 -> Interrompendo funções while.
continuar = 'S'
cont = soma = media = maior = menor = 0
while continuar not in 'N':
    num = int(input('Digite um número: '))
    cont = cont + 1
    soma = soma + num
    continuar = str(input('Deseja continuar? [S/N] -> ')).upper().strip()[0]
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] -> ')).upper().strip()[0]
media = soma / cont
if cont == 1:
    print(f'''RESULTADO:
-> ATENÇÃO! Foi informado apenas um número. Informe mais para um melhor resultado.
-> A média de {num} é {media}.
-> O maior e o menor número é {num}.''')
else:
    print(f'''RESULTADO:
-> Foram informados {cont} números que somados totalizam {soma}.
-> A média entre eles é {media}.
-> O maior número digitado foi {maior}.
-> O menor número digitado foi {menor}.''')
