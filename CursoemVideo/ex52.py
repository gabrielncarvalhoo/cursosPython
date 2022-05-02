num = int(input('Digite um número: '))
div = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[0;33m{}'.format(c), end=' ')
        div += 1
    else:
        print('\033[0;31m{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezes.'.format(num, div))
print('E por isso ele ', end='')
if div <= 2:
    print('É PRIMO')
else:
    print('NÃO É PRIMO')