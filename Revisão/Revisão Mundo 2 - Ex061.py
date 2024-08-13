#Ex 061 -> PA.
primeirotermo = int(input('Primeiro termo da PA: '))
qtd = int(input('Digite a quantidade de termos da PA: '))
razao = int(input('Razão da PA: '))
termo = primeirotermo
cont = 1
while cont <= qtd:
    print(f'{termo} -> ', end='')
    termo = termo + razao
    cont = cont + 1
print('FIM!')
