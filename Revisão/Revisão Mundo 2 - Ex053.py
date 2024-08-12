#Ex 053 -> Palíndromo.
frase = str(input('Digite uma frase: ')).upper().strip()
palavras = frase.strip()
junto = join(palavras)
inverso = ''
print(f'Você digitou a frase {frase}: ')