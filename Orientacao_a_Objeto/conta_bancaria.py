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

