class Conta:
    def __init__(self, numero, nome, saldo, limite=1000):
        self.__limite = limite
        self.__saldo = saldo
        self.__nome = nome
        self.__numero = numero

    def sacar(self, valor):
        self.__saldo -= valor if self.pode_sacar(valor) else print('Você não tem limite para saque.')

    def depositar(self, valor):
        self.__saldo += valor

    def extrato(self):
        return f'{self.__nome} seu saldo é de R${self.__saldo:.2f}'

    def transferir(self, recebedor, valor):
        self.__saldo -= valor
        recebedor.depositar(valor)

    def __pode_sacar(self, valor_a_sacar):
        return valor_a_sacar <= 1000 + self.__saldo

    # Getters com @property
    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__nome

    @property
    def limite(self):
        return self.__limite

    # Setter com @propriedade.setter
    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    # métodos de classe
    @staticmethod
    def codigo_dos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}

    @staticmethod
    def codigo_do_banco():
        return '001'
