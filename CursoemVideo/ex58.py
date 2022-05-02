from random import choice
lista = range(101)
sorteio = choice(lista)
quantidadetentativa = 0
tentativa = int(input('Tente acertar qual número entre 0 e 100 que o computador escolheu: '))
while tentativa != sorteio:
    if tentativa < sorteio:
        print('Mais... Tente mais uma vez.')
    elif tentativa > sorteio:
        print('Menos... tente mais uma vez.')
    tentativa = int(input('Qual o seu palpite? '))
    quantidadetentativa += 1
print('Acertou com {} tentativas. Parabéns'.format(quantidadetentativa + 1))




