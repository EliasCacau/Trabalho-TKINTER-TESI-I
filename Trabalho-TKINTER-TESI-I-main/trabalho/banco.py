class Banco:
    bancos = []
    def __init__(self, num, nome):
        self._num = num
        self._nome = nome
        self._contas = []

    #Métodos
    def __str__(self):
        return self._nome
    @property
    def num(self):
        return self._num

    @num.setter
    def num(self, valor):
        self._num = valor

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor

    @property
    def contas(self):
        return self._contas

    def adicionar_conta(self, conta):
        self._contas.append(conta)
        return self._contas

    def adicionar_banco(cls, banco):
        Banco.bancos.append(banco)
        return Banco.bancos
