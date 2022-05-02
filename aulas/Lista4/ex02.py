usuario = ''
senha = ''
while usuario == senha:
    usuario = input('Digite seu nome: ').upper()
    senha = input('Digite sua senha: ').upper()
    if usuario == senha:
        print('=-='*15)
        print('A senha não pode ser igual ao usuário.')
        print('=-=' * 15)
print('Cadastrado!')