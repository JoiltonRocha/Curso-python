#Ex029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, ...
#...mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
print('====== DESAFIO 29 ======')
v = float(input(f'Digite a velocidade em Km/h: '))
if v > 80:
    ex = v - 80
    vlr = (ex * 7)
    print(f'MULTADO! Você ultrapassou em {ex}Km/h a velocidade máxima permitida que é de 80Km/h e foi multado em R${vlr:.2f}')
    print('Dirija com segurança!')
else:
    print('Mantenha-se dentro da velocidade de segurança!')
