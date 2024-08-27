'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar
se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''
print(f'{'DESAFIO 83':=^45}')
expressão = str(input('Digite uma expressão: '))
pilha = list()
for simb in expressão:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Expressão válida!')
else:
    print('Expressão inválida!')
