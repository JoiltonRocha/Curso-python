#Ex 064 -> Tratando vários valores v1.0.
cont = num = soma = 0
while num != 999:
    num = int(input('informe um número: '))
    cont = cont + 1
    if num != 999:
        soma = soma + num
print(f'Foram mostrados {cont} nomeros que totalizaram um valor de {soma}.')
