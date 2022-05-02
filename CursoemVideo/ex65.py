num = media = soma = cont = 0
numero = []
continuar = ''
while continuar in 'S':
    num = int(input('Digite um número: '))
    continuar = input('Quer continuar? [S/N] ').upper()[0]
    cont += 1
    soma += num
    numero.append(num)
media = soma / cont
print('Você digitou {} números e a média foi {:.2f}'.format(cont, media))
print('O maior valor foi {} e o menor foi {}'.format(max(numero), min(numero)))
