from time import sleep
velocidade = int(input('Qual a velocidade que você passou? '))
multa = (velocidade - 80) * 7
print('PROCESSANDO....')
sleep(3)
if multa == 0:
    print('Muito bem!! Você está dirigindo na velocidade permitida.')
else:
    print('VOCÊ FOI MULTADO! O valor de sua multa é de R${:.2f}'.format(multa))