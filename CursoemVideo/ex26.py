frase = str(input('Digite uma frase: ')).strip()
print('Quantas vezes aparecem a letra A? {}'.format(frase.upper().count('A')))
print('Em que posição a letra "A" aparece pela primeira vez? {}'.format(frase.upper().find('A')+1))
print('Em qual posição aparece a umtima letra "A"? {}'.format(frase.upper().rfind('A')+1))