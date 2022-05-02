salario = float(input('Seu salário por hora: R$'))
horas = int(input('Horas trabalhadas no mês: R$'))
salariobruto = horas * salario
ir = salariobruto * 0.11
inss = salariobruto * 0.08
sindicato = salariobruto * 0.05
salarioliquido = salariobruto - (ir + inss + sindicato)
print('+ Salário Bruto: R${:.2f}'.format(salariobruto))
print('- IR: R${:.2f}'.format(ir))
print('- INSS: R${:.2f}'.format(inss))
print('- Sindicato: R${:.2f}'.format(sindicato))
print('= Salário Líquido: R${:.2f}'.format(salarioliquido))
