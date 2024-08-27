'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''
print(f'{'DESAFIO 78':=^45}')
valores = list()
maior = menor = cont = posmaior = posmenor = 0
for c in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
    if len(valores) == 1:
        maior = valores[0]
        menor = valores[0]
        posmaior = enumerate(valores[cont])
        posmenor = enumerate(valores[cont])
    else:
        cont = cont + 1
        if valores[cont] > maior:
            maior = valores[cont]
            posmaior = valores[cont]
        if valores[cont] < menor:
            menor = valores[cont]
            posmenor = valores[cont]
for pos, v in enumerate(valores):
    print('Fim')
print(f'Você digitou os valores {valores}')
print(f'O menor valor digitado foi {menor} na posição {pos}.')
print(f'O maior valor digitado foi {maior} na posição {pos}.')
