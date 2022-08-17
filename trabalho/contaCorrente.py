from trabalho.conta import Conta


class ContaCorrente(Conta):
    def __init__(self, num, cli, saldo):
        super().__init__(num, cli, saldo)