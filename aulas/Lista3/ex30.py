genero = str(input('Digite seu sexo(F ou M): ')).upper().strip()
if genero == 'F':
    print('Seu sexo é Feminino.')
elif genero == 'M':
    print('Seu sexo é Masculino.')
else:
    print('Sexo Inválido.')