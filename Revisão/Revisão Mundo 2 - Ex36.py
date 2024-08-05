#Ex: 036 -> Empréstimo bancário.
valor = float(input('Digite o valor da casa: '))
salário = float(input('Digite o salário: '))
prazo = int(input('Digite o prazo para pagamento em anos: '))
parcela = valor / (prazo * 12)
if parcela > 30 / 100 * salário:
    print(f'Valor da parcela R${parcela:.2f}. Empréstimo negado')
elif parcela <= 30 / 100 * salário:
    print(f'Valor da parcela R${parcela:.2f}. Empréstimo APROVADO!')
print('Obrigaso por usar os nossos serviços')
