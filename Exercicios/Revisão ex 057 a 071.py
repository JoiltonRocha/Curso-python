#ex057:
'''sexo = str(input('Informe o sexo [F/M]: ')).upper().strip()[0]
while sexo not in 'FM':
    sexo = str(input('Informe o sexo [F/M]: ')).upper().strip()[0]'''


#ex058:
'''from random import randint
computador = randint(0,10)
print('COMPUTADOR: Vamos jogar? Tente acertar o número que estou pensando...')
palpite = 0
while True:
    jogador = int(input('Seu palpite: '))
    if jogador < computador:
        palpite = palpite + 1
        print('Mais...')
    elif jogador > computador:
        palpite = palpite + 1
        print('Menos...')
    elif jogador == computador:
        break
print(f'Acertou na {palpite}ª tentativa.')'''


#ex059:
'''n1 = int(input('Informe um valor: '))
n2 = int(input('Informe outro valor: '))
while True:
    print('OPÇÕES:\n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa')
    opção = int(input('Sua escolha -> '))
    if opção == 1:
        r = n1 + n2
        print(f'A soma entre {n1} e {n2} é {n1 + n2}.')
        print('+' * 40)
    if opção == 2:
        print(f'A razaão entre {n1} e {n2} é {n1 * n2}')
        print('*' * 40)
    if opção == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}.')
            print('-+' * 20)
        elif n2 > n1:
            print(f'{n2} é maior que {n1}.')
            print('-+' * 20)
        else:
            print('Os dois valores informados são iguais.')
            print('-+' * 20)
    if opção == 4:
        print('x' * 40)
        n1 = float(input('Informe um valor: '))
        n2 = float(input('Informe outro valor: '))
    if opção == 5:
        print('!' * 40)
        print('Fim!')
        break
    if opção >= 6:
        print('!' * 40)
        print('Opção inválida.')'''


#ex060 !!!!!!!!!!!!!!!!!
'''num = int(input('Informe um número para ver seu fatorial: '))
print(f'O fatorial de {num} é {num}!= {num} x ', end='')
while num > 1:
    num = num - 1
    print(f'{num} x ', end='')'''


#ex061:
'''primeirotermo = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Informe a razão da PA: '))
termo = primeirotermo
print(f'{termo} -> ', end='')
total = 10
cont = 1
while cont < total:
    termo = termo + razao
    cont = cont + 1
    print(f'{termo} -> ', end='')
print('Fim!')'''


#ex062:
'''primeirotermo = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Informe a razão da PA: '))
termo = primeirotermo
print(f'{termo} -> ', end='')
mais = 10
cont = 1
total = 0
while mais > 0:
    total = total + mais
    while cont < total:
        termo = termo + razao
        print(f'{termo} -> ', end='')
        cont = cont + 1
    print('PAUSA')
    mais = int(input('Deseja mostrar mais quantos termos? '))
print(f'Foram mostrados {total} termos.')'''


#ex063:
'''num = int(input('Informe a quantidade de elementos da Sequência de Fibonacci que deseja mostrar: '))
total = num
t1 = 0
t2 = 1
print(f'{t1} -> {t2} -> ', end='')
cont = 3
while cont <= total:
    t3 = t1 + t2
    cont = cont + 1
    print(f'{t3} -> ', end='')
    t1 = t2
    t2 = t3
print('Fim!')'''


#ex064:
'''cont = soma = 0
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    cont = cont + 1
    soma = soma + num
print(f'Foram informados {cont} números que somados, totalizam {soma}.')'''


#ex065:
'''continuar = 'S'
cont = soma = media = menor = maior = 0
while continuar not in 'N':
    num = int(input('Digite um número: '))
    cont = cont + 1
    soma = soma + num
    media = soma / cont
    if cont == 1:
        menor = num
        maior = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    continuar = str(input('Deseja informar outro número? [S/N] -> ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Deseja informar outro número? [S/N] -> ')).upper().strip()[0]
print(f'FIM!\nForam digitados {cont} números e a média entre eles é {media:.1f}!\nO menor número digitado foi {menor} e o maior, {maior}.')'''


#ex066:
'''cont = soma = 0
while True:
    num = int(input('Digite um número [999 para parar]: '))
    if num == 999:
        break
    cont = cont + 1
    soma = soma + num
print(f'Foram informados {cont} números que somados totalizam {soma}.')'''


#ex067:
'''while True:
    num = int(input('Digite um número para ver sua tabuada: '))
    n = 1
    while n < 11:
        print(f'{num} x {n:2} = {n * num:3}')
        n = n + 1
    if num < 0:
        break'''


#ex068:
'''from random import randint
v = 0
while True:
    computador = randint(1, 10)
    print('Vamos jogar PAR OU ÍMPAR?\nDIGITE:\n[0] Para PAR\n[1] Para ÍMPAR')
    opção = int(input('Sua escolha: '))
    jogador = int(input('Digite um número: '))
    print('=' * 60)
    total = computador + jogador
    print(f'Computador jogou {computador} e jogador {jogador} totalizando {total} ', end='')
    print(f'que é PAR.' if total % 2 == 0 else 'que é ÍMPAR. ', end='')
    if opção == 0:
        if total % 2 == 0:
            v = v + 1
            print('Você venceu.')
        else:
            print('Você perdeu.')
            break
    if opção == 1:
        if total % 2 == 0:
            print('Você perdeu.')
            break
        else:
            v = v + 1
            print('Você venceu')
if v == 0:
    print('GAME OVER! Nenhuma vitória.')
elif v == 1:
    print('GAME OVER! Uma vitória.')
else:
    print(f'GAME OVER! {v} vitórias consecutivas.')'''


#ex069:
'''maior18 = totH = totF = totM = 0
while True:
    print(F'{'CADASTRE UMA PESSOA':+^45}')
    idade = int(input('Informe a idade: '))
    sexo = str(input('Informe o sexo [F/M]: ')).upper().strip()[0]
    while sexo not in 'FM':
        sexo = str(input('Informe o sexo [F/M]: ')).upper().strip()[0]
    if idade >= 18:
        maior18 = maior18 + 1
    if sexo in 'M':
        totM = totM + 1
    if sexo in 'F' and idade <= 20:
        totF = totF + 1
    continuar = str(input('Deseja cadastrar outra pessoa [S/N]: ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Deseja cadastrar outra pessoa [S/N]: ')).upper().strip()[0]
    if continuar in 'N':
        break
print('=' * 45)
print('RESUMO:')
if maior18 > 0:
    print(f'-> ', end='')
    print(f'Foi cadastrada ' if maior18 == 1 else 'Foram cadastradas ', end='')
    print(maior18, end='')
    print(' pessoa com 18 anos ou mais.' if maior18 == 1 else ' pessoas com 18 anos ou mais.')
if totM > 0:
    print(f'-> ', end='')
    print(f'Foi cadastrado ' if totM == 1 else ' Foram cadastrados', end='')
    print(totM, end='')
    print(' homem.' if totM == 1 else ' homens.')
if totF > 0:
    print(f'-> ', end='')
    print(f'Foi cadastrada ' if totF == 1 else 'Foram cadastradas ', end='')
    print(totF, end='')
    print(' mulher com 20 anos ou menos.' if totF == 1 else ' mulheres com 20 anos ou menos.')'''


#ex070
'''soma = prodmil = cont = prodbarato = contmil = 0
nomebarato = nomemil = ''
while True:
    print(f'{'CADASTRO DE PRODUTOS':+^40}')
    produto = str(input('PRODUTO: '))
    preço = float(input('PREÇO: '))
    cont = cont + 1
    soma = soma + preço
    if preço >= 1000:
        contmil = contmil + 1
        if contmil == 1:
            prodmil = preço
            nomemil = produto
        elif preço > prodmil:
            prodmil = preço
            nomemil = produto
    if cont == 1:
        prodbarato = preço
        nomebarato = produto
    elif preço < prodbarato:
        prodbarato = preço
        nomebarato = produto
    continuar = str(input('Deseja continuar? [S/N] -> ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] -> ')).upper().strip()[0]
    if continuar in 'N':
        break
print('=' * 40)
print(f'TOTAL: R$ {soma:.2f}')
if prodmil > 0:
    print(f'-> Quantidade de produto maior ou igual a R$ 1.000,00: {contmil}')
    print(f'-> O mais caro: {nomemil}. Preço: {prodmil}')
print(f'-> Produto mais barato: {nomebarato}. Preço: {prodbarato:.2f} ')'''


#ex071:
'''saque = int(input('Informe o valor do saque: R$ '))
total = saque
céd = 200
cont = 0
while True:
    if total >= céd:
        total = total - céd
        cont = cont + 1
    else:
        if cont > 0:
            print(f'-> {cont} cédulas de R$ {céd}')
        if céd == 200:
            céd = 100
        elif céd == 100:
            céd = 50
        elif céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 5
        elif céd == 5:
            céd = 1
        cont = 0
        if total == 0:
            break'''


lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
for c in lanche:
    print(c)



