from math import factorial
num = int(input('Digite um número para \ncalcular seu Fatorial: '))
fatorial = factorial(num)
print('{}! = {}'.format(num, num), end=' ')
while num != 1:
    num = num - 1
    print('X {}'.format(num), end=' ')
print('= {}'.format(fatorial))