distancia = int(input('Qual a distância de sua viagem: '))
if distancia <= 200:
    print('Sua viagem de {}Km ficará por R${:.2f}'.format(distancia, distancia * 0.5))
else:
    print('Sua viagem de {}Km ficará por R${:.2f}'.format(distancia, distancia * 0.45))
