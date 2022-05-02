dias = int(input('Dias alugados: '))
km = float(input('Km percorridos: '))
d = dias * 60
k = km * 0.15
print('O total a pagar é de R${:.2f}.'.format(d+k))
