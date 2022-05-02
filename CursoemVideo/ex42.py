a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
lado1 = (b - c) < a < (b + c)
lado2 = (a - c) < b < (a + c)
lado3 = (a - b) < c < (a + b)
if lado1 and lado2 and lado3:
    if a != b != c != a:
        print('O triângulo é escaleno.')
    elif a == b == c:
        print('O triângulo é equilátero.')
    else:
        print('O triângulo é isóceles.')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo.')