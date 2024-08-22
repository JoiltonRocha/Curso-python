'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem
de colocação. Depois mostre:
a) Apenas os 5 primeiros colocados.
b) Os últimos colocados da tabela.
c) Uma lista com os times em ordem afabética.
d) Em que posição na tabela está o time da Chapecoense.'''
print(f'{'DESAFIO 73':=^45}')
tupla = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print(f'Lista de times do Brasileirão: {tupla}')
print(f'Os cinco primeiros são: {tupla[1:6]}')
print(f'Ordem alfabética: {sorted(tupla)}')
