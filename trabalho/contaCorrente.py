from trabalho.conta import Conta
from trabalho.contas_id import Id


class ContaCorrente(Conta, Id):
    def __init__(self, num, cli, saldo):
        super().__init__(num, cli, saldo)
        self._taxa = 0.05
        self._id = Id.id_contaCorrente(self)


    def saque(self, valor):
        if self._saldo >= valor:
            self._saldo = self._saldo * self._taxa
            self._saldo = self._saldo - valor
        else:
            print("Saldo insuficiente")
        return self._saldo

    def deposito(self, valor):
        self._saldo = self._saldo * self._taxa
        self._saldo = self._saldo + valor
        return self._saldo