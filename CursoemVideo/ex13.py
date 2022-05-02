salario = float(input('O valor do salário é de R$'))
aumento = salario + (salario * 0.15)
print('O salário inicial era de R${:.2f}, e passou a ser R${:.2f}, após os 15% de aumento.'.format(salario, aumento))
