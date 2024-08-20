#Ex 066 -> Vários números com flag.
cont = soma = 0
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    cont = cont + 1
    soma = soma + num
print(f'Foram informados {cont} números, que somados totalizam {soma}.')
