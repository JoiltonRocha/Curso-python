'''Crie um programa que tenha uma tupla totalmente preenchida com uma contagem po extenso, de zero até vinte.
Seu programa deverá mostrar ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''
print(f'{'DESAFIO 72':=^45}')
tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quize', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Opção inválida. ', end='')
print(f'Você digitou o número {tupla[num]}.')
