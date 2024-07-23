'''Ex49: Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que
agora utilizando um laço for.'''
print(f'{'DESAFIO 49':=^45}')
n = int(input('Digite um número: '))
for c in range(1, 9+1):
    t = n * c
    print(t)
