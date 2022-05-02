import time
nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
media = (nota1 + nota2) / 2
print('CALCULANDO...')
time.sleep(2)
if media >= 9 and media <= 10:
    print('\033[1;31mPARABÉNS, VOCÊ É INCRIVEL!! CONCEITO A\033[m')
elif media >= 7.5 and media < 9:
    print('Parabéns!! Conceito B')
elif media >= 6 and media < 7:
    print('Você passou! Conceito C')
elif media >= 4 and media < 6:
    print('Quase passou. Conceito D')
else:
    print('Estude mais!!! Conceito E')