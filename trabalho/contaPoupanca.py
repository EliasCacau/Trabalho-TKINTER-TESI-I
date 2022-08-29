from trabalho.conta import Conta
from trabalho.id import Id


class ContaPoupanca(Conta, Id):
    contas_cp = []

    def __init__(self, num, cli):
        super().__init__(num, cli)
        self._id = Id.id_contaPoupanca(self)
        self._taxa = 10

    def passar_mes(self):
        self._saldo = self._saldo * 0.1
        return self._saldo

    @property
    def taxa(self):
        return self._taxa

    def add_conta(cls, conta):
        ContaPoupanca.contas_cp.append(conta)
        return ContaPoupanca.contas_cp