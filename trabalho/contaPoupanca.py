from trabalho.conta import Conta
from trabalho.contas_id import Id


class ContaPoupanca(Conta, Id):
    def __init__(self, num, cli, saldo):
        super().__init__(num, cli, saldo)
        self._id = Id.id_contaPoupanca(self)

    def atualiza_conta(self):
        self._saldo = self._saldo * 0.1
        return self._saldo