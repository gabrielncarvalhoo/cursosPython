salario = float(input('Informe seu salário: R$'))
if salario > 1250:
    porcentagem = 0.10
else:
    porcentagem = 0.15
aumento = (salario * porcentagem) + salario
print('Seu salário era de R${:.2f} e passou a ser R${:.2f}'.format(salario, aumento))