from id import Id
from extrato import Extrato


class Conta(Id):
    contas = []
    def __init__(self, num, cli):
        super().__init__()
        self._numero = num
        self._titular = cli
        self._saldo = 0
        self._status = "Ativo"
        self._id = 0
        self._banco = ''
        self._taxa = 0
        self._extrato = Extrato()

    #Métodos
    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, valor):
        self._numero = valor

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, valor):
        self._titular = valor

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        self._saldo = valor

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, valor):
        self._status = valor

    @property
    def id(self):
        return self._id

    @property
    def banco(self):
        return self._banco

    @banco.setter
    def banco(self, valor):
        self._banco = valor

    @property
    def extrato(self):
        return self._extrato.extrato

    def saque(self, valor):
        if self._saldo >= valor:
            self._saldo = self._saldo - valor
        return self._saldo

    def deposito(self, valor):
        self._saldo = self._saldo + valor
        return self._saldo

    def add_conta(cls, conta):
        Conta.contas.append(conta)
        return Conta.contas

    def imprimir_extrato(self):
        return self._extrato.imprimir(self.id)


