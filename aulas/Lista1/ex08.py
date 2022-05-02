nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
media = (nota1 + nota2) / 2
if media < 10 and media >= 7:
    print('Você está Aprovado!')
elif media < 7:
    print('Você está Reprovado.')
else :
    print('Você foi Aprovado com Distinção!!!')