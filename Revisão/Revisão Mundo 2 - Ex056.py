#Ex 056 -> Analisador completo.
from time import sleep
totidade = mediaidade = maiorhomem = totmulher20 = 0
nomevelho = nomemulher20 = ''
for c in range(1, 5):
    print(f'* * * * * {c}ª PESSOA * * * * *')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] -> ')).upper().strip()
    totidade = totidade + idade
    if c == 1 and sexo in 'M':
        maiorhomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maiorhomem:
        maiorhomem = idade
        nomevelho = nome
    if sexo in 'F' and idade < 20:
        totmulher20 = totmulher20 + 1
    media = totidade / c
print('Analisando ', end='')
sleep(0.5)
for c in range(1, 10):
    print('.', end='')
    sleep(1)
sleep(0.5)
print(f'\n-> A média de idade do grupo informado é {media} anos.')
print(f'-> O homem mais velho tem {maiorhomem} anos e se chama {nomevelho}.')
if totmulher20 == 0:
    print('-> Não foi informado nenhuma mulher com idade inferior a 20 anos.')
else:
    if totmulher20 == 1:
        print(f'-> {totmulher20} mulher com idade inferior a 20 anos.')
    else:
        print(f'-> {totmulher20} mulheres com idade inferior a 20 anos.')