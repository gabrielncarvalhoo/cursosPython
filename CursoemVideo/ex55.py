maior = 0
menor = 0
lista = []
for c in range(1, 4):
    peso = float(input('Digite o {}° peso: '.format(c)))
    lista += [peso]
print('O maior peso foi de {:.1f}Kg'.format(max(lista)))
print('O menor peso foi de {:.1f}Kg'.format(min(lista)))
