numero = 0
soma = 0
cont = 0
while numero != 999:
    numero = int(input('Digite um número [999 para parar]: '))
    if numero == 999:
        break
    cont += 1
    soma += numero
print('Você digitou {} números e a soma entre eles foi {}'.format(cont, soma))