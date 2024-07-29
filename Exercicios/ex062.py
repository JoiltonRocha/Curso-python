'''Ex62: Melhore o desafio 61, perguntando para o usuário se ele quer mostrar mais alguns
termos. O programa encerra quando ele disser que quer mostrar 0 termos.'''
print(f'{'DESAFIO 62':=^45}')
primeirotermo = int(input('Digite o primeiro termo:'))
razão = int(input('Digite a razão: '))
termo = primeirotermo
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo = termo + razão
        cont = cont + 1
    print('PAUSA')
    mais = int(input('Quer mostrar mais quantos termos? '))
print(f'FIM. Foram mostrados {total} termos.')