from conta import Conta
from contaCorrente import ContaCorrente
from contaPoupanca import ContaPoupanca

conta1 = Conta(123, "Elias", 50)
conta2 = Conta(1234, "Elias", 50)

cc1 = ContaCorrente(123, "Elias", 50)
cc2 = ContaCorrente(123, "Elias", 50)
cc3 = ContaCorrente(123, "Elias", 50)
cc4 = ContaCorrente(123, "Elias", 50)
cc5 = ContaCorrente(123, "Elias", 50)

conta3 = Conta(1234, "ELias", 100)
conta4 = Conta(1234, "ELias", 100)
conta5 = Conta(1234, "ELias", 100)
cc6 = ContaCorrente(123, "Elias", 50)
conta6 = Conta(1234, "ELias", 100)



print(conta1.id())
print(conta2.id())
print(cc1.id())
print(cc2.id())
print(cc3.id())
print(conta3.id())
print(conta5.id())
print(conta6.id())
print(cc6.id())


