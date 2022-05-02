a = float(input('Comprimento do cateto oposto: '))
b = float(input('Comprimento do cateto adjacente: '))
h2 = (a ** 2) + (b ** 2)
h = h2 ** (1/2)
print('A hipotenusa é {:.2f}.'.format(h))

import math
hi = math.hypot(a, b)
print('A hipotenusa é {:.2f}.'.format(hi))
