altura = float(input('Digite sua altura (em m): '))
hm = str(input('Digite se você é homem ou mulher: ')).upper().strip()
if hm == 'HOMEM':
    print('Seu peso ideal é {:.1f}.'.format((72.7 * altura) - 58))
elif hm == 'MULHER':
    print('Seu peso ideal é {:.1f}.'.format((62.1 * altura) - 44.7))
else:
    print('Aprenda a digitar!!')