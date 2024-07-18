'''Ex40: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma...
mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO.
- Média entre 5.0 e 6.9: RECUPERAÇÃO.
- Média 7.0 ou superior: APROVADO.'''
print('====== DESAFIO 40 ======')
print('*' * 30)
print('NOTA DE CORTE:')
print('*APROVADO: 7.0 ou mais.\n*RECUPERAÇÃO: Entre 5.1 e 6.9.\n*REPROVADO: 5.0 ou menos.')
print('*' * 30)
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media <= 5:
    print(f'A média entre {nota1} e {nota2} é {media}. Infelizmente você não atingiu a nota miníma e foi REPROVADO.')
elif media > 5 and media < 6.9:
    print(f'A média entre {nota1} e {nota2} é {media}. Você tem mais uma oportunidade na RECUPERAÇÃO. Faça bom uso.')
else:
    media >= 7
    print(f'A média entre {nota1} e {nota2} é {media}. Parabéns! Você está aprovado!')
