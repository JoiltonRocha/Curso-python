'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''
valores = list()
maior = menor = cont = posmaior = posmenor = 0
for c in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
    if len(valores) == 1:
        maior = valores[0]
        menor = valores[0]
        print(enumerate(valores))
        #posmaior = enumerate(valores)
        #posmenor = enumerate(valores)
    else:
        cont = cont + 1
        if valores[cont] > maior:
            maior = valores[cont]
            posmaior = enumerate(valores)
        if valores[cont] < menor:
            menor = valores[cont]
            posmenor = enumerate(valores)
print(f'Você digitou os valores {valores}')
print(f'O menor valor digitado foi {menor} na posição {posmenor}.')
print(f'O maior valor digitado foi {maior} na posição {posmaior}.')

