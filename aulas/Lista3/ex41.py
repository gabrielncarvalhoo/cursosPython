valor = int(input('Quanto deseja sacar? R$'))
cem = valor // 100
cinquenta = (valor // 10 % 10) // 5
dez = (valor // 10 % 10) % 5
cinco = (valor // 1 % 10) // 5
um = (valor // 1 % 10) % 5

print('Notas de R$100,00 = {}'.format(cem))
print('Notas de R$50,00 = {}'.format(cinquenta))
print('Notas de R$10,00 = {}'.format(dez))
print('Notas de R$5,00 = {}'.format(cinco))
print('Notas de R$1,00 = {}'.format(um))