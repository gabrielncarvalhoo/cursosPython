produto1 = float(input('Valor do primeiro produto: R$'))
produto2 = float(input('Valor do segundo produto: R$'))
produto3 = float(input('Valor do terceiro produto: R$'))
melhor = min(produto1, produto2, produto3)
print('Você deve comprar o produto que tem o valor de R${:.2f}'.format(melhor))