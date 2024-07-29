'''Ex65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução
mostre a média entre todos os valores e qual foi o maior e o menor valor lido. O programa deve
perguntar ao usuário se ele quer ou não continuar a digitar valores.'''
print(f'{'DESAFIO 65':=^45}')
continuar = 'S'
cont = soma = media = 0
while continuar not in 'N':
    num = int(input('Digite um número: '))
    cont = cont + 1
    soma = soma + num
    media = soma / cont
    continuar = str(input('Quer continuar digitando [S/N]? ')).upper().strip()[0]
    if continuar not in 'SN':
        while continuar not in 'SN':
            print('Opção inválida. Escolha [S] para continuar ou [N] para finalizar.')
            continuar = str(input('Quer continuar digitando [S/N]? ')).upper().strip()[0]
print(f'FIM. Foram digitados {cont} número e a média entre eles é {media:.1f}.')
