from trabalho.conta import Conta
from trabalho.id import Id


class ContaPoupanca(Conta, Id):
    def __init__(self, num, cli):
        super().__init__(num, cli)
        self._id = Id.id_contaPoupanca(self)

    def passar_mes(self):
        self._saldo = self._saldo * 0.1
        return self._saldo