frase = str(input('Digite uma frase: ')).upper().split()
frase = ''.join(frase)
inverso = frase[::-1]
'''inverso = ''
for letra in range(len(frase) -1, -1, -1):
    inverso += frase[letra]'''
print('Você digitou {} e o inverso é {}.'.format(frase, inverso))
if frase == inverso:
    print('É um palíndromo.')
else:
    print('Não é um palíndromo.')