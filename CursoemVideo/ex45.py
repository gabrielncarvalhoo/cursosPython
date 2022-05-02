import random
import time
print("""Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA""")
escolha = int(input('Qual é a sua escolha? '))
lista = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint(0, 2)
time.sleep(1)
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!!')
time.sleep(1)
print('O computador jogou {}'.format(lista[computador]))
print('Você jogou {}'.format(lista[escolha]))
if computador == 0: #PEDRA
    if escolha == 0:
        print('VOCÊ EMPATOU')
    elif escolha == 1:
        print('VOCÊ GANHOU!!!!')
    elif escolha == 2:
        print('VOCÊ PERDEU')
    else:
        print('JOGADA INVÁLIDA')

elif computador == 1: #PAPEL
    if escolha == 0:
        print('VOCÊ PERDEU')
    elif escolha == 1:
        print('VOCÊ EMPATOU')
    elif escolha == 2:
        print('VOCÊ GANHOU!!!!')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2: #TESOURA
    if escolha == 0:
        print('VOCÊ GANHOU!!!!')
    elif escolha == 1:
        print('VOCÊ PERDEU')
    elif escolha == 2:
        print('VOCÊ EMPATOU')
    else:
        print('JOGADA INVÁLIDA')