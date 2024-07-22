'''Ex42: Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- Equilátero: todos os lados iguais.
- Isósceles: dois lados iguais.
- Escaleno: todos os lados diferentes.'''
print('====== DESAFIO 35 ======')
r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2 and r1 == r2 and r1 == r3 and r2 == r3:
    print('Os segmentos acima Formam um triângulo EQUILÁTERO!')
elif r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2 and r1 == r2 or r1 == r3 or r2 == r3:
    print('Os segmentos acima formam um triângulo ISÓSCELES.')
elif r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2 and r1 != r2 and r1 != r3 and r2 != r3:
    print('Os segmentos acima formam um triângulo ESCALENO.')
else:
    print('Os segmentos acima não podem formar triângulo!')

'''OUTRA FORMA
r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima Formam um triângulo ', end='')
    if r1 == r2 == r2:
        print('EQUILÁTERO!')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('ISÓSCELES!')
    else:
        print('ESCALENO!')
else:
    print('Os segmentos acima não podem formar triângulo!')'''