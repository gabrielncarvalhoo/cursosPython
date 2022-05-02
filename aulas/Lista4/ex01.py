nota = int(input('Digite uma nota entre 0 e 10: '))
while nota < 0 or nota > 10:
    nota = int(input('Por favor, informe um valor válido: '))
print('Nota arquivada.')