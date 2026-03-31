class Conta:
    def __init__(self, numero, titular, saldo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print("Depósito realizado com sucesso!")
        print(f"Novo saldo de {self.titular}: R$ {self.saldo:.2f}")

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente para saque!")
            print(f"Saldo atual de {self.titular}: R$ {self.saldo:.2f}")
        else:
            self.saldo -= valor
            print("Saque realizado com sucesso!")
            print(f"Novo saldo de {self.titular}: R$ {self.saldo:.2f}")

    def transferir(self, valor, destino):
        if valor > self.saldo:
            print("Saldo insuficiente para transferência!")
            print(f"Saldo atual de {self.titular}: R$ {self.saldo:.2f}")
        else:
            self.saldo -= valor
            destino.saldo += valor
            print("Transferência realizada com sucesso!")
            print(f"Saldo de {self.titular}: R$ {self.saldo:.2f}")
            print(f"Saldo de {destino.titular}: R$ {destino.saldo:.2f}")

conta1 = Conta(1, "João", 1000.00)
conta2 = Conta(2, "Maria", 500.00)

print("Saldo inicial:")
print(f"{conta1.titular}: R$ {conta1.saldo:.2f}")
print(f"{conta2.titular}: R$ {conta2.saldo:.2f}")

conta1.depositar(200.00)

conta2.sacar(300.00)

conta1.transferir(400.00, conta2)

conta2.sacar(1000.00)

print("\nSaldo final:")
print(f"{conta1.titular}: R$ {conta1.saldo:.2f}")
print(f"{conta2.titular}: R$ {conta2.saldo:.2f}")