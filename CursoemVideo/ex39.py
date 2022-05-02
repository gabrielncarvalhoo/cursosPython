from datetime import date
ano = int(input('Ano do nascimento: '))
anoatual = date.today().year
idade = anoatual - ano
print('Quem naceu em {} tem {} anos em {}.'.format(ano, idade, anoatual))
if idade == 18:
    print('Você deve se alistar imediatamente!')
elif idade < 18:
    tempo = 18 - idade
    anoalistamento = anoatual + tempo
    print('Ainda faltam {} anos para o alistamento.'.format(tempo))
    print('Seu alistamento será em {}.'.format(anoalistamento))
else:
    tempo = idade - 18
    anoalistamento = anoatual - tempo
    print('Você já deveria ter se alistado há {} anos.'.format(tempo))
    print('Seu alistamento foi em {}.'.format(anoalistamento))