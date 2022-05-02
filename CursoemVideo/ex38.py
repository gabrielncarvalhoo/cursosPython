num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
maior = max(num1, num2)
if maior == num1 and maior != num2:
    print('Primeiro número é maior.')
elif maior == num2 and maior != num1:
    print('Segundo número é maior.')
elif maior == num1 and maior == num2:
    print('Os dois são iguais.')