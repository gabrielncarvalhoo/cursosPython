casa = float(input('Valor da casa: R$'))
salario = float(input('Qual o seu salário: R$'))
anos = int(input('Pretende pagar em quantos anos: '))
parcela = casa / (anos * 12)
per30 = salario * 0.3
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}'.format(casa, anos, parcela))
if parcela <= per30:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')