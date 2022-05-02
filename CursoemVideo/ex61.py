num1 = int(input('Primeiro termo: '))
num2 = int(input('Razão: '))
cont = 1
while cont <= 10:
    cont += 1
    print(num1, end=' → ')
    num1 += num2
print('ACABOU!!')

