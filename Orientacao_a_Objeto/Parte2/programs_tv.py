class Programa:
    def __init__(self, nome, ano):
        self._likes = 0
        self.ano = ano
        self._nome = nome.title()

    @property
    def likes(self):
        return self._likes

    def deu_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas


if __name__ == '__main__':
    vingadores = Filme('vingadores - guerra infinita', 2018, 160)
    print(vingadores.nome)
