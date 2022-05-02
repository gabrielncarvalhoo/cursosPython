import time
peso = float(input('Quantidade em quilos de peixe: '))
excesso = peso - 50
multa = excesso * 4
print('\033[1;34mPROCESSANDO...\033[m')
time.sleep(2)
if peso > 50:
    print('\033[1;31mVOCÊ FOI MULTADO EM R${:.2f}!!!\033[m Você excedeu o limitte diário em {:.1f}Kg.'.format(multa, excesso))
else:
    Print('Você não excedeu o limite diário.')