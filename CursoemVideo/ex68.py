from random import randint
vitoria = 0
print('=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')

while True:
    print('=-' * 20)
    valor = int(input('Diga um valor: '))
    parouimpar = ' '
    computador = randint(0, 11)
    soma = valor + computador
    while parouimpar not in 'PI':
        parouimpar = input('Par ou Ímpar? [P/I] ').upper()
    print('-' * 40)
    print(f'Você jogou {valor} e o computador {computador}. Total de {soma} ', end='')
    print('DEU PAR' if soma % 2 == 0 else 'DEU ÍMPAR')
    print('-' * 40)
    if parouimpar == 'P':
        if soma % 2 == 0:
            print('Você VENCEU!')
            vitoria += 1
        else:
            print('Você PERDEU!!')
            break
    elif parouimpar == 'I':
        if soma % 2 == 1:
            print('Você VENCEU!')
            vitoria += 1
        else:
            print('Você PERDEU!!')
            break
    print('Vamos Jogar novamente...')
print(f'GAME OVER! Você venceu {vitoria} vezes')
