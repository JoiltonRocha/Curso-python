#Ex33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
print('====== DESAFIO 33 ======')
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
#Verificando quem é menor
menor = n1
if n2 < n1 and n3 < n2:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
#Verificando quem é maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f'O menor número digitado foi {menor}.')
print(f'O maior número digitado foi {maior}.')
