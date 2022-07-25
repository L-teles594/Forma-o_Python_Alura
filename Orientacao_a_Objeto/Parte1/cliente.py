class Cliente:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome.title()

    @nome.setter
    def nome(self, nome):
        self.__nome = nome


if __name__ == '__main__':
    cliente = Cliente('osmar')
    print(cliente.nome)
    cliente.nome = 'carlos'
    print(cliente.nome)
