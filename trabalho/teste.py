from conta import Conta
from contaCorrente import ContaCorrente
from contaPoupanca import ContaPoupanca
from banco import Banco

banco1 = Banco(1, "Santander")

conta1 = Conta(123, "ISd", 50)
conta2 = Conta(1234, "Elias", 50)

cc1 = ContaCorrente(123, "Elias", 50)
cc2 = ContaCorrente(123, "Elias", 50)
cc3 = ContaCorrente(123, "Elias", 50)
cc4 = ContaCorrente(123, "Elias", 50)
cc5 = ContaCorrente(123, "Elias", 50)

conta3 = Conta(1234, "ELias", 100)
conta4 = Conta(1234, "ELias", 100)
conta5 = Conta(1234, "ELias", 100)
cc6 = ContaCorrente(123, "ESA", 50)
conta6 = Conta(1234, "E", 100)

# print(banco1.adicionar_conta(conta1))
# banco1.adicionar_conta(conta6)
# print(banco1.adicionar_conta(cc6))
# for i in banco1.contas:
#     print(i.titular)
# print(banco1.contas[1].titular)

#print(conta1.id())
#print(conta2.id())
print(cc1.id())
print(cc2.id())
print(cc3.id())
#print(conta3.id())
#print(conta5.id())
#print(conta6.id())
print(cc6.id())
print(banco1)


