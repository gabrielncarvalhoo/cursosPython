data = input('Digite uma data no formato dd/mm/aaa: ')
dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[6:10])
if dia < 0 or dia > 31:
    print('Dia inválido.')
if mes < 0 or mes > 12:
    print('Mês inválido.')
if ano < 0:
    print('Ano inválido.')

