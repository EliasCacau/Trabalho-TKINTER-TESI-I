class Cliente:
    def __init__(self, n, e, cpf):
        self._nome = n
        self._endereco = e
        self._cpf = cpf

    #Métodos
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor

    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, valor):
        self._endereco = valor

    @property
    def cpf(self):
        return self._endereco

    @cpf.setter
    def cpf(self, valor):
        self.cpf = valor
