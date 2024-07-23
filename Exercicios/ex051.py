'''Ex51: Desenvolva um programa que leia o primeiro número e a razão de uma PA. No final,
mostre os 10 primeiros termos dessa progressão.'''
print(f'{'DESAFIO 51':=^45}')
primeirotermo = int(input('Digite o primeiro termo:'))
razão = int(input('Digite a razão: '))
décimotermo = primeirotermo + (10 - 1) * razão
for c in range(primeirotermo, décimotermo + razão, razão):
    print(f'{c}', end=' -> ')
print('Acabou')
