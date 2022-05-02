from manifestacoes import Todasmanifestacoes
from listas import listatodasmanifestacoes

opcao = 0

while opcao != 7:
    print('=-' * 25)
    print(f'\033[1;33m{"Ouvidoria Universidade ABC": ^50}\033[m')
    print(f'\033[1;33m{"MENU": ^50}\033[m')
    print()
    print()
    print('Opções: ')
    print("""    [ 1 ] Listar todas as manifestações
    [ 2 ] Listar todas as sugestões
    [ 3 ] Listar todas as reclamações
    [ 4 ] Listar todos os elogios
    [ 5 ] Enviar nova manifestação
    [ 6 ] Pesquisar protocolo por número (ID)
    [ 7 ] Sair""")
    opcao = int(input('Digite sua opção: '))
    print('=-' * 25)
    print()


    #[ 1 ] Listar todas as manifestações
    if opcao == 1:
        print(f'\033[1;33m{"TODAS AS MANIFESTAÇÕES": ^50}\033[m\n')
        for manifestacoes in listatodasmanifestacoes:
            print(f'Protocolo: {manifestacoes.id}')
            print(manifestacoes.estilo)
            print(f'Requisitante: {manifestacoes.nome}')
            print(f'Descrição: {manifestacoes.descricao}')
            print('-' * 50)
            print()


    #[ 2 ] Listar todas as sugestões
    elif opcao == 2:
        print(f'\033[1;33m{"TODAS AS SUGESTÕES": ^50}\033[m\n')
        for manifestacoes in listatodasmanifestacoes:
            if manifestacoes.estilo == 'Sugestão':
                print(f'Protocolo: {manifestacoes.id}')
                print(manifestacoes.estilo)
                print(f'Requisitante: {manifestacoes.nome}')
                print(f'Descrição: {manifestacoes.descricao}')
                print('-' * 50)
                print()


    #[ 3 ] Listar todas as reclamações
    elif opcao == 3:
        print(f'\033[1;33m{"TODAS AS RECLAMAÇÕES": ^50}\033[m\n')
        for manifestacoes in listatodasmanifestacoes:
            if manifestacoes.estilo == 'Reclamação':
                print(f'Protocolo: {manifestacoes.id}')
                print(manifestacoes.estilo)
                print(f'Requisitante: {manifestacoes.nome}')
                print(f'Descrição: {manifestacoes.descricao}')
                print('-' * 50)
                print()


    #[ 4 ] Listar todos os elogios
    elif opcao == 4:
        print(f'\033[1;33m{"TODAS OS ELOGIOS": ^50}\033[m\n')
        for manifestacoes in listatodasmanifestacoes:
            if manifestacoes.estilo == 'Elogios':
                print(f'Protocolo: {manifestacoes.id}')
                print(manifestacoes.estilo)
                print(f'Requisitante: {manifestacoes.nome}')
                print(f'Descrição: {manifestacoes.descricao}')
                print('-' * 50)
                print()

    #[ 5 ] Enviar nova manifestação.
    elif opcao == 5:

        while True:
            print('Qual o tipo de manifestação deseja fazer?')
            print("""[ 1 ] Sugestão \n[ 2 ] Reclamação \n[ 3 ] Elogio \n[ 4 ] Voltar par o menu""")
            tipo = int(input('Digite a opção desejada: '))
            if tipo == 4:
                print()
                break
            elif tipo < 1 or tipo > 4:
                print('\n\033[31mValor Inválido!!\033[m\n')
                continue

            prot = Todasmanifestacoes()
            prot.id = len(listatodasmanifestacoes) + 1
            prot.nome = input('Qual o nome do requisitante? ').capitalize().strip()
            prot.descricao = input('Digite a descrição: ').capitalize().strip()


            #Inserir Sugestão
            if tipo == 1:
                prot.estilo = 'Sugestão'
                listatodasmanifestacoes.append(prot)
                print('\nManifestação inserida!')
                break

            #Inserir reclamação
            elif tipo == 2:
                prot.estilo = 'Reclamação'
                listatodasmanifestacoes.append(prot)
                print('\nManifestação inserida!')
                break

            #Inserir Elogios
            elif tipo == 3:
                prot.estilo = 'Elogios'
                listatodasmanifestacoes.append(prot)
                print('\nManifestação inserida!')
                break





    #[ 6 ] Pesquisar protocolo por número (ID)
    elif opcao == 6:
        while True:
            pesquisa = int(input('Digite o número do protocolo: '))
            contador = 0
            print('-' * 50)
            print()
            for p in listatodasmanifestacoes:
                if p.id == pesquisa:
                    contador += 1
                    print(f'Protocolo: {p.id}')
                    print(p.estilo)
                    print(f'Requisitante: {p.nome}')
                    print(f'Descrição: {p.descricao}')
                    print('-' * 50)

            if contador < 1:
                print('\033[31mProtocolo não encontrado\033[m\n')
                print('-' * 50)

            continuar = input('Deseja fazer outra pesquisa? [S/N] ').upper().split()[0]
            if continuar == 'S':
                continue
            else:
                break


    #[ 7 ] Sair
    elif opcao == 7:
        break

    #Número invalido
    else:
        print('Opção inválida')
        continue