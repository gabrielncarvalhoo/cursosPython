a = int(input('Primeiro segmento: '))
b = int(input('Segundo segmento: '))
c = int(input('Terceiro segmento: '))
lado1 = (b - c) < a < (b + c)
lado2 = (a - c) < b < (a + c)
lado3 = (a - b) < c < (a + b)
if lado1 and lado2 and lado3:
    print('Os segmentos acima PODEM formar um triângulo.')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo.')