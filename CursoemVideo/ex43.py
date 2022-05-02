peso = float(input('Digite seu peso: (Kg) '))
altura = float(input('Digite sua altura: (m) '))
imc = peso / (altura ** 2)
print('O seu IMC é {:.2f}, '.format(imc), end='')
if imc < 18.5:
 print('classificado como abaixo do peso.')
elif 18.5 <= imc < 25:
 print('classificado como peso normal.')
elif 25 <= imc < 30:
 print('classificado como sobrepeso.')
elif 30 <= imc < 35:
 print('classificado como obesidade grau I.')
elif 35 <= imc < 40:
 print('classificado como obesidade grau II.')
else:
 print('classificado como obesidade grau III ou Mórbida.')