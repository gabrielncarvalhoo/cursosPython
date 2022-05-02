filmes = ['F1', 'F2', 'F3', 'F4', 'F5']
filmeslocados = []
opcao = 0


while opcao != 5:
    print('=-'*20)
    print('Locadora AgixFilmes\n')
    print('Opções:')
    print('[ 1 ] Listar os filmes disponíveis')
    print('[ 2 ] Locar um filme disponível')
    print('[ 3 ] Listar os filmes que eu loquei')
    print('[ 4 ] Devolver Filme')
    print('[ 5 ] Sair do programa')
    opcao = int(input('Digite sua opção: '))
    print('=-' * 20)

    #[ 1 ] Listar os filmes disponíveis
    if opcao == 1:
        print('FILMES DISPONÍVEIS:\n')
        quantidadefilmes = len(filmes)
        for c in range(quantidadefilmes):
            print(f'{c + 1}) {filmes[c]}')

    #[ 2 ] Locar um filme disponível
    elif opcao == 2:
        print('Qual filme você deseja locar?')
        quantidadefilmes = len(filmes)
        for c in range(quantidadefilmes):
            print(f'{c + 1}) {filmes[c]}')
        locar = int(input('Digite o número do filme: \n'))
        print(f'Parabéns!!! Você escolheu o filme "{filmes[locar - 1]}".')

        #Adicionar filme a lista filmes locados
        filmeslocados.append(filmes[locar - 1])

        #Remover filme da lista de filmes
        filmes.remove(filmes[locar - 1])


    #[ 3 ] Listar os filmes que eu loquei
    elif opcao == 3:
        print('Você alugou os filmes listados abaixo:')
        quantidadefilmeslocados = len(filmeslocados)
        for l in range(quantidadefilmeslocados):
            print(f'{l + 1}) {filmeslocados[l]}')

    elif opcao == 4:
        print('Qual filme você deseja devolver?')
        quantidadefilmeslocados = len(filmeslocados)
        for l in range(quantidadefilmeslocados):
            print(f'{l + 1}) {filmeslocados[l]}')
        devolver = int(input('Digite o número do filme: \n'))
        print(f'Obrigado por devolver o filme "{filmes[devolver - 1]}".')

        # Adicionar filme a lista filmes
        filmes.append(filmes[devolver - 1])

        # Remover filme da lista de filmes
        filmeslocados.remove(filmeslocados[devolver - 1])



    elif opcao == 5:
        print('Programa Finalizado!!')

    else:
        print('Opção inválida!')
