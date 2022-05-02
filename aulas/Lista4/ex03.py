nome = input('Nome: ')
idade = int(input('Idade: '))
salario = int(input('Salário: R$'))
sexo = input('Sexo [F/M]: ').upper()[0]
estadocivil = input('Estado civil: ').upper()[0]
while len(nome) < 4:
    print('=-=' * 10)
    print('Nome Inválido')
    print('=-=' * 10)
    nome = input('Nome: ')

while idade < 0 or idade > 150:
    print('=-=' * 10)
    print('Idade Inválida')
    print('=-=' * 10)
    idade = int(input('Idade: '))

while salario > 0:
    print('=-=' * 10)
    print('Salário Inválido')
    print('=-=' * 10)
    salario = int(input('Salário: R$'))

while not sexo in 'MF':
    print('=-=' * 10)
    print('Sexo Inválido')
    print('=-=' * 10)
    sexo = input('Sexo [F/M]: ').upper()[0]

while not estadocivil in 'SCVD':
    print('=-=' * 10)
    print('Estado Civil Inválido')
    print('=-=' * 10)
    estadocivil = input('Estado civil: ').upper()[0]
print('Cadastrado com Sucesso!')
