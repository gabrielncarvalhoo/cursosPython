import random
lista = range(1, 6)
sorteio = random.choice(lista)
tentativa = int(input('Tente acertar qual número entre 1 e 5 o computador escolheu: '))
print('O número escolhido pelo computador foi {}.'.format(sorteio))
if sorteio == tentativa:
    print('Você acertou!!!')
else:
    print('Você errou!')