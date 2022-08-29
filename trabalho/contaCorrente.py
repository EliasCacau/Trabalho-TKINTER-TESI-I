from trabalho.conta import Conta
from trabalho.id import Id
from datetime import datetime

class ContaCorrente(Conta, Id):
    contas_cc = []

    def __init__(self, num, cli):
        super().__init__(num, cli)
        self._id = Id.id_contaCorrente(self)

    def saque(self, valor):
        if self._saldo >= valor:
            tipo = "Saque"
            taxa = 1
            self._saldo = self._saldo - taxa
            self._saldo = self._saldo - valor
            self.movimentacao(tipo, valor, taxa)
        return self._saldo

    def deposito(self, valor):
        tipo = "Deposito"
        taxa = 1
        self._saldo = self._saldo - taxa
        self._saldo = self._saldo + valor
        self.movimentacao(tipo, valor, taxa)
        return self._saldo

    def add_conta(cls, conta):
        ContaCorrente.contas_cc.append(conta)
        return ContaCorrente.contas_cc

    def movimentacao(self, tipo, valor, taxa):
        today = datetime.now()
        day = today.strftime("%d/%m/%Y às %H:%M")
        self.extrato.append(
            f"|{tipo}| no valor de {valor:.2f}, com taxa de {taxa:.2f}| {day}|"
        )
