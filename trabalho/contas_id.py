class Id:
    contaPoupanca_id = 0
    contaCorrente_id = 0
    def __init__(self):
        pass

    def id_contaPoupanca(cls):
        Id.contaPoupanca_id += 1
        return Id.contaPoupanca_id

    def id_contaCorrente(cls):
        Id.contaCorrente_id += 1
        return Id.contaCorrente_id
