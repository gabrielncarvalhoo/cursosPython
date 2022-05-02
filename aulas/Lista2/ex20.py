salario = float(input('Quando você ganha por hora? R$'))
horas = float(input('Quantas horas você trabalha por mês?'))
total = salario * horas
print('Você ganha R${:.2f} por mês.'.format(total))