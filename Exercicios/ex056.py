'''Ex56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do
programa, mostre:
> A média de idade do grupo.
> Qual é o nome do homem mais velho.
> Quantas mulheres têm menos de 20 anos.'''
print(f'{'DESAFIO 56':=^45}')
totidade = 0
mediaidade = 0
maiorhomem = 0
nomevelho = ''
totmulher20 = 0
nomemulher20 = ''
for c in range(1, 5):
    print(f'* * * * {c}ª PESSOA * * * *')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    totidade = totidade + idade
    if c == 1 and sexo in 'Mm':
        maiorhomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maiorhomem:
        maiorhomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 = totmulher20 + 1
mediaidade = totidade / c
print(f'A média de idade do grupo é de {mediaidade:.0f} anos.')
print(f'O homem mais velho tem {maiorhomem} anos e ele se chama {nomevelho}')
print(f'O total de mulheres com menos de 20 anos é {totmulher20}.')
