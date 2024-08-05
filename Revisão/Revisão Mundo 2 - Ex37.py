#Ex: 037 -> Base numérica.
num = int(input('Digite um número: '))
base = ('Binário', 'Octal', 'Hexadecimal')
base = int(input('''Base de conversão: 
- [1] Binário
- [2] Octal
- [3] Hexadecimal
Opção: '''))
if base == 1:
    conversão = bin(num)[2:]
    base = 'Binária'
elif base == 2:
    conversão = oct(num)[2:]
    base = 'Octal'
elif base == 3:
    conversão = hex(num)[2:]
    base = 'Hexadecimal'
else:
    while base not in '123':
        base = int(input('''Base de conversão: 
        - [1] Binário
        - [2] Octal
        - [3] Hexadecimal
        Opção: '''))
print(f'O número {num} convertido para base {base} é {conversão}.')