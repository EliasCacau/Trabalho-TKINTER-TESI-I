class Conta:
    def __init__(self, num, cli, saldo):
        self._numero = num
        self._titular = cli
        self._saldo = saldo

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

