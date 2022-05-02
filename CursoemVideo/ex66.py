soma = 0
cont = 0
while True:
    valor = int(input('Digite um valor [0 interrompe]: '))
    if valor == 0:
        break
    soma += valor
    cont += 1
print(f'São {cont} valores e a soma de todos é {soma}')