par = 0
impar = 0
for num in range(1, 11):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        par += 1
    if num % 2 != 0:
        impar += 1
print(f'{par} - Par \n{impar} - Impar')