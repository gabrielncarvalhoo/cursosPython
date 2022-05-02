num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print("""   [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos valores
    [ 5 ] Sair do programa""")
    opcao = int(input('>>>>> Qual é a sua opção? '))
    if opcao == 1:
        print('{} + {} = {}'.format(num1, num2, num1 + num2))
    elif opcao == 2:
        print('{} X {} = {}'.format(num1, num2, num1 * num2))
    elif opcao == 3:
        print('Entre {} e {}, o número {} é o maior.'.format(num1, num2, max(num1, num2)))
    elif opcao == 4:
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
    elif opcao == 5:
        break
    else:
        print('Opção Inválida.')
    print('=-='*10)
print('Programa Finalizado.')
