
sugestoes = ['001#Sugestão#Requisitante: Gabriel#Descrição: Colocar ar-condicionado nas salas.', '004#Sugestão#Requisitante: Brendda#Descrição: Livros novos na biblioteca.']
reclamacoes = ['002#Reclamação#Requisitante: Jeneffer#Descrição: Falta água nos corredores.', '005#Reclamação#Requisitante: Pedro#Descrição: Janela da sala 201 está quebrada.']
elogios = ['003#Elogio#Requisitante: Daniel#Descrição: Limpeza está em dia.', '006#Elogio#Requisitante: Lucas Lapenda#Descrição: Aulas no meu nível.']
todasmanifestacoes = sugestoes + reclamacoes + elogios
opcao = 0

while opcao != 7:
    print('=-' * 25)
    print(f'{"Ouvidoria Universidade ABC": ^50}')
    print(f'{"MENU": ^50}')
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
        print(f'{"TODAS AS MANIFESTAÇÕES": ^50}\n')
        for manifestacoes in todasmanifestacoes:
            todasmanifestacoes.sort()

            print(f'Protocolo: {manifestacoes.split("#")[0]}')
            print(manifestacoes.split("#")[1])
            print(manifestacoes.split("#")[2])
            print(manifestacoes.split("#")[3])
            print('-' * 50)
            print()


    #[ 2 ] Listar todas as sugestões
    elif opcao == 2:
        print(f'{"TODAS AS SUGESTÕES": ^50}\n')
        for manifestacoes in sugestoes:
            print(f'Protocolo: {manifestacoes.split("#")[0]}')
            print(manifestacoes.split("#")[2])
            print(manifestacoes.split("#")[3])
            print('-' * 50)
            print()


    #[ 3 ] Listar todas as reclamações
    elif opcao == 3:
        print(f'{"TODAS AS RECLAMAÇÕES": ^50}\n')
        for manifestacoes in reclamacoes:
            print(f'Protocolo: {manifestacoes.split("#")[0]}')
            print(manifestacoes.split("#")[2])
            print(manifestacoes.split("#")[3])
            print('-' * 50)
            print()


    #[ 4 ] Listar todos os elogios
    elif opcao == 4:
        print(f'{"TODAS OS ELOGIOS": ^50}\n')
        for manifestacoes in elogios:
            print(f'Protocolo: {manifestacoes.split("#")[0]}')
            print(manifestacoes.split("#")[2])
            print(manifestacoes.split("#")[3])
            print('-' * 50)
            print()


    #[ 5 ] Enviar nova manifestação *Não sei como deu certo, mas deu.
    elif opcao == 5:

        while True:
            nome = input('Digite o nome do requisitante: ').capitalize().strip()
            print()
            print(f'{nome}, qual o tipo de manifestação deseja fazer?')
            print("""[ 1 ] Sugestão \n[ 2 ] Reclamação \n[ 3 ] Elogio \n[ 4 ] Voltar par o menu""")
            tipo = int(input('Digite a opção desejada: '))
            if tipo == 4:
                print()
                break
            descricao = input('Digite a descrição: ').capitalize().strip()
            codigo = int(todasmanifestacoes[len(todasmanifestacoes) - 1].split('#')[0])  # número do último protocolo
            codigo += 1



            #Inserir Sugestão
            if tipo == 1:
                sugestoes.append(f'{str(codigo).zfill(3)}#Sugestão#Requisitante: {nome}#Descrição: {descricao}')
                todasmanifestacoes.append(sugestoes[len(sugestoes) - 1])
                print('\nManifestação inserida!')
                break

            #Inserir reclamação
            elif tipo == 2:
                reclamacoes.append(f'{str(codigo).zfill(3)}#Reclamação#Requisitante: {nome}#Descrição: {descricao}')
                todasmanifestacoes.append(reclamacoes[len(reclamacoes) - 1])
                print('\nManifestação inserida!')
                break

            #Inserir Elogios
            elif tipo == 3:
                elogios.append(f'{str(codigo).zfill(3)}#Elogio#Requisitante: {nome}#Descrição: {descricao}')
                todasmanifestacoes.append(elogios[len(elogios) - 1])
                print('\nManifestação inserida!')
                break


            else:
                print('\nValor Inválido!!')
                continue


    #[ 6 ] Pesquisar protocolo por número (ID)
    elif opcao == 6:
        while True:
            pesquisa = input('Digite o número do protocolo: ').strip()
            print('-' * 50)
            print()
            protocolo = [s for s in todasmanifestacoes if pesquisa in s]
            if protocolo:
                for p in range(0, len(protocolo)):
                    if pesquisa in protocolo[p].split('#')[0]:
                        protocolo.sort()
                        numeroprotocolo = int(protocolo[p].split('#')[0])
                        print(protocolo[p].split('#')[0])
                        print(protocolo[p].split('#')[1])
                        print(protocolo[p].split('#')[2])
                        print(protocolo[p].split('#')[3])
                        print('-' * 50)

            else:
                print('Protocolo não encontrado')
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
