class ClienteId:
    clienteId = 0
    def __init__(self):
        pass

    def id_cliente(cls):
        ClienteId.clienteId += 1
        return ClienteId.clienteId