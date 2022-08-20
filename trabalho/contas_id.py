class Id:
    conta_id = 0
    contaPoupanca_id = 0
    contaCorrente_id = 0
    contador = 0
    def __init__(self):
        pass
    
    #Ao criar uma nova conta, devido a herança na conta poupança e conta corrente, é incrementado
    # mais um novo id para a conta_id, como modo de manter o registro apenas da conta_id
    # Foi Colocado um contador, ele vai contar quantas contas foram criadas na conta poupança/corrente
    # E depois subtraido com o numero total de contas criadas
    def id_conta(cls):
        Id.conta_id += 1
        valor = Id.conta_id - Id.contador
        return valor

    def id_contaPoupanca(cls):
        Id.contaPoupanca_id += 1
        Id.contador += 1
        return Id.contaPoupanca_id

    def id_contaCorrente(cls):
        Id.contaCorrente_id += 1
        Id.contador += 1
        return Id.contaCorrente_id
