salario = float(input('Qual o seu salário? R$'))
print('O salário era de R${:.2f}'.format(salario))
if salario <= 280:
    aumento = salario * 0.2
    total = salario + aumento
    print('Após o aumento de 20%, ou seja, R${:.2f}, o salário passou a ser R${:.2f}.'.format(aumento, total))
elif salario > 280 and salario < 700:
    aumento = salario * 0.15
    total = salario + aumento
    print('Após o aumento de 15%, ou seja, R${:.2f}, o salário passou a ser R${:.2f}.'.format(aumento, total))
elif salario >= 700 and salario < 1500:
    aumento = salario * 0.1
    total = salario + aumento
    print('Após o aumento de 10%, ou seja, R${:.2f}, o salário passou a ser R${:.2f}.'.format(aumento, total))
else :
    aumento = salario * 0.05
    total = salario + aumento
    print('Após o aumento de 05%, ou seja, R${:.2f}, o salário passou a ser R${:.2f}.'.format(aumento, total))

