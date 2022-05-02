turno = str(input('Qual turno você estuda (M-matutinoou V-Vespertinoou N-Noturno)? ')).upper().strip()
if turno == 'M':
    print('Bom Dia!')
elif turno == 'V':
    print('Boa Tarde!')
elif turno == 'N':
    print('Boa Noite!')
else:
    print('Valor Inválido')