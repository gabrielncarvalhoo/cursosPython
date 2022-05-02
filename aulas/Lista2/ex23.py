inteiro1 = int(input('Digite um número inteiro: '))
inteiro2 = int(input('Digite outro número inteiro: '))
real = float(input('Digite um número real: '))
calculo1 = (inteiro1 * 2) * ((1/2) * inteiro2)
calculo2 = (3 * inteiro1) + real
calculo3 = real ** 3
print('O produto do dobro do primeiro com metade do segundo é {}.'.format(calculo1))
print('A soma do triplo do primeiro com o terceiro é {}'.format(calculo2))
print('O terceiro elevado ao cubo é {}'.format(calculo3))