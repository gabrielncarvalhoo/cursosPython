num1 = int(input('Primeiro termo: '))
num2 = int(input('Razão: '))
termo = num1
cont = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while cont <= total:
        print(termo, end=' → ')
        termo += num2
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('ACABOU!!')
