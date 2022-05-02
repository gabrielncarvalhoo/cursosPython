
while True:
    valor = int(input('Quer ver a tabuada de qual valor? '))
    if valor < 0:
        break
    for tabuada in range(1, 11):
        print(f'{valor} X {tabuada:>2} = {valor * tabuada}')
