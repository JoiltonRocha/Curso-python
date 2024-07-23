'''Ex49: Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que
agora utilizando um laço for.'''
print(f'{'DESAFIO 49':=^45}')
n = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print(f'{n} x {c:2} = {n * c:2}')
