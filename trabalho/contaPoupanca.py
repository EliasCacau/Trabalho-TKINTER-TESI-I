from trabalho.conta import Conta


class ContaPoupanca(Conta):
    def __init__(self, num, cli, saldo):
        super().__init__(num, cli, saldo)