'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem
de colocação. Depois mostre:
a) Apenas os 5 primeiros colocados.
b) Os últimos colocados da tabela.
c) Uma lista com os times em ordem afabética.
d) Em que posição na tabela está o time da Chapecoense.'''
print(f'{'DESAFIO 73':=^45}')
tupla = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport Recife',
         'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta',
         'Atlético-GO')
print('*' * 50)
print(f'-> Lista de times do Brasileirão: {tupla}')
print('*' * 50)
print(f'-> Os cinco primeiros são: {tupla[0:5]}')
print('*' * 50)
print(f'-> Os quatro últimos são: {tupla[-4:]}')
print('*' * 50)
print(f'-> Times em ordem alfabética: {sorted(tupla)}')
print('*' * 50)
print(f'-> O Chapecoense está na {tupla.index('Chapecoense')+1}ª posição.')
