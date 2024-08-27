'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição
correta de inserção (sem usar o sort()).
No final, mostre a lista ordenada na tela.'''
print(f'{'DESAFIO 80':=^45}')
num = list()
for c in range(0, 5):
    n = (int(input('Digite um número: ')))
    if c == 0 or n > num[-1]:
        num.append(n)
        print(f'"{n}" foi adicionado no final da lista.')
    else:
        pos = 0
        while pos < len(num):
            if n <= num[pos]:
                num.insert(pos, n)
                print(f'"{n}" foi  adicionado na posição {pos} da lista')
                break
            pos = pos + 1
print('=' * 30)
print(f'Os valores digitados, ordenados em ordem crescente fica assim: {num}')
