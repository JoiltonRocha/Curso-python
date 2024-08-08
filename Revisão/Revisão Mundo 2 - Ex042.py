#Ex 042 -> Tipos dos triângulos.
contador = equilatero = isosceles = escaleno = triangulo = ntriangulo = 0
tipotriangulo = ['EQUILÁTERO', 'ISÓSCELES', 'ESCALENO']
while True:
    r1 = float(input('Digite o primeiro segmanto: '))
    r2 = float(input('Digite o segundo segmento: '))
    r3 = float(input('Digite o terceiro segmento: '))
    contador = contador + 1
    if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
        triangulo = triangulo + 1
        if r1 == r2 == r3:
            equilatero = equilatero + 1
            print(f'{r1} mais {r2} mais {r3} formam um triângulo {tipotriangulo[0]}, quando todos os lados são iguais.')
        elif r1 == r2 or r2 == r3 or r1 == r3:
            isosceles = isosceles + 1
            print(f'{r1} mais {r2} mais {r3} formam um triângulo {tipotriangulo[1]}, quando ao menos dois lados são iguais.')
        else:
            escaleno = escaleno + 1
            print(f'{r1} mais {r2} mais {r3} formam um triângulo {tipotriangulo[2]}, quando todos os lados são diferentes.')
    else:
        ntriangulo = ntriangulo + 1
        print(f'Os segmentos informados não podem formar um triângulo pois não obedecem a condição de existência. ')
    continuar = str(input('Deseja informar outros três segmentos? [S/N ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Deseja informar outros três segmentos? [S/N ')).upper().strip()[0]
    if continuar in 'N':
        break
print('*' * 100 )
if contador > 0:
    if contador == 1:
        print(f'# Foi informado 1 conjunto de três segmentos. Que:')
    else:
        print(f'# Foram informados {contador} conjuntos de três segmentos. Dos quais:')
if ntriangulo > 0:
    if ntriangulo == 1:
        if contador == 1:
            print('NÃO FORMA TRIÂNGULO.')
        else:
            print(f'{ntriangulo} -> NÃO FORMA TRIÂNGULO.')
    else:
        print(f'{ntriangulo} -> NÃO FORMAM TRIÂNGULO.')
if triangulo > 0:
    if triangulo == 1:
        print(f'{triangulo} -> FORMA TRIANGULO.')
    else:
        print(f'{triangulo} -> FORMAM TRIANGULO.')
    print('* DOS QUE FORMAM TRIÂNGULO:')
if equilatero > 0:
    print(f'- {equilatero} -> EQUIÁTERO.')
if isosceles > 0:
    print(f'- {isosceles} -> ISÓSCELES.')
if escaleno > 0:
    print(f'- {escaleno} -> ESCALENO.')
