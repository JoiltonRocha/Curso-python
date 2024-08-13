#Ex 040 -> Média de notas.
contador = total = 0
qnota = 1

while True:
    nota = float(input(f'Digite a {qnota}ª nota: '))
    qnota = qnota + 1
    contador = contador + 1
    total = total + nota
    continuar = str(input('Deseja informar mais notas? [S/N] -> ')).upper().strip()[0]
    while continuar not in 'SN':
        ontinuar = str(input('Deseja informar mais notas? [S/N] -> ')).upper().strip()[0]
    if continuar in 'N':
        break
media = total / contador
if contador > 0:
    if contador == 1:
        print(f'Foi informada apenas 1 nota.')
        print(f'MÉDIA -> {media}')
    else:
        print(f'Foram informadas {contador} notas.')
        print(f'MÉDIA -> {media:.1f}')
