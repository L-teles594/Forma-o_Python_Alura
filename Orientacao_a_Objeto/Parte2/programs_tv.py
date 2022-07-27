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

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes}'


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao}min - {self._likes}'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes}'


class Playlist:
    def __init__(self, nome, programas):
        self.programas = programas
        self.nome = nome

    def tamanho(self):
        return len(self.programas)


if __name__ == '__main__':
    vingadores = Filme('vingadores - guerra infinita', 2018, 160)
    atlanta = Serie('atlanta', 2018, 2)
    tmep = Filme('todo mundo em panico', 1999, 100)
    demolidor = Serie('demolidor', 2016, 2)

    vingadores.deu_like()
    atlanta.deu_like()
    tmep.deu_like()
    tmep.deu_like()
    demolidor.deu_like()
    demolidor.deu_like()
    demolidor.deu_like()
    atlanta.deu_like()
    # print(f'{vingadores.nome} - {vingadores.duracao} - Likes: {vingadores.likes}')
    # print(f'{atlanta.nome} - {atlanta.temporadas} - Likes: {atlanta.likes}')

    filmes_e_series = [vingadores, atlanta, demolidor, tmep]
    playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

    for programa in playlist_fim_de_semana.programas:
        print(programa.__str__())
