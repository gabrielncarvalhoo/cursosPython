valor = 1
valores = []
soma = 0
while valor != 0:
    valor = int(input('Digite um valor [0 interrompe]: '))
    if valor == 0:
        break
    soma += valor
    valores.append(valor)
print(f'O maior valor é {max(valores)}, o menor é {min(valores)} e a soma de todos os valores é {soma}')