class Conta:
    def __init__(self, numero, nome, saldo, limite=1000):
        self.__limite = limite
        self.__saldo = saldo
        self.__nome = nome
        self.__numero = numero

    def sacar(self, valor):
        self.__saldo -= valor

    def depositar(self, valor):
        self.__saldo += valor

    def extrato(self):
        return f'{self.__nome} seu saldo é de R${self.__saldo:.2f}'

    def transferir(self, recebedor, valor):
        self.__saldo -= valor
        recebedor.depositar(valor)

    # Getters
    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__nome

    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):
        self.__limite = limite

