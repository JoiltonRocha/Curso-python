#Ex024: Crie um progama que leia o nome de uma cidade e diga se ela começa ou não com a palavra "SANTO".
print('====== DESAFIO 024 ======')
nat = str(input('Onde você nasceu? ')).strip()
print(nat[:5].upper() == 'SANTO')
