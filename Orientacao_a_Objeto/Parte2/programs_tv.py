class Filme:
    def __init__(self, nome, ano, duracao):
        self.__likes = 0
        self.duracao = duracao
        self.ano = ano
        self.__nome = nome.title()

    @property
    def likes(self):
        return self.__likes

    def deu_like(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()


class Serie:
    def __init__(self, nome, ano, temporadas):
        self.__likes = 0
        self.temporadas = temporadas
        self.ano = ano
        self.__nome = nome.title()

    @property
    def likes(self):
        return self.__likes

    def deu_like(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()


if __name__ == '__main__':
    vingadores = Filme('vingadores - guerra infinita', 2018, 160)
    print(vingadores.nome)
