import advinhacao
while True:
    print('*' * 32)
    print('1 - Advinhação')
    print('2 - Forca')
    escolha = input('Escolha o seu jogo pelo número: ')
    if escolha == '1':
        advinhacao.main()
    elif escolha == '2':
        pass
    else:
        print('Faça uma escolha válida')
    if input('Deseja jogar novamente [s/n]: ').lower()[0] == 'n':
        break
