class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print("Saque realizado com sucesso.")
            print(f"Novo saldo: R${self.saldo:.2f}")
        else:
            print("Saldo insuficiente.")

conta = ContaBancaria("Maria", 200.00)

conta.sacar(300.00)