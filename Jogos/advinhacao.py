def apresentacao():
    print('*' * 32)
    print('Bem vindo ao jogo de Adivinhação')
    print('*' * 32)


def gerar_numero():
    from random import randint
    return randint(0, 100)


def chutando_numero():
    print('*' * 32)
    while True:
        chute = input('Digite um número inteiro entre 0 e 100: ')
        if chute.isdigit():
            chute = int(chute)
            return chute
        print('Por favor digite um número inteiro.')


def dificuldade():
    print('*' * 32)
    print('0 - Fácil - 12 tentativas')
    print('1 - Normal - 8 tentativas')
    print('2 - difícil - 5 tentativas', '\n')
    escolha = input('Escolha a sua dificuldade pelo número: ')
    print('*' * 32)

    escolha = int(escolha) if escolha.isdigit() else dificuldade()

    dificuldades = [12, 8, 5]

    try:
        return dificuldades[escolha]
    except IndexError:
        print('Digite uma difículdade válida')
        dificuldade()


def main():
    apresentacao()
    tentativas = dificuldade()
    print(f'Você tem {tentativas} tentativas')
    numero_secreto = gerar_numero()
    print(numero_secreto)
    chute = chutando_numero()

    while tentativas > 1:
        print('*' * 32)
        if chute == numero_secreto:
            print('Você acertou!')
            return
        else:
            if chute > numero_secreto:
                print('Você errou! seu chute foi maior que o número secreto.')
            elif chute < numero_secreto:
                print('Você errou! seu chute foi menor que o número secreto.')
            tentativas -= 1
        print(f'Você tem {tentativas} tentativas')
        chute = chutando_numero()
    print(f'Você ficou sem tentativas, o número secreto era {numero_secreto}')


if __name__ == '__main__':
    main()
