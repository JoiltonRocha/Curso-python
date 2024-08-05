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
    total.apend(nota1)
    continuar = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
    while continuar not in 'SN':
        ontinuar = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
    if continuar in 'N':
        break

    media = (nota1 + nota2) / contador
print(total)
