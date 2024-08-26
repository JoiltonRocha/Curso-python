'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''
print(f'{'DESAFIO 76':=^45}')
contprod = 0
contpreço = 1
tupla = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15, 'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9)
print('-' * 45)
print(f'{'LISTAGEM DE PREÇOS':^45}')
print(f'-' * 45)
for c in range(0, len(tupla)):
    print(f'{tupla[contprod]:.<30} R$ {tupla[contpreço]:.2f  }')
    contprod = contprod + 2
    contpreço = contpreço + 2
print('-' * 45)