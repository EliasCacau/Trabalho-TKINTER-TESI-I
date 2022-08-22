from trabalho.contas_id import Id


class Conta(Id):
    def __init__(self, num, cli, saldo):
        super().__init__()
        self._numero = num
        self._titular = cli
        self._saldo = saldo
        self._status = "Ativo"
        self._id = 0

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

    def saque(self, valor):
        if self._saldo >= valor:
            self._saldo = self._saldo - valor
        else:
            print("Saldo insuficiente")
        return self._saldo

    def deposito(self, valor):
        self._saldo = self._saldo + valor
        return self._saldo

    def status(self):
        if self._saldo <= 0:
            self._status = "Encerrada"
        return self._status

    def id(self):
        return self._id