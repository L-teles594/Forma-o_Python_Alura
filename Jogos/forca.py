def artes_enforcado(ind):
    from arte import enforcado
    print(enforcado[ind])


def formata_palavra(palavra):
    lista = ['á', 'à', 'ã', 'â', 'é', 'ê', 'í', 'ó', 'ô', 'ú']
    vogais = 'aeiou'
    nova_palavra = ''

    for letra in palavra:
        if letra in lista:
            if 0 <= lista.index(letra) <= 3:
                nova_palavra += vogais[0]
            elif 4 <= lista.index(letra) <= 5:
                nova_palavra += vogais[1]
            elif lista.index(letra) == 6:
                nova_palavra += vogais[2]
            elif 7 <= lista.index(letra) <= 8:
                nova_palavra += vogais[3]
            elif lista.index(letra) == 9:
                nova_palavra += vogais[4]
        else:
            nova_palavra += letra

    return nova_palavra


def gerador_de_palavra_secreta():
    from random import choice
    with open('palavras.txt') as file:
        lista = file.read().split('\n')
    palavra = choice(lista)
    palavra = formata_palavra(palavra.lower())
    return palavra


def main():
    palavra_secreta = gerador_de_palavra_secreta()
    letras_adivinhadas = ['_' for letra in palavra_secreta]
    letras_usadas = []
    tentativas = 6

    while ('_' in letras_adivinhadas) and tentativas > 0:
        artes_enforcado(tentativas)
        print(''.join(letras_adivinhadas))
        chute = input('Digite uma letra: ').strip()[0]

        if chute in letras_usadas:
            print('Vecê já chutou essa letra!')
            continue
        if chute in palavra_secreta:
            for ind, letra in enumerate(palavra_secreta):
                if chute == letra:
                    letras_adivinhadas[ind] = letra
        else:
            tentativas -= 1

        letras_usadas.append(chute)
        print(f'letras chutadas: {" ".join(letras_usadas)}')

    artes_enforcado(tentativas)
    print(''.join(letras_adivinhadas))

    if tentativas > 0:
        print('Você acertou a palavra secreta, Parabéns!')
    else:
        print(f'Você foi enforcado, a palavra secreta era {palavra_secreta}')


if __name__ == '__main__':
    main()
