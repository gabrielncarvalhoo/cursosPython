from datetime import date
contmaior = 0
contmenor = 0
for c in range(1, 8):
    ano = int(input('Em qual ano a {}° pessoa nasceu? \n'.format(c)))
    idade = date.today().year - ano
    if idade >= 18:
        contmaior += 1
    else:
        contmenor += 1
print('{} - Maior de idade.'.format(contmaior))
print('{} - Menor de idade.'.format(contmenor))