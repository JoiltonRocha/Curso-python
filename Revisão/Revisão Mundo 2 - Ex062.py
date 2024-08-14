#Ex 062 -> Ex 061 melhorado.
primeirotermo = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Informe a razão da PA: '))
termo = primeirotermo
total = 0
cont = 1
mais = 10
while mais > 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo = termo + razao
        cont = cont + 1
    print('PAUSA')
    mais = int(input('Informe mais quantos termos da PA deseja mostrar ou, tecle [0] para sair: '))
print(f'FIM! Foram mostrados {total} termos.')

