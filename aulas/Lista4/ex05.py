a = int(input('Qual o tamanho da primeira população? '))
taxaa = float(input('Qual a  sua taxa de crescimento? [%] '))
b = int(input('Qual o tamanho da segunda população? '))
taxab = float(input('Qual a sua taxa de crescimento? [%] '))
anos = 0
porcentagema = (taxaa / 100) + 1
porcentagemb = (taxab / 100) + 1
if a > b:
    while a > b:
        a *= porcentagema
        b *= porcentagemb
        anos += 1
elif b > a:
    while b > a:
        a *= porcentagema
        b *= porcentagemb
        anos += 1
else:
    print('As populações são iguais.')
print(f'Para a população menor passar a maior, demorou {anos} anos.')
