#Crie um algoritimo que leia um número e mostre o seu dobro, trplo e raiz quadrada.
print('====== DESAFIO 06 ======')
n = int(input('Digite um número: '))
d = n * 2
t = n * 3
rq = n ** (1/2)
print(f'O dobro de {n} é {d}, o triplo é {t} e a raiz quadrada é {rq:.2f}')
