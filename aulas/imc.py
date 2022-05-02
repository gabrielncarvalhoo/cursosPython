peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)
#print('O seu IMC é {:.2f}'.format(imc))
if imc < 18.5:
 print('O seu IMC é {:.2f}, classificado como abaixo do peso.'.format(imc))
elif 18.5 <= imc < 25:
 print('O seu IMC é {:.2f}, classificado como peso normal.'.format(imc))
elif 25 <= imc < 30:
 print('O seu IMC é {:.2f}, classificado como sobrepeso.'.format(imc))
elif 30 <= imc < 35:
 print('O seu IMC é {:.2f}, classificado como obesidade grau I.'.format(imc))
elif 35 <= imc < 40:
 print('O seu IMC é {:.2f}, classificado como obesidade grau II.'.format(imc))
else:
 print('O seu IMC é {:.2f}, classificado como obesidade grau III ou Mórbida.'.format(imc))