'''Ex61: Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10
primeiros termos da progressão usando a estrutura while.'''
print(f'{'DESAFIO 61':=^45}')
primeirotermo = int(input('Digite o primeiro termo:'))
razão = int(input('Digite a razão: '))
termo = primeirotermo
cont = 1
while cont <= 10:
    print(f'{termo} -> ', end='')
    termo = termo + razão
    cont = cont + 1
print('Acabou')