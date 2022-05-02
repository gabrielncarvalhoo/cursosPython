print('\033[1;30;46mNóbrega Store\033[m')
produto = float(input('Digite o valor do produto: R$'))
print("""[ 1 ] À VISTA (DINHEIRO OU CHEQUE).
[ 2 ] NO CARTÃO DE CRÉDITO.""")
formapg = int(input('Selecione a forma de pagamento: '))
if formapg == 2:
    parcela = int(input('Em quantas parcelas você pretente dividir? '))
    if parcela == 1:
        desconto = produto * 0.05
        vfinal = produto - desconto
        print('Você possui um desconto de R${:.2f} e o valor do produto ficará por R${:.2f}.'.format(desconto, vfinal))
    elif parcela == 2:
        parcela2 = produto / 2
        print('O valor do produto é de R${:.2f} e ficará R${:.2f} por mês.'.format(produto, parcela2))
    else:
        acressimo = produto * 0.2
        vfinal = produto + acressimo
        parcela2 = vfinal / parcela
        print('O valor do seu acréssimo será de R${:.2f} e o preço final será de R${:.2f}. A parcela ficará R${:.2f} por Mês.'.format(acressimo, vfinal, parcela2))
elif formapg == 1:
    desconto = produto * 0.1
    vfinal = produto - desconto
    print('Você possui um desconto de R${:.2f} e o valor do produto ficará por R${:.2f}.'.format(desconto, vfinal))
else:
    print('Opção inválida!!')