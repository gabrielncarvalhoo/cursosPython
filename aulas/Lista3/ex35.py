num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
num3 = int(input('Terceiro número: '))
lista = [num1, num2, num3]
lista.sort()
print('Ordem decrescente {}, {}, {}'.format(lista[2], lista[1], lista[0]))
