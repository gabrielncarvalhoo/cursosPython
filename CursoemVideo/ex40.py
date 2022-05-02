nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
media = (nota1 + nota2) / 2
print('Sua primeira nota foi {:.1f} e sua segunda nota foi {:.1f}, a média foi {:.1f}.'.format(nota1, nota2, media))
if media < 5:
    print('REPROVADO!')
elif media >= 5 and media < 7:
    print('Recuperação.')
else:
    print('APROVADO!')