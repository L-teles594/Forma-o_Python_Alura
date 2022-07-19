def gerador_de_palavra_secreta():
    from random import choice
    with open('palavras.txt') as file:
        lista = file.read().split('\n')
    palavra = choice(lista)
    return palavra.lower()


def main():
    palavra_secreta = gerador_de_palavra_secreta()
    letras_adivinhadas = ['_' for letra in palavra_secreta]


if __name__ == '__main__':
    main()
