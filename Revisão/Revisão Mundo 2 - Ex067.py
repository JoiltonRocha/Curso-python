#Ex 067 -> Tabuada v3.0.
num = 1
while num > 0:
    num = int(input('Digite um número para ver sua tabuada: '))
    if num < 0:
        break
    else:
        for c in range(1, 11):
            print(f'{num} x {c:2} = {c * num:3}')
