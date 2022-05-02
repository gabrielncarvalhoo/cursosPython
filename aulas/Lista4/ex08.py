numero = []
soma = 0
for num in range(1, 6):
    num = int(input('Digite um número: '))
    soma += num
    #numero.append(num)
media = soma / 5
print(f'A soma é {soma} e a média é {media:.1f}')