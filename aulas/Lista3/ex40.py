num = int(input('Digite um número de 0 até 1000: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
lista1 = '{} milhar, {} centena, {} dezena e {} unidade'.format(m, c, d, u)
lista2 = '{} centena, {} dezena e {} unidade'.format(c, d, u)
lista3 = '{} dezena e {} unidade'.format(d, u)
if num < 10:
    if u <= 1:
        print('{} unidade.'.format(u))
    else:
        print('{} unidades.'.format(u))
elif num >= 10 and num < 100:
    if u > 1:
        lista3 = lista3.replace('unidade', 'unidades')
    if d > 1:
        lista3 = lista3.replace('dezena', 'dezenas')
    print(lista3)
elif num >= 100 and num < 1000:
    if u > 1:
        lista2 = lista2.replace('unidade', 'unidades')
    if d > 1:
        lista2 = lista2.replace('dezena', 'dezenas')
    if c > 1:
        lista2 = lista2.replace('centena', 'centenas')
    print(lista2)
elif num == 1000:
    if u > 1:
        lista1 = lista1.replace('unidade', 'unidades')
    if d > 1:
        lista1 = lista1.replace('dezena', 'dezenas')
    if c > 1:
        lista1 = lista1.replace('centena', 'centenas')
else:
    print('Número Inválido')