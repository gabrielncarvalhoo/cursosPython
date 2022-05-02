num1 = int(input('Primeiro termo: '))
num2 = int(input('Razão: '))
numfim = num1 + num2 * 10
for c in range(num1, numfim, num2):
    print(c, end=' → ')
print('ACABOU!!')