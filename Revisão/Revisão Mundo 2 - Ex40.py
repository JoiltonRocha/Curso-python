#Ex 040 -> Média de notas.
total = []
contador = total = 0
qnota = 1
while True:
    nota1 = float(input(f'Digite a {qnota}ª nota: '))
    qnota = qnota + 1
    contador = contador + 1
    nota2 = float(input(f'Digite a {qnota}ª nota: '))
    qnota = qnota + 1
    contador = contador + 1
    continuar = str(input('Deseja informar mais notas? [S/N] -> ')).upper().strip()[0]
    while continuar not in 'SN':
        ontinuar = str(input('Deseja informar mais notas? [S/N] -> ')).upper().strip()[0]
    if continuar in 'N':
        break
    if contador == 2:
        media = (qnota(1) + qnota(2)) / contador
    if contador == 4:
        media = (qnota(1) + qnota(2) + qnota(3) + qnota(4)) / contador
print(media)
