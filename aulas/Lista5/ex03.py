def converter(moeda):
    if moeda == 'D':
        conver = real / 4.94
    elif moeda == 'E':
        conver = real / 5.19
    elif moeda == 'P':
        conver = real * 0.043
    else:
        print('Moeda inválida!')
    return conver


valorreal = float(input('Digite o valor que deseja converter: R$'))
moedas = input('Para qual moeda deseja converter? [Dólar/Euro/Peso Argentino]').upper()[0]
print(f'O valor foi de {converter(valorreal, moedas):.2f} da moeda escolhida.')