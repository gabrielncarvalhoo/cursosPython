media = 0
mulher = 0
idadeh = []
idadem = []
nomeh = []
for p in range(1, 5):
    print('{} {}° PESSOA {}'.format('-'*5, p, '-'*5))
    nome = str(input('Nome: ')).strip().capitalize()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    media += idade / 4
    if sexo == 'M':
        idadeh += [idade]
        if idade == max(idadeh):
            nomeh = nome
    if sexo == 'F':
        idadem += [idade]
        if idadem < [20]:
            mulher += 1


print('A média de idade é de {:.1f} anos.'.format(media))
if idadeh == 0:
    print('Não exisatem homens em análise.')
else:
    print('O homem mais velho tem {} anos e se chama {}.'.format(max(idadeh), nomeh))
print('Ao todo são {} mulheres com menos de 20 anos'.format(mulher))
