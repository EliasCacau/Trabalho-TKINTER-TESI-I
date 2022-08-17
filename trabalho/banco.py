class Banco:
    def __init__(self, num, nome):
        self._num = num
        self._nome = nome
        self._contas = []

    #Métodos
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

