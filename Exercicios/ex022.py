#Ex022: Crie um programa que leia o nome completo de uma pessoa e mostre:
#a) O nome com todas as letras maiúsculas.
#b) O nome com todas as letras minúsculas.
#c) Quantas letras ao todo (sem considerar espaços).
#d) Quantas letras tem o primeiro nome.
print('====== DESAFIO 022 ======')
nome = str(input('Digite seu nome completo: ')).strip()
print(f'Seu nome com letras maiúsculas: {nome.upper()}')
print(f'Seu nome com letras minúsculas: {nome.lower()}')
print(f'Quantidade total de letras: {len(nome) - nome.count(' ')}')
print(f'Quantidade de letras do primeiro nome: {nome.find(' ')}')
#OUTRA FORMA PARA FAZER "A QUANTIDADE DE LETRAS DO PRIMEIRO NOME":
#separa = nome.split()
#print(f'Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras.')
