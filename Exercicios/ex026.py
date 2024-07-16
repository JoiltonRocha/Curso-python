#Ex026: Faça um programa que leia uma frase pelo teclado e mostre:
#a) Quantas vezes aparece a letra "A".
#b) Em que posição ela aparece a primeira vez.
#c)Em que posição ela aparece a última vez.
print('====== DESAFIO 026 ======')
frase = str(input('Digite uma frase: ')).upper().strip()
print(f'A letra A aparece {frase.count('A')} vezes na frase.')
print(f'A primeira letra A apareceu na posição {frase.find('A') + 1}.')
print(f'A última letra A apareceu na posição {frase.rfind('A') + 1}.')
