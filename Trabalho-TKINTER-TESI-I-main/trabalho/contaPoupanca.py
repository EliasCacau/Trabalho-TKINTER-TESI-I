from conta import Conta
from id import Id
from datetime import datetime


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

    def saque(self, valor):
        if self._saldo >= valor:
            tipo = "Saque"
            self._saldo = self._saldo
            self._saldo = self._saldo - valor
            self.movimentacao(tipo, valor)
        return self._saldo

    def deposito(self, valor):
        tipo = "Deposito"
        self._saldo = self._saldo
        self._saldo = self._saldo + valor
        self.movimentacao(tipo, valor)
        return self._saldo

    def add_conta(cls, conta):
        ContaPoupanca.contas_cp.append(conta)
        return ContaPoupanca.contas_cp

    def movimentacao(self, tipo, valor):
        today = datetime.now()
        day = today.strftime("%d/%m/%Y às %H:%M")
        self.extrato.append(
            f"|{tipo}| no valor de {valor:.2f}| {day}|"
        )