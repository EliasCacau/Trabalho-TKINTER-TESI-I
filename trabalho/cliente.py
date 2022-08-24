from trabalho.id import Id


class Cliente(Id):
    clientes = []
    def __init__(self, n, cpf, e):
        super().__init__()
        self._nome = n
        self._endereco = e
        self._cpf = cpf
        self._id = Id.id_cliente(self)

    #Métodos
    def __str__(self):
        return self._nome

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
        return self._cpf

    @cpf.setter
    def cpf(self, valor):
        self.cpf = valor

    @property
    def id(self):
        return self._id

    def adicionar_clientes(cls, cliente):
        Cliente.clientes.append(cliente)
        return Cliente.clientes