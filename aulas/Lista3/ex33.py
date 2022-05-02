num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite outro número: '))
if num1 > num2 and num1 > num3:
    print('O maior número é {}'.format(num1))
elif num2 > num1 and num2 > num3:
    print('O maior número é {}'.format(num2))
else:
    print('O maior número é {}'.format(num3))


if num1 < num2 and num1 < num3:
    print('O menor número é {}'.format(num1))
elif num2 < num1 and num2 < num3:
    print('O menor número é {}'.format(num2))
else:
    print('O menor número é {}'.format(num3))
    