from datetime import date
ano = int(input('Digite o ano para saber se ele é bissexto ou não: '))
if ano == 0:
    ano = date.today().year
caso1 = ano % 4
caso2 = ano % 100
caso3 = ano % 400
if caso1 == 0 and caso2 != 0 or caso1 == 0 and caso2 == 0 and caso3 == 0:
    print('O ano é bissexto!')
else:
    print('O ano não é bissexto')
print(ano)
